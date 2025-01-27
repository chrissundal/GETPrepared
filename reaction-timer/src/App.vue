<template>
  <h1>Reaction Timer</h1>
  <button @click="start" v-if="!isPlaying">{{endgame ? 'Play again' : 'Play'}}</button>
  <Block v-if="isPlaying" :delay="delay" @end="endGame"/>
  <Results v-if="endgame" :score="reactionTimer"/>
</template>
<script>
import Block from "./components/Block.vue";
import Results from "@/components/Results.vue";
export default {
  name: 'App',
  components: {
    Block,
    Results,
  },
  data() {
    return {
      isPlaying: false,
      delay: null,
      reactionTimer: null,
      endgame: false,
    }
  },
  methods: {
    start() {
      this.delay = 2000 + Math.random() * 5000;
      this.isPlaying = true
      this.endgame = false;
    },
    endGame(reactionTime) {
      this.isPlaying = false
      this.reactionTimer = reactionTime;
      this.endgame = true;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #444;
  margin-top: 60px;
}
button {
  border: none;
  outline: none;
  background: #0faf87;
  padding: 15px 30px;
  font-size: medium;
  font-weight: bold;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.4s ease;
}
button:hover {
  transform: scale(1.05);
  background: #0c9370;
}
</style>
