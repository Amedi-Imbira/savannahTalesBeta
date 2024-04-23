<template>
      <nav>
            <h2>
                  <RouterLink to="/">Savannah Tales</RouterLink>
            </h2>
            <ul>
                  <li><RouterLink to="/about">Our Mission</RouterLink></li>
                  <li><RouterLink to="/login">Sign In</RouterLink></li>
                  <li><RouterLink to="/signup" class="cta-fill-normal">Get Started</RouterLink></li>
            </ul>
      </nav>
</template>

<style scoped>
nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 10rem;
      border-bottom: 1px solid #E4E2E1;
}
ul li {
      display: inline-block;
      padding: 0 1.5rem;
}
</style>