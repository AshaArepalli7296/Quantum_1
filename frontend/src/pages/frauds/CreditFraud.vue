<template>
  <div class="fraud-container">
    <h1>💳 Credit Card Fraud Detection</h1>

    <!-- Form Card -->
    <div class="card">
      <form @submit.prevent="predictFraud" class="form-box">
        <div class="form-group">
          <label>Transaction Step:</label>
          <input v-model.number="transaction.step" type="number" required />
        </div>

        <div class="form-group">
          <label>Amount:</label>
          <input v-model.number="transaction.amount" type="number" required />
        </div>

        <div class="form-group">
          <label>Old Balance Origin:</label>
          <input v-model.number="transaction.oldbalanceOrg" type="number" required />
        </div>

        <div class="form-group">
          <label>New Balance Origin:</label>
          <input v-model.number="transaction.newbalanceOrig" type="number" required />
        </div>

        <div class="form-group">
          <label>Old Balance Destination:</label>
          <input v-model.number="transaction.oldbalanceDest" type="number" required />
        </div>

        <div class="form-group">
          <label>New Balance Destination:</label>
          <input v-model.number="transaction.newbalanceDest" type="number" required />
        </div>

        <div class="form-group">
          <label>Transaction Type:</label>
          <select v-model="transaction.type">
            <option value="TRANSFER">TRANSFER</option>
            <option value="CASH_OUT">CASH_OUT</option>
            <option value="PAYMENT">PAYMENT</option>
            <option value="DEBIT">DEBIT</option>
          </select>
        </div>

        <button type="submit" class="btn">🔍 Predict</button>
      </form>
    </div>

    <!-- Result Card -->
    <div
      v-if="result"
      class="card result-box"
      :class="result.prediction === 1 ? 'fraud' : 'legit'"
    >
      <h2>
        {{ result.prediction === 1 ? "🚨 Fraud Detected!" : "✅ Legit Transaction" }}
      </h2>
      <p>Probability: {{ (result.probability * 100).toFixed(2) }}%</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import axios from "axios"

const transaction = ref({
  step: 0,
  amount: 0,
  oldbalanceOrg: 0,
  newbalanceOrig: 0,
  oldbalanceDest: 0,
  newbalanceDest: 0,
  type: "TRANSFER"
})

const result = ref(null)

const predictFraud = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/predict/creditcard/",
      transaction.value
    )
    result.value = response.data
  } catch (error) {
    console.error(error)
    result.value = { prediction: -1, probability: 0 }
  }
}
</script>

<style scoped>
/* Container */
.fraud-container {
  max-width: 600px;
  margin: 40px auto;
  text-align: center;
  font-family: "Segoe UI", Tahoma, sans-serif;
  color: #2c3e50;
}

/* Heading */
.fraud-container h1 {
  margin-bottom: 25px;
  font-size: 26px;
  color: #34495e;
}

/* Card */
.card {
  background: #ffffff;
  padding: 25px;
  margin-bottom: 20px;
  border-radius: 12px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
}

/* Form Layout */
.form-box {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  text-align: left;
}

label {
  font-weight: 600;
  margin-bottom: 5px;
  display: inline-block;
  color: #34495e;
}

input,
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #dcdde1;
  border-radius: 8px;
  transition: border 0.3s ease;
  font-size: 14px;
}

input:focus,
select:focus {
  border-color: #3498db;
  outline: none;
}

/* Button */
.btn {
  background: linear-gradient(135deg, #3498db, #2980b9);
  color: #fff;
  font-weight: 600;
  padding: 12px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s ease, background 0.3s ease;
}

.btn:hover {
  background: linear-gradient(135deg, #2980b9, #1f6391);
  transform: scale(1.05);
}

/* Result Box */
.result-box {
  padding: 20px;
  font-weight: bold;
  border-radius: 10px;
  transition: 0.3s;
}

.result-box.fraud {
  background: #ffeaea;
  border: 2px solid #e74c3c;
  color: #c0392b;
}

.result-box.legit {
  background: #eaffea;
  border: 2px solid #2ecc71;
  color: #27ae60;
}
</style>
 