<template>
  <div class="app">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="nav-container">
        <!-- Brand -->
        <div class="brand">Quantum Supernovas</div>
        <!-- Links -->
        <div class="nav-links">
          <a href="#" class="nav-link">Home</a>
          <a href="#about" class="nav-link">About</a>
          <a href="#models" class="nav-link">Models</a>
          <a href="#dashboard" class="nav-link">Dashboard</a>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero">
      <!-- Slideshow Background -->
      <div class="slideshow">
        <div
          v-for="(image, i) in images"
          :key="i"
          :class="['slide', currentImage === i ? 'active' : '']"
          :style="{ backgroundImage: `url(${image})` }"
        ></div>
        <div class="overlay"></div>
      </div>

      <!-- Hero Content -->
      <div class="hero-content">
        <h1>Quantum ML Fraud Detection</h1>
        <p>Smarter Fraud Prevention with Quantum Computing</p>
        <a href="#about" class="cta-btn">Learn More ↓</a>
      </div>

      <!-- Slideshow Indicators -->
      <div class="indicators">
        <button
          v-for="(image, i) in images"
          :key="i"
          @click="setCurrentImage(i)"
          :class="['dot', currentImage === i ? 'active' : '']"
        ></button>
      </div>
    </header>

    <!-- Title Cards Section -->
    <section class="cards-section">
      <div class="card card-enhanced">
        <h3 class="card-title">Accuracy</h3>
        <p class="card-text">Quantum models deliver higher fraud detection accuracy with 99.8% precision.</p>
      </div>
      <div class="card card-enhanced">
        <h3 class="card-title">Speed</h3>
        <p class="card-text">Transactions analyzed in real time with quantum efficiency under 10ms.</p>
      </div>
      <div class="card card-enhanced">
        <h3 class="card-title">Security</h3>
        <p class="card-text">Enhanced protection with quantum-powered anomaly detection systems.</p>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
      <h2>About Our Project</h2>
      <p>
        Our system leverages <span class="highlight">Quantum Machine Learning</span>
        to detect fraud patterns faster and more accurately. By combining cutting-edge algorithms
        with quantum computing, we ensure financial safety and smarter detection.
      </p>
    </section>

    <!-- Fraud Models -->
    <!-- Fraud Section -->
<section id="fraud" class="fraud-section">
  <h2 class="section-title">Fraud Detection Models</h2>
  <div class="fraud-grid">
    <router-link to="/frauds/credit" class="fraud-card">
      <h3 class="card-title">💳 Credit Card Fraud</h3>
      <p class="card-text">
        Detect anomalies in credit card transactions using advanced Quantum ML pipelines with real-time monitoring.
      </p>
    </router-link>

    <router-link to="/frauds/ecommerce" class="fraud-card">
      <h3 class="card-title">🛒 E-commerce Fraud</h3>
      <p class="card-text">
        Identify fraudulent behaviors and anomalies in online shopping transactions with behavioral analysis.
      </p>
    </router-link>

    <router-link to="/frauds/payment" class="fraud-card">
      <h3 class="card-title">💻 Online Payment Fraud</h3>
      <p class="card-text">
        Monitor suspicious activities in online payments with machine learning pattern recognition.
      </p>
    </router-link>
  </div>
</section>


    <!-- Models Section -->
    <section id="models" class="models">
      <h2>Our Fraud Detection Models</h2>
      <div class="model-grid">
        <div class="model-card">
          <h3 class="card-title">Quantum SVM</h3>
          <p class="card-text">Fast classification of fraudulent transactions using quantum kernels and support vector machines.</p>
          <div class="model-features">
            <span class="feature-tag">Quantum Kernels</span>
            <span class="feature-tag">Fast Processing</span>
          </div>
        </div>
        <div class="model-card">
          <h3 class="card-title">Quantum Neural Net</h3>
          <p class="card-text">Deep learning powered by quantum computing for advanced fraud pattern recognition and detection.</p>
          <div class="model-features">
            <span class="feature-tag">Deep Learning</span>
            <span class="feature-tag">Pattern Recognition</span>
          </div>
        </div>
        <div class="model-card">
          <h3 class="card-title">Hybrid QML</h3>
          <p class="card-text">Combines classical ML with quantum models for maximum accuracy and optimal performance results.</p>
          <div class="model-features">
            <span class="feature-tag">Hybrid Architecture</span>
            <span class="feature-tag">Max Accuracy</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Dashboard CTA -->
    <section id="dashboard" class="dashboard">
      <h2>Try Our Dashboard</h2>
      <p>Interactive fraud detection dashboard with real-time insights.</p>
      <a href="#" class="dashboard-btn">Go to Dashboard →</a>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <p>© 2025 Quantum Supernovas | Built for Hackathon</p>
    </footer>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'QuantumSupernovas',
  setup() {
    const images = [
      "https://images.unsplash.com/photo-1556075798-4825dfaaf498?w=1920&h=1080&fit=crop",
      "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920&h=1080&fit=crop",
      "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920&h=1080&fit=crop"
    ]

    const currentImage = ref(0)
    let slideInterval = null

    const setCurrentImage = (index) => {
      currentImage.value = index
    }

    onMounted(() => {
      slideInterval = setInterval(() => {
        currentImage.value = (currentImage.value + 1) % images.length
      }, 5000)
    })

    onUnmounted(() => {
      if (slideInterval) clearInterval(slideInterval)
    })

    return { images, currentImage, setCurrentImage }
  }
}
</script>

