<template>
      <nav class="navbar is-spaced has-shadow" role="navigation" aria-label="main navigation">
        <!-- Logo -->
        <div class="navbar-brand">
          <RouterLink class="navbar-item">
            <h1 class="subtitle">Savannah Tales</h1>
          </RouterLink>
        </div>
    
        <!-- Menu -->
        <div class="navbar-menu">
          <!-- Righ nav links -->
          <div class="navbar-start">
            <RouterLink class="navbar-item">Our Mission</RouterLink>
          </div>
    
          <!-- Left nav links -->
          <div class="navbar-end">
            <div class="buttons">
              <RouterLink class="button">Log In</RouterLink>
              <RouterLink class="button is-primary is-outlined">Get Started</RouterLink>
            </div>
          </div>
        </div>
      </nav>
    </template>