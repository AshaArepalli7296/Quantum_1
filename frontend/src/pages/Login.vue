<template>
  <div class="container" ref="container">
    <!-- login form -->
    <div class="form-box login">
      <form id="loginForm" @submit.prevent="handleLogin">
        <h1>Login</h1>
        <div class="input-box" :class="{ error: loginErrors.username }">
          <input type="text" v-model.trim="loginData.username" placeholder="Username" required>
          <i class='bx bxs-user'></i>
          <div class="error-message" v-if="loginErrors.username">{{ loginErrors.username }}</div>
        </div>
        <div class="input-box" :class="{ error: loginErrors.password }">
          <input type="password" v-model="loginData.password" placeholder="Password" required>
          <i class='bx bxs-lock-alt'></i>
          <div class="error-message" v-if="loginErrors.password">{{ loginErrors.password }}</div>
        </div>
        <div class="forgot-link">
          <a href="#" @click.prevent="openForgotPassword">Forgot password?</a>
        </div>
        <button type="submit" class="btn">Login</button>
        <p>or login with social platforms</p>
        <div class="social-icons">
          <a href="#"><i class='bx bxl-google'></i></a>
          <a href="#"><i class='bx bxl-facebook'></i></a>
          <a href="#"><i class='bx bxl-github'></i></a>
          <a href="#"><i class='bx bxl-linkedin'></i></a>
        </div>
      </form>
    </div>

    <!-- Registration -->
    <div class="form-box register">
      <form id="registerForm" @submit.prevent="handleRegister">
        <h1>Registration</h1>
        <div class="input-box" :class="{ error: registerErrors.username }">
          <input type="text" v-model.trim="registerData.username" placeholder="Username" required>
          <i class='bx bxs-user'></i>
          <div class="error-message" v-if="registerErrors.username">{{ registerErrors.username }}</div>
        </div>
        <div class="input-box" :class="{ error: registerErrors.email }">
          <input type="email" v-model.trim="registerData.email" placeholder="Email" required>
          <i class='bx bxs-envelope'></i>
          <div class="error-message" v-if="registerErrors.email">{{ registerErrors.email }}</div>
        </div>
        <div class="input-box" :class="{ error: registerErrors.password }">
          <input type="password" v-model="registerData.password" placeholder="Password" required>
          <i class='bx bxs-lock-alt'></i>
          <div class="error-message" v-if="registerErrors.password">{{ registerErrors.password }}</div>
        </div>
        <button type="submit" class="btn">Register</button>
        <p>or Register with social platforms</p>
        <div class="social-icons">
          <a href="#"><i class='bx bxl-google'></i></a>
          <a href="#"><i class='bx bxl-facebook'></i></a>
          <a href="#"><i class='bx bxl-github'></i></a>
          <a href="#"><i class='bx bxl-linkedin'></i></a>
        </div>
      </form>
    </div>

    <!-- Toggle -->
    <div class="toggle-box">
      <div class="toggle-panel toggle-left">
        <h1>Hello, Welcome!</h1>
        <p>Don't have an account?</p>
        <button class="btn register-btn" @click.prevent="showRegister">Register</button>
      </div>
      <div class="toggle-panel toggle-right">
        <h1>Welcome Back!</h1>
        <p>Already have an account?</p>
        <button class="btn login-btn" @click.prevent="showLogin">Login</button>
      </div>
    </div>

    <!-- Forgot Password Popup -->
    <div v-if="showForgot" class="modal-overlay">
      <div class="modal-content">
        <ForgotPassword @close="closeForgotPassword" />
      </div>
    </div>
  </div>
</template>

<script>
import ForgotPassword from './ForgotPassword.vue';

export default {
  name: "Login",
  components: { ForgotPassword },
  data() {
    return {
      portfolioURL: "https://chinni-portfolio.vercel.app/#home",
      loginData: { username: "", password: "" },
      registerData: { username: "", email: "", password: "" },
      loginErrors: {},
      registerErrors: {},
      showForgot: false
    };
  },
  methods: {
    showRegister() {
      this.$refs.container.classList.add("active");
    },
    showLogin() {
      this.$refs.container.classList.remove("active");
    },
    openForgotPassword() {
      this.showForgot = true;
    },
    closeForgotPassword() {
      this.showForgot = false;
    },
    validatePassword(password) {
      return password.length >= 6;
    },
    handleLogin() {
      this.loginErrors = {};
      if (!this.loginData.username) {
        this.loginErrors.username = "Username is required";
      }
      if (!this.validatePassword(this.loginData.password)) {
        this.loginErrors.password = "Password must be at least 6 characters long";
      }
      if (Object.keys(this.loginErrors).length === 0) {
        window.location.href = this.portfolioURL;
      }
    },
    handleRegister() {
      this.registerErrors = {};
      if (!this.registerData.username) {
        this.registerErrors.username = "Username is required";
      }
      if (!this.registerData.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.registerData.email)) {
        this.registerErrors.email = "Please enter a valid email";
      }
      if (!this.validatePassword(this.registerData.password)) {
        this.registerErrors.password = "Password must be at least 6 characters long";
      }
      if (Object.keys(this.registerErrors).length === 0) {
        window.location.href = this.portfolioURL;
      }
    }
  }
};
</script>

