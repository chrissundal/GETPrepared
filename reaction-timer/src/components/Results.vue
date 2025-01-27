<template>
  <h3>{{cheers[Math.floor(Math.random() * cheers.length)-1]}} You did it in {{score}} ms</h3>
  <p class="rank">{{rank}}</p>
</template>
<script>
export default {
  props: ['score'],
  data() {
    return {
      rank: null,
      cheers: [
          "Good job!",
          "Not bad!",
          "Almost the same time as myself!",
          "Wow, have you been training?",
          "Faster than your own shadow!",
          "Not as fast as me, but good enough!",
          "Next time you will get it!",
          "Sweet!",
          "Thats not bad!"
      ]   
    }
  },
  mounted() {
    if (this.score < 300) {
      this.rank = 'Gunslinger'
    } else if (this.score < 600) {
      this.rank = 'Rapid reflexes'
    } else {
      this.rank = 'Turtle mode'
    }
  }
}
</script>
<style scoped>
.rank {
  font-size: 1.4em;
  color: #0faf87;
  font-weight: bold;
}
</style>