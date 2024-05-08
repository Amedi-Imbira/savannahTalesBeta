<template>
  <article class="media has-background-light p-3">
    <figure class="media-left">
      <p class="image is-48x48">
        <img src="../assets/profile.jfif" class="is-rounded" />
      </p>
    </figure>
    <div class="media-content">
      <div class="content">
        <p>
          <strong>John Smith</strong> <small>@johnsmith</small>
          <small> . {{ article.published_on }}</small>
          <br />
          <h1 class="title is-4">{{ article.title }}</h1>
          {{ truncateText(article.body, 30) }}
        </p>
      </div>
      <nav class="level is-mobile">
        <div class="level-left">
          <a class="tag is-primary is-rounded">Humor</a>
        </div>

        <div class="level-right">
          <a href="" class="level-item has-text-primary"
            ><font-awesome-icon icon="fa fa-book-bookmark"
          /></a>
          <a href="" class="level-item has-text-primary"
            ><font-awesome-icon icon="fa fa-ellipsis"
          /></a>
        </div>
      </nav>
    </div>
    <div class="media-right">
      <figure class="image is-128x128">
        <img src="../assets/profile.jfif" />
      </figure>
    </div>
  </article>
</template>

<script>
export default {
  props: {
    article: {
      type: Object,
      required: true
    }
  },

  mounted() {
    console.log(this.article)
  },

  methods: {
    truncateText(text, maxLength) {
      if (text.length <= maxLength) {
        return text;
      } else {
        let words = text.split(' ');
        return words.slice(0, maxLength).join(' ') + '...' 
      }
    }
  }
}
</script>
