<template>
  <div class="page-full">
    <div :class="['container', { active: isActive }]">
      <!-- Login Box -->
      <div class="form-box login">
        <form @submit.prevent="handleLogin">
          <h1>Login</h1>
          <div class="input-box" :class="{ error: errors.email }">
            <input
              type="email"
              placeholder="Email"
              v-model="loginData.email"
            />
            <i class="bx bx-envelope"></i>
            <div class="error-message">{{ errors.email }}</div>
          </div>
          <div class="input-box" :class="{ error: errors.password }">
            <input
              type="password"
              placeholder="Password"
              v-model="loginData.password"
            />
            <i class="bx bx-lock-alt"></i>
            <div class="error-message">{{ errors.password }}</div>
          </div>
          <div class="forgot-link">
            <a href="#">Forgot password?</a>
          </div>
          <button type="submit" class="btn">Login</button>
          <p>or login with social platforms</p>
          <div class="social-icons">
            <a href="#"><i class="bx bxl-google"></i></a>
            <a href="#"><i class="bx bxl-facebook"></i></a>
            <a href="#"><i class="bx bxl-twitter"></i></a>
          </div>
        </form>
      </div>

      <!-- Register Box -->
      <div class="form-box register">
        <form @submit.prevent="handleRegister">
          <h1>Register</h1>
          <div class="input-box" :class="{ error: errors.name }">
            <input type="text" placeholder="Name" v-model="registerData.name" />
            <i class="bx bx-user"></i>
            <div class="error-message">{{ errors.name }}</div>
          </div>
          <div class="input-box" :class="{ error: errors.email }">
            <input
              type="email"
              placeholder="Email"
              v-model="registerData.email"
            />
            <i class="bx bx-envelope"></i>
            <div class="error-message">{{ errors.email }}</div>
          </div>
          <div class="input-box" :class="{ error: errors.password }">
            <input
              type="password"
              placeholder="Password"
              v-model="registerData.password"
            />
            <i class="bx bx-lock-alt"></i>
            <div class="error-message">{{ errors.password }}</div>
          </div>
          <button type="submit" class="btn">Register</button>
          <p>or register with social platforms</p>
          <div class="social-icons">
            <a href="#"><i class="bx bxl-google"></i></a>
            <a href="#"><i class="bx bxl-facebook"></i></a>
            <a href="#"><i class="bx bxl-twitter"></i></a>
          </div>
        </form>
      </div>

      <!-- Toggle Panels -->
      <div class="toggle-box">
        <div class="toggle-panel toggle-left">
          <h1>Hello, Welcome!</h1>
          <p>Don’t have an account?</p>
          <button class="btn" @click="toggle">Register</button>
        </div>
        <div class="toggle-panel toggle-right">
          <h1>Welcome Back!</h1>
          <p>Already have an account?</p>
          <button class="btn" @click="toggle">Login</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthPage",
  data() {
    return {
      isActive: false,
      loginData: {
        email: "",
        password: "",
      },
      registerData: {
        name: "",
        email: "",
        password: "",
      },
      errors: {},
    };
  },
  methods: {
    toggle() {
      this.isActive = !this.isActive;
      this.errors = {};
    },
    handleLogin() {
      this.errors = {};
      if (!this.loginData.email) {
        this.errors.email = "Email is required";
      }
      if (!this.loginData.password) {
        this.errors.password = "Password is required";
      }
      if (Object.keys(this.errors).length === 0) {
        alert("Login successful!");
        this.$router.push({ name: 'Home' });
      }
    },
    handleRegister() {
      this.errors = {};
      if (!this.registerData.name) {
        this.errors.name = "Name is required";
      }
      if (!this.registerData.email) {
        this.errors.email = "Email is required";
      }
      if (!this.registerData.password) {
        this.errors.password = "Password is required";
      }
      if (Object.keys(this.errors).length === 0) {
        alert("Registration successful!");
        this.$router.push({ name: 'Home' });
      }
    },
  },
};
</script>

<style scoped>
@import url("https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
.page-full {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f0f2f5;
}
.container {
  position: relative;
  width: 850px;
  height: 500px;
  background: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
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
  background-color: #3c61e2; /* 🔵 main theme color */
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  color: #fff;
  font-weight: 600;
  transition: 0.3s;
}
.btn:hover {
  background-color: #2c4cc9;
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
  background: #3c61e2; /* 🔵 theme color */
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
</style>
