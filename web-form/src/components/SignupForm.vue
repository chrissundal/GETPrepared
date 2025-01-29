<template>
  <form @submit.prevent="handleSubmit">
    <label>Email:</label>
    <input type="email" v-model="email" required/>
    <label>Password:</label>
    <input type="password" v-model="password" minlength="6" required/>
    <label>Role:</label>
    <select v-model="role">
      <option value="developer">Web Developer</option>
      <option value="designer">Web Designer</option>
    </select>
    <label>Skills:</label>
    <input type="text" :placeholder="message" v-model="tempSkill" @keyup="addSkill"/>
    <div v-for="skill in skills" key="skill" class="pill">
      <span @click="deleteSkill(skill)">{{skill}}</span>
    </div>
    <div class="terms">
      <input type="checkbox" v-model="terms" required>
      <label>Accept terms and conditions</label>
    </div>
    
    <div class="submit">
      <button type="submit">Create an account</button>
    </div>
<!--    <div>-->
<!--      <input type="checkbox" value="chris" v-model="names">-->
<!--      <label>Chris</label>-->
<!--    </div>-->
<!--    <div>-->
<!--      <input type="checkbox" value="bjarne" v-model="names">-->
<!--      <label>Bjarne</label>-->
<!--    </div>-->
<!--    <div>-->
<!--      <input type="checkbox" value="tore" v-model="names">-->
<!--      <label>Tore</label>-->
<!--    </div>-->
  </form>
  <p>Email: {{email}}</p>
  <p>Password: {{password}}</p>
  <p>Role: {{role}}</p>
  <p>Checkbox: {{terms}}</p>
<!--  <p>Names: {{names}}</p>-->
</template>
<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      role: "",
      terms: false,
      names: [],
      tempSkill: "",
      skills: [],
      message: "",
      newUser: '',
    }
  },
  methods: {
    addSkill(e) {
      this.message = "";
      if(e.key === "," && this.tempSkill){
        let formatSkill = this.tempSkill.slice(0,this.tempSkill.length - 1);
        if (!this.skills.includes(formatSkill)){
          this.skills.push(formatSkill)
        }
        else {
          this.message = "Already picked";
        }
        this.tempSkill = ""
      }
    },
    deleteSkill(skill) {
        //this.skills.splice(this.skills.indexOf(skill), 1);    
      this.skills = this.skills.filter((item) => {
        return skill !== item
      })
    },
    handleSubmit() {
      let newUser = {
        email: this.email,
        password: this.password,
        role: this.role,
        skills: this.skills,
        terms: this.terms
      }
      this.newUser = newUser
      console.log(this.newUser)
    }
  }
}
</script>
<style scoped>
  form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
  }
  label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  input, select {
    width: 100%;
    display: block;
    padding: 10px 6px;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  input[type=checkbox] {
    display: inline-block;
    width: 16px;
    margin: 0 10px 0 0;
    position: relative;
    top: 2px;
  }
  .pill {
    display: inline-block;
    margin: 20px 10px 0 0;
    padding: 6px 12px;
    background: #eee;
    border-radius: 20px;
    font-size: 12px;
    letter-spacing: 1px;
    font-weight: bold;
    color: #777;
    cursor: pointer;
  }
  button {
    background: #0b6dff;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
    cursor: pointer;
  }
  .submit {
    text-align: center;
    
  }
</style>