<template>
  <div class="backdrop" @click.self="closeThisModal">
    <div class="modal" :class="{ dark:theme }">
      <h1 v-if="!showMore">{{ header }}</h1><br>
      <p v-if="showMore">{{ text }}</p>
      <button v-if="!showMore" @click="nextText()">Learn more</button>
      <button @click="closeModal">No Thanks</button>
      <button v-if="showMore" @click="scammed">Yes</button>
    </div>
  </div>
</template>
<script>
export default {
  props: ['closeModal','header','scammed','theme'],
  data() {
    return {
      showMore: false,
      text: "I'm a wealthy African Prince, with my accounts frozen. I only need 1000 dollars to open them. Can you help me? I will double your money!"
    }
  },
  methods: {
    nextText(){
      this.showMore = !this.showMore;
    },
    closeThisModal(){
      this.$emit('close');
    }
  }
}
</script>
<style>
.modal {
  width: 400px;
  padding: 20px;
  margin: 100px auto;
  background: white;
  border-radius: 10px;
  
}
.backdrop {
  top: 0;
  position: fixed;
  background: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
} 
.modal h1 {
  color: #c047e2;
  border: none;
  padding: 0;
}
.modal dark {
  border: 2px solid #c047e2;
  width: 500px;
  padding: 20px;
  margin: 100px auto;
  background: darkgray;
  border-radius: 10px;
}
.modal dark h1{
  color: black;
}
</style>