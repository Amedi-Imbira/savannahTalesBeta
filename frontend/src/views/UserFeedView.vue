<template>
  <UserNav />

  <div class="container-fluid mt-6">
    <div class="container">
      <div class="columns">
        <div class="column is-two-thirds">
          <Article
            v-for="(article, index) in articles"
            :key="index"
            :article="article"
          />
        </div>

        <div class="column has-background-warning">
          <SideBar />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SideBar from "@/components/SideBar.vue";
import Article from "../components/Article.vue";
import UserNav from "../components/UserNav.vue";

export default {
  components: {
    UserNav,
    Article,
    SideBar,
  },

  data() {
    return {
      articles: [],
    };
  },

  mounted() {
    this.fetchArticles();
  },

  methods: {
    async fetchArticles() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/v1/articles");
        this.articles = res.data;
        console.log(res.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>


