<template>
  <div class="bg-[#f8fafc] min-h-screen">
    <!-- Navbar -->
    <nav class="fixed top-0 left-0 w-full backdrop-blur-md bg-white/80 shadow-md z-50 animate-fadeDown">
      <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <!-- Brand -->
        <div class="text-2xl font-extrabold text-[#2563eb] tracking-wide hover:scale-105 transition-transform duration-300">
          Quantum Supernovas
        </div>
        <!-- Links -->
        <div class="space-x-8">
          <a href="#" class="nav-link">Home</a>
          <a href="#about" class="nav-link">About</a>
          <a href="#models" class="nav-link">Models</a>
          <a href="#dashboard" class="nav-link">Dashboard</a>
        </div>
      </div>
    </nav>

    <!-- Hero Section with Slideshow -->
    <header class="h-screen flex flex-col justify-center items-center text-center px-6 relative overflow-hidden bg-center bg-cover">
      <!-- Slideshow Background -->
      <div class="absolute inset-0 w-full h-full z-0">
        <div
          v-for="(image, i) in images"
          :key="i"
          :class="[
            'absolute inset-0 w-full h-full object-cover transition-all duration-1000 ease-in-out',
            currentImage === i ? 'opacity-100' : 'opacity-0'
          ]"
          :style="{
            backgroundImage: `url(${image})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center'
          }"
        ></div>
        <!-- Semi-transparent overlay for better text readability -->
        <div class="absolute inset-0 bg-black/40 z-10"></div>
      </div>
      <!-- Hero Content -->
      <div class="relative z-20 animate-fadeIn">
        <h1 class="text-5xl md:text-6xl font-extrabold text-white mb-4 drop-shadow-lg">
          Quantum ML Fraud Detection
        </h1>
        <p class="text-lg md:text-xl text-white/90 mb-6 max-w-2xl">
          Smarter Fraud Prevention with Quantum Computing
        </p>
        <a
          href="#about"
          class="bg-white text-[#2563eb] px-6 py-3 rounded-full font-semibold shadow-md hover:bg-[#2563eb] hover:text-white transition transform hover:scale-110 inline-block animate-bounce-slow"
        >
          Learn More ↓
        </a>
      </div>
      <!-- Slideshow indicators -->
      <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex space-x-2 z-20">
        <button
          v-for="(image, i) in images"
          :key="i"
          @click="setCurrentImage(i)"
          :class="[
            'w-3 h-3 rounded-full transition-all duration-300',
            currentImage === i ? 'bg-white' : 'bg-white/50'
          ]"
        ></button>
      </div>
    </header>

    <!-- Title Cards Section -->
    <section class="max-w-6xl mx-auto px-6 -mt-12 relative z-10">
      <div class="grid md:grid-cols-3 gap-4">
        <div class="card-enhanced animate-on-scroll" data-animation="slideInLeft">
          <h3 class="card-title">Accuracy</h3>
          <p class="card-text">Quantum models deliver higher fraud detection accuracy with 99.8% precision.</p>
        </div>
        <div class="card-enhanced animate-on-scroll animation-delay-200" data-animation="slideInUp">
          <h3 class="card-title">Speed</h3>
          <p class="card-text">Transactions analyzed in real time with quantum efficiency under 10ms.</p>
        </div>
        <div class="card-enhanced animate-on-scroll animation-delay-400" data-animation="slideInRight">
          <h3 class="card-title">Security</h3>
          <p class="card-text">Enhanced protection with quantum-powered anomaly detection systems.</p>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="max-w-6xl mx-auto px-6 py-6 text-center animate-on-scroll" data-animation="fadeInUp">
      <h2 class="text-3xl font-bold text-[#1e293b] mb-4">About Our Project</h2>
      <p class="text-lg text-gray-600 max-w-3xl mx-auto">
        Our system leverages <span class="font-semibold text-[#2563eb]">Quantum Machine Learning</span> to detect fraud patterns faster and more accurately. By combining cutting-edge algorithms with quantum computing, we ensure financial safety and smarter detection.
      </p>
    </section>

    <!-- Fraud Models -->
    <section id="fraud" class="flex flex-col items-center justify-center bg-[#f8fafc] px-6 py-4">
      <h2 class="text-4xl md:text-5xl font-bold mb-6 text-[#1e293b] animate-on-scroll" data-animation="fadeInUp">
        Fraud Detection Models
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-6xl w-full">
        <div class="fraud-card animate-on-scroll" data-animation="rotateInLeft">
          <h3 class="card-title">Credit Card Fraud</h3>
          <p class="card-text">Detect anomalies in credit card transactions using advanced Quantum ML pipelines with real-time monitoring.</p>
        </div>
        <div class="fraud-card animate-on-scroll animation-delay-200" data-animation="rotateInUp">
          <h3 class="card-title">E-commerce Fraud</h3>
          <p class="card-text">Identify fraudulent behaviors and anomalies in online shopping transactions with behavioral analysis.</p>
        </div>
        <div class="fraud-card animate-on-scroll animation-delay-400" data-animation="rotateInRight">
          <h3 class="card-title">Online Payment Fraud</h3>
          <p class="card-text">Monitor suspicious activities in online payments with machine learning pattern recognition.</p>
        </div>
      </div>
    </section>

    <!-- Models Section -->
    <section id="models" class="bg-white py-8">
      <div class="max-w-6xl mx-auto px-6 text-center">
        <h2 class="text-3xl font-bold text-[#1e293b] mb-6 animate-on-scroll" data-animation="fadeInUp">
          Our Fraud Detection Models
        </h2>
        <div class="grid md:grid-cols-3 gap-4">
          <div class="model-card animate-on-scroll" data-animation="flipInY">
            <h3 class="card-title">Quantum SVM</h3>
            <p class="card-text">Fast classification of fraudulent transactions using quantum kernels and support vector machines.</p>
            <div class="model-features">
              <span class="feature-tag">Quantum Kernels</span>
              <span class="feature-tag">Fast Processing</span>
            </div>
          </div>
          <div class="model-card animate-on-scroll animation-delay-200" data-animation="flipInY">
            <h3 class="card-title">Quantum Neural Net</h3>
            <p class="card-text">Deep learning powered by quantum computing for advanced fraud pattern recognition and detection.</p>
            <div class="model-features">
              <span class="feature-tag">Deep Learning</span>
              <span class="feature-tag">Pattern Recognition</span>
            </div>
          </div>
          <div class="model-card animate-on-scroll animation-delay-400" data-animation="flipInY">
            <h3 class="card-title">Hybrid QML</h3>
            <p class="card-text">Combines classical ML with quantum models for maximum accuracy and optimal performance results.</p>
            <div class="model-features">
              <span class="feature-tag">Hybrid Architecture</span>
              <span class="feature-tag">Max Accuracy</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Dashboard CTA -->
    <section id="dashboard" class="py-8 text-center animate-on-scroll" style="background:#ffffff;" data-animation="fadeInUp">
      <h2 class="text-3xl font-bold text-[#1e293b] mb-3">Try Our Dashboard</h2>
      <p class="text-lg text-[#4b5563] mb-4">Interactive fraud detection dashboard with real-time insights.</p>
      <a
        href="#"
        class="bg-[#1e293b] text-white px-6 py-3 rounded-full font-semibold shadow-md hover:bg-[#2563eb] hover:text-white transition transform hover:scale-110 pulse-animation"
      >
        Go to Dashboard →
      </a>
    </section>

    <!-- Footer -->
    <footer class="bg-[#1e293b] text-white py-4 text-center animate-on-scroll" data-animation="fadeInUp">
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
      "https://images.unsplash.com/photo-1556075798-4825dfaaf498?w=1920&h=1080&fit=crop", // Dark abstract tech
      "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920&h=1080&fit=crop", // Blue tech circuit
      "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920&h=1080&fit=crop" // Dark quantum computer
    ]

    const currentImage = ref(0)
    let slideInterval = null

    const setCurrentImage = (index) => {
      currentImage.value = index
    }

    const initScrollAnimations = () => {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const animation = entry.target.getAttribute('data-animation') || 'fadeInUp'
              entry.target.classList.add('animate-' + animation)
              observer.unobserve(entry.target)
            }
          })
        },
        { threshold: 0.1 }
      )
      
      document.querySelectorAll('.animate-on-scroll').forEach((el) => {
        observer.observe(el)
      })
    }

    onMounted(() => {
      slideInterval = setInterval(() => {
        currentImage.value = (currentImage.value + 1) % images.length
      }, 5000)

      initScrollAnimations()
    })

    onUnmounted(() => {
      if (slideInterval) {
        clearInterval(slideInterval)
      }
    })

    return {
      images,
      currentImage,
      setCurrentImage
    }
  }
}
</script>

<style>
body { 
  font-family: 'Inter', sans-serif; 
}

/* Base animations */
@keyframes fadeIn { 
  from { opacity: 0; } 
  to { opacity: 1; } 
}

/* Utility animation class */
.animate-fadeIn { 
  animation: fadeIn 1.2s ease forwards; 
}

@keyframes slideInUp { 
  from { opacity: 0; transform: translateY(30px); } 
  to { opacity: 1; transform: translateY(0); } 
}

@keyframes slideInLeft { 
  from { opacity: 0; transform: translateX(-30px); } 
  to { opacity: 1; transform: translateX(0); } 
}

@keyframes slideInRight { 
  from { opacity: 0; transform: translateX(30px); } 
  to { opacity: 1; transform: translateX(0); } 
}

@keyframes fadeInUp { 
  from { opacity: 0; transform: translateY(20px); } 
  to { opacity: 1; transform: translateY(0); } 
}

@keyframes rotateInLeft { 
  from { opacity: 0; transform: rotate(-15deg) translateX(-50px); } 
  to { opacity: 1; transform: rotate(0deg) translateX(0); } 
}

@keyframes rotateInRight { 
  from { opacity: 0; transform: rotate(15deg) translateX(50px); } 
  to { opacity: 1; transform: rotate(0deg) translateX(0); } 
}

@keyframes rotateInUp { 
  from { opacity: 0; transform: rotate(-15deg) translateY(50px); } 
  to { opacity: 1; transform: rotate(0deg) translateY(0); } 
}

@keyframes flipInY { 
  from { opacity: 0; transform: perspective(400px) rotateY(20deg); } 
  to { opacity: 1; transform: perspective(400px) rotateY(0deg); } 
}

@keyframes bounceSlow { 
  0%, 100% { transform: translateY(0); } 
  50% { transform: translateY(-8px); } 
}

@keyframes pulse { 
  0%, 100% { transform: scale(1); } 
  50% { transform: scale(1.05); } 
}

/* Animation classes */
.animate-slideInUp { 
  animation: slideInUp 0.8s ease forwards; 
}

.animate-slideInLeft { 
  animation: slideInLeft 0.8s ease forwards; 
}

.animate-slideInRight { 
  animation: slideInRight 0.8s ease forwards; 
}

.animate-fadeInUp { 
  animation: fadeInUp 0.8s ease forwards; 
}

.animate-rotateInLeft { 
  animation: rotateInLeft 0.8s ease forwards; 
}

.animate-rotateInRight { 
  animation: rotateInRight 0.8s ease forwards; 
}

.animate-rotateInUp { 
  animation: rotateInUp 0.8s ease forwards; 
}

.animate-flipInY { 
  animation: flipInY 0.8s ease forwards; 
}

.animate-bounce-slow { 
  animation: bounceSlow 2s infinite; 
}

.pulse-animation { 
  animation: pulse 2s infinite; 
}

/* Animation delays */
.animation-delay-200 { 
  animation-delay: 0.2s; 
}

.animation-delay-300 { 
  animation-delay: 0.3s; 
}

.animation-delay-400 { 
  animation-delay: 0.4s; 
}

.animation-delay-600 { 
  animation-delay: 0.6s; 
}

/* Enhanced Cards */
.card-enhanced {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
  opacity: 0;
  transition: all 0.3s ease;
  border: 1px solid rgba(37, 99, 235, 0.1);
}

.card-enhanced:hover { 
  transform: translateY(-5px); 
  box-shadow: 0 15px 35px rgba(37, 99, 235, 0.2); 
}

/* Fraud Cards */
.fraud-card {
  background: linear-gradient(145deg, #ffffff, #f8fafc);
  padding: 2rem;
  border-radius: 1.5rem;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  opacity: 0;
  transition: all 0.4s ease;
  border: 2px solid transparent;
  position: relative;
  overflow: hidden;
}

.fraud-card::before { 
  content: ''; 
  position: absolute; 
  top: 0; 
  left: -100%; 
  width: 100%; 
  height: 2px; 
  background: linear-gradient(90deg, transparent, #2563eb, transparent); 
  transition: left 0.6s ease; 
}

.fraud-card:hover::before { 
  left: 100%; 
}

.fraud-card:hover { 
  transform: translateY(-8px) scale(1.02); 
  border-color: rgba(37, 99, 235, 0.3); 
  box-shadow: 0 20px 40px rgba(37, 99, 235, 0.15); 
}

/* Model Cards */
.model-card {
  background: white;
  padding: 2rem;
  border-radius: 1.5rem;
  text-align: center;
  box-shadow: 0 8px 25px rgba(0,0,0,0.08);
  opacity: 0;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
}

.model-card::after { 
  content: ''; 
  position: absolute; 
  top: -50%; 
  left: -50%; 
  width: 200%; 
  height: 200%; 
  background: radial-gradient(circle, rgba(37, 99, 235, 0.1) 0%, transparent 70%); 
  transform: scale(0); 
  transition: transform 0.6s ease; 
}

.model-card:hover::after { 
  transform: scale(1); 
}

.model-card:hover { 
  transform: translateY(-10px) rotateX(5deg); 
  box-shadow: 0 25px 50px rgba(37, 99, 235, 0.2); 
}

/* Default styles for animation elements */
.animate-on-scroll { 
  opacity: 0; 
}

.card-title { 
  font-size: 1.5rem; 
  font-weight: 700; 
  color: #2563eb; 
  margin-bottom: 0.5rem; 
}

.card-text { 
  color: #4b5563; 
  line-height: 1.6; 
}

.nav-link { 
  color: #2563eb; 
  font-weight: 600; 
  transition: all 0.3s; 
  position: relative; 
}

.nav-link::after { 
  content: ''; 
  position: absolute; 
  width: 0; 
  height: 2px; 
  bottom: -5px; 
  left: 0; 
  background: #2563eb; 
  transition: width 0.3s; 
}

.nav-link:hover { 
  color: #1e40af; 
  transform: translateY(-2px); 
}

.nav-link:hover::after { 
  width: 100%; 
}

.model-features {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.feature-tag {
  background: rgba(37, 99, 235, 0.1);
  color: #2563eb;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
}
</style>
