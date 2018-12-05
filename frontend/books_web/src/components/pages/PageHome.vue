<template>
<div>
<ul v-if="posts && posts.length">
  <li v-for="(post, index) of posts" :key="index">
    <p><strong>{{post.title}}</strong></p>
    <p>{{post.content}}</p>
  </li>
</ul>

<ul v-if="errors && errors.length">
  <li v-for="(error, index) of errors" :key="index">
    {{error.message}}
  </li>
</ul>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: null,
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/chapter/')
      .then((response) => {
        // JSON responses are automatically parsed.
        this.posts = response.data;
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>
