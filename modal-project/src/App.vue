<template>
  
  <button class="darkModeButton" @click="setDarkMode" :class="{dark:darkMode}">{{ darkMode ? 'LightMode' : 'DarkMode' }}</button>
  <h3 style="text-align: left; margin: 10px">My cash: {{ money }}</h3>
  <div>
  </div>
  <h1 class="header">{{ title }}</h1>
<!--  <h3>testing</h3>-->
<!--  <input type="text" ref="name">-->
<!--  <button @click="handleClick">Click me</button>-->
  <div>
    <button v-if="!showModal && !gotScammed" @click="setShowModal">Once in a lifetime opportunity</button>
<!--    endre en div til teleport for å flytte den inn i modals '.' for klasser, '#' ved id-->
    <teleport to=".modals" v-if="showModal"> 
      <Modal :closeModal="setShowModal" :header="header" :scammed="getScammed" :theme="darkMode" @close="setShowModal"/>
    </teleport>
    <teleport to=".modals" v-if="showModalForm">
      <ModalForm :theme="darkMode" @close="toggleModalForm">
        <template v-slot:links>
          <a href="#">Sounds good</a><br>
          <a href="#">More info</a>
        </template>
        <h1>Hello, this is a message from {{scamCompany[Math.floor(Math.random() * scamCompany.length)]}}</h1>
        <p>{{scamsPlot[Math.floor(Math.random() * scamsPlot.length)]}}</p>
      </ModalForm>  
    </teleport>
    <br>
    <button v-if="!showModalForm && !gotScammed" @click="toggleModalForm">More great offers</button>
    <h1 class="scamtext" v-if="gotScammed">{{scamText}}</h1>
    
  </div>
</template>

<script>
//import {ref} from "vue";
import Modal from './components/Modal.vue'
import ModalForm from './components/ModalForm.vue'
export default {
  name: 'App',
  components: {
    Modal,
    ModalForm,
  },
  data() {
    return {
      title: 'Great deals',
      showModal: false,
      showModalForm: false,
      gotScammed: false,
      money: 1000,
      header: "Hello my friend! Do i have an offer for you!",
      scamText: "You got scammed bigtime, you blue eyed fool! Wave goodbye to your 1000 bucks!",
      darkMode: false,
      scamCompany: [
        "Microsoft Tech Support",
        "IRS (Internal Revenue Service)",
        "Bank of America",
        "Amazon Customer Service",
        "Apple Customer Service",
        "Norton Antivirus"
      ],
      scamsPlot: [
        "You have a refund ready for you, all you need to do is add your personal information including your credit card. And we will take care of the rest!",
        "Congratulations! You've won a lifetime supply of invisible socks. Just send us your bank details, and we'll ship them right away!",
        "Your pet rock has been selected for a free vacation. Provide your social security number to claim this exclusive offer!",
        "You've been chosen to join the Secret Society of Unicorn Riders. Simply share your credit card info to receive your magical unicorn!",
        "Alert! Your fridge warranty is about to expire. Renew it now by sending us your PIN number, and keep your veggies safe!",
        "Good news! You've inherited a fortune from a distant Martian relative. Transfer a small fee to unlock your intergalactic riches!",
      ],
    }
  },
  methods: {
    setShowModal() {
      this.showModal = !this.showModal;
    },
    toggleModalForm() {
      this.showModalForm = !this.showModalForm;
    },
    getScammed() {
      this.money = 0;
      this.showModal = false;
      this.gotScammed = true;
    },
    setDarkMode() {
      this.darkMode = !this.darkMode;
    }
  }
  //   handleClick() {
  //     //this.title = this.$refs.name.value;
  //     //this.$refs.name.classList.add('active');
  //     //this.$refs.name.focus();
  //   }
  // }
}
</script>

<style>
#app, .modals {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  background-image: url("assets/scammer.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
}

.scamtext {
  border: none;
  width: 600px
}
.darkModeButton {
  width: 100px;
}
.dark {
  background: darkgray;
  color: black;
}
.header {
  color: black;
  font-size: 50px;
  font-weight: bold;
}
</style>
