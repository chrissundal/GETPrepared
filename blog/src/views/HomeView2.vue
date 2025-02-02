<template>
  <div class="home">
    <h1>Home</h1>
    <input type="text" v-model="search">
    <p>search: {{search}}</p>
    <div v-for="name in match" :key="name">{{name}}</div>
    <button @click="handleClick">stop watching</button>
<!--    <h2>Refs</h2>-->
<!--    <p>{{chrisOne.name}} - {{chrisOne.age}}</p>-->
<!--    <button @click="updateChrisOne">Update</button>-->
<!--    <h2>Reactive</h2>-->
<!--    <p>{{chrisTwo.name}} - {{chrisTwo.age}}</p>-->
<!--    <button @click="updateChrisTwo">Update</button>-->
<!--    <button @click="age++">Add 1 to age</button>-->
<!--    <input type="text" v-model="name" placeholder="Enter your name"/>-->
  </div>

</template>

<script setup>
import {ref, computed, watch, watchEffect} from "vue";
  const names = ref(['Mario','Yoshi','Luigi','Toad','Bowser','Koopa','Peach']);
  const search = ref('');
  const match = computed(() => {
    return names.value.filter((name) => name.toLowerCase().includes(search.value.toLowerCase()));
  })
  const stopWatch = watch(search, () => {
    console.log('test')
  })
  const stopEffectWatch = watchEffect(() => {
    console.log('testeffect',search.value);
  })
  const handleClick = () => {
    stopWatch();
    stopEffectWatch();
  }
  // const name = computed(() => {
  //   return 'chris'
  // })
  // const chrisOne = ref({name: 'Chris', age: 37})
  // const chrisTwo = reactive({name: 'Bjarne', age: 30}) //kan ikke være feks string da det ikke er mulig med .value
  // const updateChrisOne = () => {
  //   chrisOne.value.age = 30
  // }
  // const updateChrisTwo = () => {
  //   chrisTwo.age = 25;
  // }
  // const parag = ref(null)
  // const name = ref('Christoffer');
  // const age = ref(37);
  // const handleClick = () => {
  //   name.value = 'Bjarne';
  //   age.value = 30;
  // parag.value.classList.add('test');
  // parag.value.textContent = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate, nihil.'


</script>