<style>
body {
  font-family: 'Inter', sans-serif;
  margin: 0;
  padding: 0;
}
.app { background: #f8fafc; min-height: 100vh; }

/* Navbar */
.navbar {
  position: fixed; top: 0; left: 0; width: 100%;
  background: rgba(255,255,255,0.9); backdrop-filter: blur(10px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1); z-index: 50;
}
.nav-container {
  max-width: 1200px; margin: 0 auto;
  display: flex; justify-content: space-between; align-items: center;
  padding: 1rem 2rem;
}
.brand { font-size: 1.5rem; font-weight: 800; color: #2563eb; }

/* Nav links */
.nav-links { display: flex; gap: 2rem; }
.nav-link { color: #2563eb; font-weight: 600; text-decoration: none; position: relative; }
.nav-link:hover { color: #1e40af; }
.nav-link::after {
  content: ''; position: absolute; bottom: -4px; left: 0; height: 2px; width: 0;
  background: #2563eb; transition: width 0.3s;
}
.nav-link:hover::after { width: 100%; }

/* Hero */
.hero { height: 100vh; display: flex; justify-content: center; align-items: center; text-align: center; position: relative; }
.slideshow { position: absolute; inset: 0; overflow: hidden; }
.slide { position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: opacity 1s ease-in-out; }
.slide.active { opacity: 1; }
.overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.4); }
.hero-content { position: relative; z-index: 10; color: white; }
.hero-content h1 { font-size: 3rem; margin-bottom: 1rem; }
.cta-btn {
  display: inline-block; margin-top: 1rem;
  background: white; color: #2563eb; padding: 0.75rem 1.5rem;
  border-radius: 2rem; font-weight: 600; text-decoration: none;
  transition: 0.3s;
}
.cta-btn:hover { background: #2563eb; color: white; transform: scale(1.05); }
.indicators { position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); display: flex; gap: 0.5rem; }
.dot { width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.5); border: none; cursor: pointer; }
.dot.active { background: white; }

/* Cards */
.cards-section { max-width: 1000px; margin: -3rem auto 2rem; display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.card-enhanced {
  background: white; padding: 2rem; border-radius: 1rem; text-align: center;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1); transition: 0.3s;
}
.card-enhanced:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.2); }

/* About */
.about { max-width: 900px; margin: 3rem auto; text-align: center; padding: 2rem; }
.about h2 { font-size: 2rem; margin-bottom: 1rem; color: #1e293b; }
.about p { color: #555; line-height: 1.6; }
.highlight { color: #2563eb; font-weight: 600; }

/* Fraud */
.fraud-section { padding: 3rem 1rem; text-align: center; }
.fraud-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; max-width: 1000px; margin: 0 auto; }
.fraud-card {
  background: linear-gradient(145deg, #ffffff, #f8fafc); padding: 2rem; border-radius: 1rem;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1); transition: 0.3s;
}
.fraud-card:hover { transform: translateY(-8px) scale(1.02); }

/* Models */
.models { background: white; padding: 3rem 1rem; text-align: center; }
.model-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; max-width: 1000px; margin: 0 auto; }
.model-card {
  background: white; padding: 2rem; border-radius: 1rem;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1); transition: 0.3s;
}
.model-card:hover { transform: translateY(-8px); }
.model-features { display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap; margin-top: 1rem; }
.feature-tag { background: rgba(37,99,235,0.1); color: #2563eb; padding: 0.3rem 0.8rem; border-radius: 1rem; font-size: 0.85rem; }

/* Dashboard */
.dashboard { padding: 3rem 1rem; text-align: center; }
.dashboard-btn {
  display: inline-block; margin-top: 1rem; background: #1e293b; color: white; padding: 0.75rem 1.5rem;
  border-radius: 2rem; font-weight: 600; text-decoration: none; transition: 0.3s;
}
.dashboard-btn:hover { background: #2563eb; }

/* Footer */
.footer { background: #1e293b; color: white; padding: 1rem; text-align: center; margin-top: 2rem; }
</style>
