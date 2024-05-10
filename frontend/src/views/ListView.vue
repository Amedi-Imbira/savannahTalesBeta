<template>
  <UserNav />

  <div class="container-fluid">
    <div class="container mt-6">
      <div class="columns">
        <div class="column is-two-thirds">
          <article class="media box has-background-light">
            <figure class="media-left">
              <p class="image is-64x64">
                <img src="../assets/profile.jfif" />
              </p>
            </figure>
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>John Smith</strong> <small>@johnsmith</small>
                  <small>31m</small>
                  <br />
                  <p class="title is-4">This is title</p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin
                  ornare magna eros, eu pellentesque tortor vestibulum ut. eu pellentesque tortor vestibulum ut
                  eu pellentesque tortor vestibulum ut
                </p>
              </div>
              <nav class="level is-mobile">
                <div class="level-left">
                  <a class="level-item">
                    <div class="tags">
                      <span class="tag is-primary">Humor</span>
                      <span class="tag is-primary">Web Development</span>
                    </div>
                  </a>
                </div>
                
                <div class="level-right">
                  <div class="level-item">
                    <button class="button is-primary is-outlined is-small">
                      <font-awesome-icon icon="fa fa-bookmark" />

                    </button>
                    
                  </div>
                  <div class="dropdown is-hoverable">
                    <div class="dropdown-trigger">
                      <button class="button is-outlined is-primary is-small" aria-haspopup="true" aria-controls="dropdown-menu">
                        <font-awesome-icon icon="fa fa-ellipsis" />
                      </button>
                    </div>
                    <div class="dropdown-menu" id="dropdown-menu" role="menu">
                      <div class="dropdown-content">
                        <a href="#" class="dropdown-item">Follow author</a>
                        <hr class="dropdown-divider">
                        <a href="#" class="dropdown-item">Mute author</a>
                        <a href="#" class="dropdown-item has-text-danger">Report story</a>
                      </div>
                    </div>
                  </div>
                </div>
              </nav>
            </div>
            <div class="media-right">
              <figure class="image is-128x128">
                <img src="../assets/profile.jfif" alt="">
              </figure>
            </div>
          </article>
        </div>
        <!-- Side column -->
        <div class="column">Side</div>
      </div>
    </div>
  </div>
</template>

<script>
import UserNav from "@/components/UserNav.vue";

export default {
  components: {
    UserNav,
  },
};
</script>
