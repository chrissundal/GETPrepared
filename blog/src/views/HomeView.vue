<template>
<div class="home">
  <h1>Home</h1>
  <div v-if="error">{{error}}</div>
  <div v-if="posts.length">
    <PostList :posts="posts" />
  </div>
  <div v-else>
    <h3>Loading posts...</h3>
  </div>
</div>
</template>
<script setup>
  import {ref} from "vue";
  import PostList from "@/components/PostList.vue";
  import GetPosts from "@/composables/getPosts.js";
  const props = defineProps({

  })
  const {posts,error,load} = GetPosts()
  load()
</script>

<style scoped>

</style>
