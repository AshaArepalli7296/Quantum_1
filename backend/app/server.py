from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware  # ✅ added

app = FastAPI(title="Fraud Detection API")

# ---- Enable CORS for your frontend ----
origins = [
    "http://localhost:5173",  # Vue dev server
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Paths to artifacts ----
ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts","OnlineFraud")

model_path = os.path.join(ARTIFACTS_DIR, "fraud_model.joblib")
scaler_path = os.path.join(ARTIFACTS_DIR, "scaler.joblib")
features_path = os.path.join(ARTIFACTS_DIR, "important_features.joblib")

# ---- Load artifacts ----from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Fraud Detection API")

# ---- Enable CORS for your frontend ----
origins = [
    "http://localhost:5173",  # Vue dev server
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================
# CREDIT CARD MODEL ARTIFACTS
# ===========================
CREDIT_ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts", "CreditFraud")

try:
    rf_model = joblib.load(os.path.join(CREDIT_ARTIFACTS_DIR, "random_forest.joblib"))
    scaler_cc = joblib.load(os.path.join(CREDIT_ARTIFACTS_DIR, "scaler_selected.joblib"))
    selected_features = joblib.load(os.path.join(CREDIT_ARTIFACTS_DIR, "selected_features.joblib"))
except Exception as e:
    raise RuntimeError(f"Failed to load CreditCard artifacts: {e}")

# ===========================
# ONLINE PAYMENT MODEL ARTIFACTS
# ===========================
ONLINE_ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts", "OnlineFraud")

try:
    online_model = joblib.load(os.path.join(ONLINE_ARTIFACTS_DIR, "fraud_model.joblib"))
    scaler_online = joblib.load(os.path.join(ONLINE_ARTIFACTS_DIR, "scaler.joblib"))
    important_features = joblib.load(os.path.join(ONLINE_ARTIFACTS_DIR, "important_features.joblib"))
except Exception as e:
    raise RuntimeError(f"Failed to load OnlineFraud artifacts: {e}")


# ===========================
# ROUTES
# ===========================

@app.get("/")
def root():
    return {"message": "Welcome to Fraud Detection API"}


# ----- CREDIT CARD PREDICTION -----
@app.post("/predict/creditcard/")
def predict_credit_card(transaction: dict):
    try:
        transaction_data = pd.DataFrame([transaction])

        # Feature engineering (same as training)
        transaction_data['balanceChangeOrig'] = transaction_data['newbalanceOrig'] - transaction_data['oldbalanceOrg']
        transaction_data['balanceChangeDest'] = transaction_data['newbalanceDest'] - transaction_data['oldbalanceDest']
        transaction_data['transactionRatio'] = transaction_data['amount'] / (transaction_data['oldbalanceOrg'] + 1)

        # One-hot encode 'type'
        if 'type' in transaction_data.columns:
            dummies = pd.get_dummies(transaction_data['type'], prefix='type')
            transaction_data = pd.concat([transaction_data, dummies], axis=1)
            transaction_data.drop(columns=['type'], inplace=True)

        # Add missing features
        missing_features = list(set(selected_features) - set(transaction_data.columns))
        for feat in missing_features:
            transaction_data[feat] = 0

        # Arrange order
        input_df = transaction_data[selected_features]
        input_scaled = scaler_cc.transform(input_df)

        prediction = rf_model.predict(input_scaled)[0]
        probability = rf_model.predict_proba(input_scaled)[0][1]

        return {"model": "CreditCard", "prediction": int(prediction), "probability": float(probability)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"CreditCard prediction error: {str(e)}")


# ----- ONLINE FRAUD PREDICTION -----
@app.post("/predict/online/")
def predict_online(transaction: dict):
    try:
        transaction_data = pd.DataFrame([transaction])

        # Feature engineering
        transaction_data['amount_log'] = np.log1p(transaction_data['amount'])
        transaction_data['amount_to_oldbalance'] = transaction_data['amount'] / (transaction_data['oldbalanceOrg'] + 1)
        transaction_data['amount_to_newbalance'] = transaction_data['amount'] / (transaction_data['newbalanceOrig'] + 1)
        transaction_data['balance_change_org'] = transaction_data['oldbalanceOrg'] - transaction_data['newbalanceOrig']
        transaction_data['balance_change_dest'] = transaction_data['newbalanceDest'] - transaction_data['oldbalanceDest']

        # One-hot encode 'type'
        if 'type' in transaction_data.columns:
            dummies = pd.get_dummies(transaction_data['type'], prefix='type')
            transaction_data = pd.concat([transaction_data, dummies], axis=1)
            transaction_data.drop(columns=['type'], inplace=True)

        # Add missing features
        missing_features = list(set(important_features) - set(transaction_data.columns))
        for feat in missing_features:
            transaction_data[feat] = 0

        # Arrange order
        input_features = transaction_data[important_features]
        input_scaled = scaler_online.transform(input_features)

        prediction = online_model.predict(input_scaled)[0]
        probability = online_model.predict_proba(input_scaled)[0][1]

        return {"model": "OnlineFraud", "prediction": int(prediction), "probability": float(probability)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OnlineFraud prediction error: {str(e)}")


try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    important_features = joblib.load(features_path)
except Exception as e:
    raise RuntimeError(f"Failed to load artifacts: {e}")

@app.get("/")
def root():
    return {"message": "Welcome to Fraud Detection API"}

@app.post("/predict/")
def predict(transaction: dict):
    try:
        transaction_data = pd.DataFrame([transaction])

        # Feature engineering
        transaction_data['amount_log'] = np.log1p(transaction_data['amount'])
        transaction_data['amount_to_oldbalance'] = transaction_data['amount'] / (transaction_data['oldbalanceOrg'] + 1)
        transaction_data['amount_to_newbalance'] = transaction_data['amount'] / (transaction_data['newbalanceOrig'] + 1)
        transaction_data['balance_change_org'] = transaction_data['oldbalanceOrg'] - transaction_data['newbalanceOrig']
        transaction_data['balance_change_dest'] = transaction_data['newbalanceDest'] - transaction_data['oldbalanceDest']

        # One-hot encode 'type'
        if 'type' in transaction_data.columns:
            dummies = pd.get_dummies(transaction_data['type'], prefix='type')
            transaction_data = pd.concat([transaction_data, dummies], axis=1)
            transaction_data.drop(columns=['type'], inplace=True)

        # Ensure all important features exist
        missing_features = list(set(important_features) - set(transaction_data.columns))
        for feat in missing_features:
            transaction_data[feat] = 0

        # Arrange features in correct order
        input_features = transaction_data[important_features]
        input_scaled = scaler.transform(input_features)

        # Predict
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        return {"prediction": int(prediction), "probability": float(probability)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during prediction: {str(e)}")