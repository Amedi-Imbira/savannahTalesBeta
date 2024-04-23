<script setup>
import Navbar from '@/components/Navbar.vue'
</script>

<template>
      <Navbar />
      
      <section>
            <div class="container">
                  <div class="image-wrapper">
                        <h1>Put an image here</h1>
                  </div>
                  <div class="form-wrapper">
                        <h1>Login to your account</h1>
                        <form>
                              <button type="submit">Continue with Google</button>
                        </form>
                        or
                        <form>
                              <div class="form-group">
                                    <label>Email</label>
                                    <input type="text" placeholder="Enter your email" />
                              </div>

                              <div class="from-group">
                                    <label>Password</label>
                                    <input type="password" placeholder="Enter your password" />
                              </div>
                              <div class="form-group-check">
                                    <div class="check-wrapper">
                                          <input type="checkbox" name="remember" value="Remember me" />
                                          Remember me
                                    </div>
                                    <RouterLink>Forgot password?</RouterLink>
                              </div>
                              <button type="submit">Login</button>
                        </form>
                        <p>Not registered yet? <RouterLink>Create an account</RouterLink></p>
                  </div>
            </div>
      </section>
</template>

<style scoped>
h1 {
      font-size: 2.6rem;
}
.container {
      min-height: 91.3vh;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding:0 10rem;
}

label {
      display: block;
}

input[type=text], input[type=password] {
      width: 100%;
      height: 40px;
}

.form-group {
      margin: 15px 0;
}

.form-group-check {
      display: flex;
      justify-content: space-between;
}

p {
      margin-top: 40px;
}

button {
      width: 100%;
}
</style>