<template>
      <nav class="navbar is-spaced has-shadow is-light">
        <div class="container">
          <!-- Brand -->
          <div class="navbar-brand">
            <RouterLink to="/" class="navbar-item">
              <p class="title is-4">Savannah Tales</p>
            </RouterLink>
          </div>
          <!-- End of brand -->
    
          <!-- Navbar menu -->
          <div class="navbar-menu">
                <div class="navbar-start">
                      <form>
                            <div class="field">
                                  <div class="control has-icons-left">
                                        <input type="text" class="input is-small" placeholder="Search">
                                        <span class="icon is-left is-small has-text-primary">
                                              <font-awesome-icon icon="fa fa-search" />
                                        </span>
                                  </div>
                            </div>
                      </form>
                </div>
                <div class="navbar-end">
                      <RouterLink to="kk" class="button is-primary is-outlined">Create Post</RouterLink>
                      <RouterLink to="/" class="navbar-item"><font-awesome-icon icon="fa fa-moon" /></RouterLink>
                      <RouterLink to="/" class="navbar-item"><font-awesome-icon icon="fa fa-bell" /></RouterLink>
                      <RouterLink to="/" class="navbar-item"><font-awesome-icon icon="fa fa-bookmark" /></RouterLink>
                      <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link">More</a>
    
                            <div class="navbar-dropdown">
                                  <div class="navbar-item">
                                        View Profile
                                  </div>
                                  <hr class="navbar-divider">
                                  <a href="#" class="navbar-item">Sign Out</a>
                            </div>
                      </div>
                </div>
          </div>
          
        </div>
      </nav>
</template>
    