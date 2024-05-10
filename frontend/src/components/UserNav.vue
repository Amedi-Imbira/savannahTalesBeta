<template>
      <nav class="navbar is-light is-spaced has-shadow">
        <div class="container">
          <div class="navbar-brand">
            <h1 class="subtitle">
              <RouterLink class="navbar-item" to="/">Savannah Tales</RouterLink>
            </h1>
          </div>
    
          <div class="navbar-menu">
            <div class="navbar-start">
              <form>
                <div class="field">
                  <div class="control has-icons-left">
                    <input
                      type="text"
                      class="input is-small"
                      placeholder="Search"
                    />
                    <span class="icon is-small is-left has-text-primary">
                      <font-awesome-icon icon="fa fa-search" />
                    </span>
                  </div>
                </div>
              </form>
            </div>
            <div class="navbar-end">
              <RouterLink
                to="/post"
                class="button is-primary is-outlined is-rounded is-hovered"
                >Create Post</RouterLink
              >
              <RouterLink to="/toggle" class="navbar-item"
                ><font-awesome-icon icon="fa fa-moon"
              /></RouterLink>
              <RouterLink to="/notifications" class="navbar-item"
                ><font-awesome-icon icon="fa fa-bell"
              /></RouterLink>
              <RouterLink to="/bookmarks" class="navbar-item"
                ><font-awesome-icon icon="fa fa-bookmark"
              /></RouterLink>
              <div class="navbar-item has-dropdown is-hoverable">
                <figure class="navbar-link image is-28x28">
                  <img src="../assets/profile.jfif" alt="" class="is-rounded">
                </figure>
                <div class="navbar-dropdown is-boxed">
                  <a class="navbar-item">Profile</a>
                  <a class="navbar-item">Settings</a>
                  <a class="navbar-item">Become a member</a>
                  <hr class="navbar-divider">
                  <a class="navbar-item">Sign out</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </template>
    
    