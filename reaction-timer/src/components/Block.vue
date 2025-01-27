<template>
  
  <div class="block" v-if="showBlock" @click="stopTimer" :style="{ top: randomTop + 'px', left: randomLeft + 'px', position: 'absolute' }">Click Me</div>
</template>
<script>
export default {
  props: ['delay'],
  data() {
    return {
      showBlock: false, 
      timer: null,
      reactionTimer: null,
      randomTop: 0,
      randomLeft: 0,
    }
  },
  mounted() {
    setTimeout(() => {
      this.setRandomPosition();
      this.showBlock = true;
      this.startTimer();
    }, this.delay);
  },
  methods: {
    startTimer() {
      this.timer = setInterval(() => {
        this.reactionTimer += 10;
      },10)
    },
    stopTimer() {
      clearInterval(this.timer);
      this.$emit('end', this.reactionTimer);
    },
    setRandomPosition() {
      this.randomTop = Math.floor(Math.random() * 800);
      this.randomLeft = Math.floor(Math.random() * 600);
    },
  }
}
</script>
<style scoped>
  .block {
    width: 200px;
    border-radius: 20px;
    background: #0faf87;
    color: white;
    text-align: center;
    padding: 50px 0;
    margin: 40px auto;
  }
</style>