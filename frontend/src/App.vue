<template>
  <div class="container">
    <h1 class="title">My Articles</h1>
    <div class="card" v-for="article in articles" :key="article.id">
      <div class="card-header">
        <div class="card-header-title">{{ article.title }}</div>
      </div>
      <div class="card-content">
        {{ article.body }}
      </div>

      <div class="card-footer">
        <div class="footer-item"><time>{{ article.published_on }}</time></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      articles: []
    }
  },
  
  mounted () {
    axios
      .get('http://127.0.0.1:8000/api/v1/articles/')
      .then(response => {
        this.articles = response.data
        console.log(response.data)
      });
  }
}
</script>