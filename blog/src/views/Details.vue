<template>
  <div v-if="error">{{error}}</div>
  <div v-if="post" class="post">
    <h3>{{post.title}}</h3>
    <p class="pre">{{post.body}}</p>
  </div>
  <div v-else>
    <h3>Loading post...</h3>
  </div>
  <button @click="back">Back</button>
</template>
<script setup>
import getPost from "@/composables/getPost.js";
import router from "@/router/index.js";
const props = defineProps({
  id: {
    type: String,
    required: true
  }
})
  const {post, error, load} = getPost(props.id)
  load()
  const back = () => {
    router.push({name: 'home'})
  }
</script>
<style scoped>
.post {
  max-width: 1200px;
  margin: 0 auto;
}
.post p {
  color: #444;
  line-height: 1.5em;
  margin-top: 40px;
}
.pre {
  white-space: pre-wrap;
}
</style>
