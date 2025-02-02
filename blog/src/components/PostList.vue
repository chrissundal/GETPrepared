<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id">
      <SinglePost v-if="showPosts" :post="post"/>
    </div>
      <button @click="showPosts = !showPosts">Toggle</button>
  </div>
</template>
<script setup>
  import SinglePost from "@/components/SinglePost.vue";
  import {onMounted, ref} from "vue";

  const props = defineProps({
    posts: Array,
  })
  onMounted(() => {

  })
  const showPosts = ref(true)
</script>
<style scoped>

</style>
