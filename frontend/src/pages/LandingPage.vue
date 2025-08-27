<template>
  <div class="min-h-screen text-gray-900">
    <!-- Navbar -->
    <nav class="sticky top-0 left-0 w-full z-50 shadow-md bg-white bg-opacity-90 backdrop-blur-md">
      <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <!-- Brand -->
        <div
          class="text-2xl font-extrabold tracking-wide hover:scale-105 transition-transform duration-300"
          style="color: #3c61e2;"
        >
          Quantum Supernovas
        </div>

        <!-- Links -->
        <div class="flex items-center space-x-8">
          <a href="#home" class="nav-link">Home</a>
          <a href="#about" class="nav-link">About</a>
          <a href="#features" class="nav-link">Features</a>
          <a href="#frauds" class="nav-link">Frauds</a>
          <a href="#how" class="nav-link">How It Works</a>
          <a href="#demo" class="nav-link">Demo</a>
          <a href="#tech" class="nav-link">Tech</a>
          <!-- Login Button -->
          <a
            href="/login"
            class="px-4 py-2 rounded-full font-semibold bg-[#38bdf8] text-black hover:bg-[#0ea5e9] transition shadow-lg"
          >
            Login
          </a>
        </div>
      </div>
    </nav>

    <!-- Hero Section with Slideshow -->
    <header
      id="home"
      class="h-screen flex flex-col justify-center items-center text-center px-6 relative overflow-hidden bg-center bg-cover"
    >
      <!-- Slideshow Background -->
      <div class="absolute inset-0 w-full h-full z-0">
        <div
          v-for="(image, index) in images"
          :key="index"
          :class="[
            'absolute inset-0 w-full h-full bg-center bg-cover transition-all duration-1000 ease-in-out',
            currentImage === index ? 'opacity-100' : 'opacity-0'
          ]"
          :style="{ backgroundImage: `url(${image})` }"
        ></div>
        <!-- Dark overlay for readability -->
        <div
          class="absolute inset-0 bg-black/50 backdrop-blur-sm z-10"
        ></div>
      </div>

      <!-- Hero Content -->
      <div class="relative z-20 animate-fadeIn max-w-3xl">
        <h1
          class="text-5xl md:text-6xl font-extrabold text-white mb-4 drop-shadow-2xl"
        >
          Smarter, Faster, and Safer Transactions with Quantum ML
        </h1>
        <p class="text-lg md:text-xl text-white/90 mb-6 drop-shadow-lg">
          Traditional fraud detection methods struggle with today’s complex transactions. 
          Our Quantum ML framework analyzes vast amounts of data in real-time, 
          detecting anomalies and patterns that others miss.
        </p>
        <div class="flex justify-center">
          <a
            href="#demo"
            class="bg-[#38bdf8] text-black px-8 py-3 rounded-full font-semibold shadow-md hover:bg-[#0ea5e9] transition transform hover:scale-110"
          >
            Try It Now
          </a>
        </div>
      </div>

      <!-- Slideshow indicators -->
      <div
        class="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex space-x-2 z-20"
      >
        <button
          v-for="(_, index) in images"
          :key="index"
          @click="currentImage = index"
          :class="[
            'w-3 h-3 rounded-full transition-all duration-300',
            currentImage === index ? 'bg-[#38bdf8]' : 'bg-white/50'
          ]"
        ></button>
      </div>
    </header>

    <!-- About -->
    <section id="about" class="py-20 px-6 bg-white animate-slideUp">
      <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-4xl font-bold text-[#38bdf8] mb-6">About the Project</h2>
        <p class="text-lg text-gray-700 leading-relaxed">
          Our Fraud Detection system uses machine learning models to identify suspicious activities in 
          transactions. By analyzing historical and live data, it predicts fraud before it happens, ensuring 
          safer and more secure operations for businesses and individuals.
        </p>
      </div>
    </section>

    <!-- Features -->
    <section id="features" class="py-20 px-6 bg-gray-50 animate-fadeIn">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-4xl font-bold text-center text-[#38bdf8] mb-12">Key Features</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="p-6 bg-white shadow rounded-2xl hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">Real-Time Detection</h3>
            <p>Instantly flags potentially fraudulent transactions for quick action.</p>
          </div>
          <div class="p-6 bg-white shadow rounded-2xl hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">High Accuracy</h3>
            <p>Trained ML models minimize false positives and maximize detection rates.</p>
          </div>
          <div class="p-6 bg-white shadow rounded-2xl hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">Data-Driven Insights</h3>
            <p>Provides actionable insights to strengthen security strategies.</p>
          </div>
          <div class="p-6 bg-white shadow rounded-2xl hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">Secure & Reliable</h3>
            <p>Ensures privacy and safe handling of sensitive transaction data.</p>
          </div>
          <div class="p-6 bg-white shadow rounded-2xl hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">Easy Integration</h3>
            <p>Seamlessly connects with existing financial and e-commerce systems.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Frauds -->
    <section id="frauds" class="py-20 px-6 bg-white animate-slideUp">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-4xl font-bold text-center text-[#38bdf8] mb-12">Types of Frauds We Detect</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="p-6 shadow rounded-2xl bg-gray-50 hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">Credit Card Fraud</h3>
            <p>Detects suspicious spending patterns, cloned cards, and unauthorized transactions.</p>
          </div>
          <div class="p-6 shadow rounded-2xl bg-gray-50 hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">E-commerce Fraud</h3>
            <p>Identifies fake accounts, false refunds, and fraudulent purchases in online marketplaces.</p>
          </div>
          <div class="p-6 shadow rounded-2xl bg-gray-50 hover:scale-105 transition">
            <h3 class="font-bold text-xl mb-3">Online Payment Fraud</h3>
            <p>Protects digital wallets and UPI transfers by analyzing unusual transaction behavior.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section id="how" class="py-20 px-6 bg-gray-50 animate-fadeIn">
      <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-4xl font-bold text-[#38bdf8] mb-12">How It Works</h2>
        <div class="space-y-6 text-lg">
          <p><span class="font-bold">1. Data Collection:</span> Gather transaction data from systems.</p>
          <p><span class="font-bold">2. Model Analysis:</span> ML models evaluate transactions for suspicious behavior.</p>
          <p><span class="font-bold">3. Fraud Prediction:</span> Each transaction is classified as safe or risky.</p>
          <p><span class="font-bold">4. Action & Reporting:</span> Alerts and reports generated in real-time.</p>
        </div>
      </div>
    </section>

    <!-- Demo -->
    <section id="demo" class="py-20 px-6 bg-white animate-slideUp">
      <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-4xl font-bold text-[#38bdf8] mb-6">Try Our Demo</h2>
        <p class="mb-6 text-lg text-gray-700">Enter a sample transaction and test how our model predicts fraud in real-time.</p>
        <a
          href="/login"
          class="px-8 py-3 rounded-full font-semibold bg-[#38bdf8] text-black hover:bg-[#0ea5e9] transition shadow-lg"
        >
          Check Transaction
        </a>
      </div>
    </section>

    <!-- Tech -->
    <section id="tech" class="py-20 px-6 bg-gray-50 animate-fadeIn">
      <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-4xl font-bold text-[#38bdf8] mb-6">Technology & Model Used</h2>
        <p class="text-lg text-gray-700 leading-relaxed">
          Our system is powered by Python, Scikit-Learn, Pandas, and Flask for the backend, 
          with Vue.js and TailwindCSS for a modern and responsive frontend. 
          Trained on historical datasets, the ML model ensures accurate and reliable predictions.
        </p>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-10 bg-gray-900 text-gray-300 text-center">
      <div class="mb-4">
        <a href="#home" class="mx-2 hover:text-white">Home</a>
        <a href="#about" class="mx-2 hover:text-white">About</a>
        <a href="#features" class="mx-2 hover:text-white">Features</a>
        <a href="#demo" class="mx-2 hover:text-white">Demo</a>
        <a href="#tech" class="mx-2 hover:text-white">Tech</a>
      </div>
      <p>© 2025 Fraud Detection ML Project by Quantum Supernovas</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import aImg from "../assets/a.jpg";
import bImg from "../assets/b.jpg";
import cImg from "../assets/c.jpg";

const images = [aImg, bImg, cImg];
const currentImage = ref(0);
let slideInterval;

onMounted(() => {
  slideInterval = setInterval(() => {
    currentImage.value = (currentImage.value + 1) % images.length;
  }, 5000);
});

onUnmounted(() => {
  if (slideInterval) clearInterval(slideInterval);
});
</script>

<style scoped>
.nav-link {
  color: #38bdf8;
  font-weight: 600;
  transition: all 0.3s;
  position: relative;
}
.nav-link::after {
  content: "";
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -5px;
  left: 0;
  background: #38bdf8;
  transition: width 0.3s;
}
.nav-link:hover {
  color: #0ea5e9;
  transform: translateY(-2px);
}
.nav-link:hover::after {
  width: 100%;
}

/* Animations */
@keyframes fadeDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeDown { animation: fadeDown 1s ease-in-out; }
.animate-fadeIn { animation: fadeIn 1.5s ease-in-out; }
.animate-slideUp { animation: slideUp 1.5s ease-in-out; }
</style>

