<template>
  <UserNav />

  <div class="container-fluid">
      <div class="container">
            <article class="media">
                  <figure class="media-left">
                        <p class="image is-64x64"><img src="../assets/profile.jfif" alt="" /></p>
                  </figure>

                  <div class="nav-level">
                        <div class="level-right">
                              <p class="level-item">Stephen Imbira</p>
                              <p class="level-item">22h</p>
                        </div>

                        
                  </div>

                  <div class="media-content">
                        <div class="content">
                              <h1 class="title">Forever</h1>
                              <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Libero nihil enim quo odio, odit quasi blanditiis perferendis animi dolor eligendi corrupti ab aut impedit, veniam cumque dicta, quisquam earum? Repellendus.</p>

                        </div>
                  </div>
                  
            </article>
      </div>
  </div>




  <div class="container-fluid">
    <div class="container">
      <article class="media has-background-primary">
        <nav class="level">
          <!-- Left side -->
          <div class="level-left">
            <div class="level-item">
              <p class="image is-64x64">
                <img src="../assets/profile.jfif" alt="" />
              </p>
            </div>
            <div class="level-item">
              <strong>Eissa Hatem</strong>
            </div>
            <p class="level-item">22h</p>
          </div>

          <!-- right side -->
          <div class="level-right">
            <p class="level-item">Bookmark</p>
            <p class="level-item">Share</p>
            <p class="level-item">More</p>
          </div>
        </nav>

        <div class="media-content">
            <div class="content">
                  <h1 class="title">This time: Xdash AI vs Mistral AI</h1>
            </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import UserNav from "../components/UserNav.vue";

export default {
  components: {
    UserNav,
  },
};
</script>
