from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib
import os

# ---- paths ----
ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts")

model_path = os.path.join(ARTIFACTS_DIR, "fraud_model.joblib")
le_path = os.path.join(ARTIFACTS_DIR, "labelencoder.joblib")   # << no underscore
scaler_path = os.path.join(ARTIFACTS_DIR, "scaler.joblib")
features_path = os.path.join(ARTIFACTS_DIR, "important_features.joblib")

# ---- load artifacts once ----
try:
    model = joblib.load(model_path)
    le = joblib.load(le_path)
    scaler = joblib.load(scaler_path)
    important_features = joblib.load(features_path)
except Exception as e:
    raise RuntimeError(f"Failed to load artifacts: {e}")

ALLOWED_TYPES = [str(x) for x in getattr(le, "classes_", [])]  # e.g. ['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER']

app = FastAPI(title="Fraud Detection API", version="1.0")

# allow your Vue dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in prod, set to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    step: int
    type: str
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

@app.get("/")
def root():
    return {"status": "ready"}

@app.get("/features")
def features():
    return {
        "important_features_order": list(important_features),
        "allowed_transaction_types": ALLOWED_TYPES,
    }

@app.post("/predict")
def predict(transaction: Transaction):
    data = transaction.dict()

    # validate type
    if ALLOWED_TYPES and data["type"] not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=422,
            detail={
                "message": f"Unknown 'type': {data['type']}. Allowed: {ALLOWED_TYPES}"
            },
        )

    # encode categorical
    try:
        data["type"] = int(le.transform([data["type"]])[0])
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Label encoding error: {e}")

    # feature engineering (must mirror your training)
    data["balance_change_orig"] = data["newbalanceOrig"] - data["oldbalanceOrg"]
    data["balance_change_dest"] = data["newbalanceDest"] - data["oldbalanceDest"]
    data["transaction_ratio"] = data["amount"] / (data["oldbalanceOrg"] + 1)
    data["zero_balance_after"] = int(data["newbalanceOrig"] == 0)

    # arrange features in exact order the model expects
    try:
        X = np.array([[data[feat] for feat in important_features]], dtype=float)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing feature: {e}")

    # scale
    try:
        Xs = scaler.transform(X)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Scaling error: {e}")

    # predict + probability (robust to class order)
    try:
        pred = int(model.predict(Xs)[0])
        # pick the probability of label "1" if present
        class_list = list(getattr(model, "classes_", [0, 1]))
        pos_index = class_list.index(1) if 1 in class_list else 1
        prob = float(model.predict_proba(Xs)[0][pos_index])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")

    return {"prediction": pred, "fraud_probability": prob}
