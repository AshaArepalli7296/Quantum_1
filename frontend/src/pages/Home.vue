<template>
  <div class="home-container">
    <!-- Navbar -->
    <Navbar />

    <!-- Hero Section -->
    <section id="hero" class="hero">
      <div class="hero-content">
        <h1 class="title">Quantum ML Fraud Detection</h1>
        <p class="subtitle">Smarter Fraud Prevention with Quantum Computing</p>
        <!-- Use router-link instead of plain button -->
        <a href="#fraud" class="explore-btn">
          Explore Models ↓
        </a>
      </div>
    </section>

    <!-- Fraud Section -->
    <section id="fraud" class="fraud-section">
  <h2 class="section-title">Fraud Detection Models</h2>
  <div class="fraud-grid">
    <router-link to="/frauds/credit" class="fraud-card">
      <h3>💳 Credit Card Fraud</h3>
      <p>Detect anomalies in credit card transactions using Quantum ML pipelines.</p>
    </router-link>

    <router-link to="/frauds/ecommerce" class="fraud-card">
      <h3>🛒 E-commerce Fraud</h3>
      <p>Identify fraudulent behaviors in online shopping and marketplace transactions.</p>
    </router-link>

    <router-link to="/frauds/payment" class="fraud-card">
      <h3>💻 Online Payment Fraud</h3>
      <p>Monitor suspicious activities in online payments with advanced anomaly detection.</p>
    </router-link>
  </div>
</section>


    <!-- Dashboard Section -->
    <section id="dashboard" class="dashboard">
      <div class="dashboard-content">
        <h2>📊 Dashboard</h2>
        <p>
          Explore real-time insights into transaction data anomalies with
          Quantum ML-driven dashboards.
        </p>
        <div class="dashboard-box">
          <h3>Live Analytics</h3>
          <p>Interactive futuristic visualizations coming soon...</p>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
import Navbar from "../components/Navbar.vue";

export default {
  name: "Home",
  components: { Navbar },
};
</script>

<style scoped>
.home-container {
  width: 100vw;           /* force exact viewport width */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 2rem;

  /* transparent so background shows from body */
  background: transparent;  
}


/* Hero Section */
.hero {
  width: 100%;
  height: 100vh;
  background: linear-gradient(135deg, #7494ec, #3c63d0);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.title {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #fff;
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
}

.subtitle {
  font-size: 1.5rem;
  opacity: 0.9;
  color: #f1f1f1;
}

.explore-btn {
  display: inline-block;
  margin-top: 2rem;
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 25px;
  background: #fff;
  color: #3c63d0;
  font-weight: bold;
  cursor: pointer;
  text-decoration: none; /* so it doesn’t look like a link */
  transition: 0.3s ease;
}

.explore-btn:hover {
  background: #00f6ff;
  color: #ffffff;
}

/* Fraud Section */
/* Fraud Section */
.fraud-section {
  width: 100%;
  min-height: 100vh;   /* 🔹 Makes this section full screen height */
  background: #f5f7ff;
  color: #333;
  display: flex;
  flex-direction: column;
  justify-content: center;  /* centers grid vertically */
  align-items: center;
  padding: 4rem 2rem;
  margin: 0;
  box-sizing: border-box;
}


.fraud-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #2a2f60;
}

.fraud-grid {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
}

.fraud-card {
  background: #ffffff;
  border-radius: 16px;
  padding: 2rem;
  width: 280px;
  text-align: center;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.fraud-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
}

/* Dashboard Section */
.dashboard {
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a40, #0d0d1a);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4rem 2rem;
  margin: 0;
  box-sizing: border-box;
}

.dashboard-content {
  text-align: center;
  max-width: 800px;
}

.dashboard-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #00f6ff;
}

.dashboard-content p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  color: #ddd;
}

.dashboard-box {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 2rem;
  color: #fff;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(12px);
}
</style>