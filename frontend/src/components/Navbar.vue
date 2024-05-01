<template>
  <nav
    class="navbar is-spaced has-shadow"
    role="navigation"
    aria-label="main navigation"
  >
    <!-- Logo -->
    <div class="navbar-brand">
      <RouterLink to="/" class="navbar-item">
        <h1 class="subtitle">Savannah Tales</h1>
      </RouterLink>

      <RouterLink
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden=""></span>
        <span aria-hidden=""></span>
        <span aria-hidden=""></span>
        <span aria-hidden=""></span>
      </RouterLink>
    </div>

    <!-- Menu -->
    <div class="navbar-menu">
      <!-- Righ nav links -->
      <div class="navbar-start">
        <RouterLink to="/mission" class="navbar-item">Our Mission</RouterLink>
      </div>

      <!-- Left nav links -->
      <div class="navbar-end">
        <div class="buttons">
          <RouterLink to="/login" class="button">Log In</RouterLink>
          <RouterLink  to="/signup" class="button is-primary is-outlined"
            >Get Started</RouterLink
          >
        </div>
      </div>
    </div>
  </nav>
</template>