<style scoped>
@import url('https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css');

/* --- paste all your CSS here --- */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(90deg, #e2e2e2, #c9d6ff);
}
.container {
  position: relative;
  width: 850px;
  height: 550px;
  background: #fff;
  border-radius: 30px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.2);
  margin: 20px;
  overflow: hidden;
}
.form-box {
  position: absolute;
  right: 0;
  width: 50%;
  height: 100%;
  background: #fff;
  display: flex;
  align-items: center;
  color: #333;
  text-align: center;
  padding: 40px;
  z-index: 1;
  transition: 0.6s ease-in-out 1.2s, visibility 0s 1s;
}
.container.active .form-box {
  right: 50%;
}
.form-box.register {
  visibility: hidden;
}
.container.active .form-box.register {
  visibility: visible;
}
form {
  width: 100%;
}
.container h1 {
  font-size: 36px;
  margin: 10px 0;
}
.input-box {
  position: relative;
  margin: 30px 0;
}
.input-box input {
  width: 100%;
  padding: 13px 50px 13px 20px;
  background: #eee;
  border-radius: 8px;
  border: none;
  outline: none;
  font-size: 16px;
  color: #333;
  font-weight: 500;
}
.input-box input::placeholder {
  color: #888;
  font-weight: 400;
}
.input-box i {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 20px;
  color: #333;
}
.forgot-link {
  margin: -15px 0 15px;
}
.forgot-link a {
  font-size: 14.5px;
  color: #333;
  text-decoration: none;
}
.btn {
  width: 100%;
  height: 48px;
  background-color: #7494ec;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  color: #fff;
  font-weight: 600;
}
.container p {
  font-size: 14.5px;
  margin: 15px 0;
}
.social-icons {
  display: flex;
  justify-content: center;
}
.social-icons a {
  display: inline-flex;
  padding: 10px;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 24px;
  color: #333;
  text-decoration: none;
  margin: 0 8px;
}
.toggle-box {
  position: absolute;
  width: 100%;
  height: 100%;
}
.toggle-box::before {
  content: "";
  position: absolute;
  left: -250%;
  width: 300%;
  height: 100%;
  background: #7494ec;
  border-radius: 150px;
  z-index: 2;
  transition: 1.8s ease-in-out;
}
.container.active .toggle-box::before {
  left: 50%;
}
.toggle-panel {
  position: absolute;
  width: 50%;
  height: 100%;
  color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 2;
}
.toggle-panel.toggle-left {
  left: 0;
  transition-delay: 1.2s;
}
.container.active .toggle-panel.toggle-left {
  left: -50%;
  transition-delay: 0.6s;
}
.toggle-panel.toggle-right {
  right: -50%;
  transition-delay: 0.6s;
}
.container.active .toggle-panel.toggle-right {
  right: 0;
  transition-delay: 1.2s;
}
.toggle-panel p {
  margin-bottom: 20px;
}
.toggle-panel .btn {
  width: 160px;
  height: 46px;
  background: transparent;
  border: 2px solid #fff;
  box-shadow: none;
}
.error-message {
  color: #ff3333;
  font-size: 12px;
  margin-top: 5px;
  text-align: left;
  display: none;
}
.input-box.error input {
  border: 2px solid #ff3333;
  background-color: #ffeeee;
}
.input-box.error .error-message {
  display: block;
}
@media screen and (max-width: 650px) {
  .container {
    height: calc(100vh - 40px);
  }
  .form-box {
    bottom: 0;
    width: 100%;
    height: 70%;
  }
  .container.active .form-box {
    right: 0;
    bottom: 30%;
  }
  .toggle-box::before {
    left: 0;
    top: -270%;
    width: 100%;
    height: 300%;
  }
  .container.active .toggle-box::before {
    left: 0;
    top: 70%;
  }
  .toggle-panel {
    width: 100%;
    height: 30%;
  }
  .toggle-panel.toggle-left {
    top: 0;
  }
  .container.active .toggle-panel.toggle-left {
    left: 0;
    top: -30%;
  }
  .toggle-panel.toggle-right {
    right: 0;
    bottom: -30%;
  }
  .container.active .toggle-panel.toggle-right {
    bottom: 0;
  }
}
@media screen and (max-width: 450px) {
  .form-box {
    padding: 20px;
  }
  .toggle-panel h1 {
    font-size: 30px;
  }
}


</style>
