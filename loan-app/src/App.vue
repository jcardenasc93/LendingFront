<template>
  <div class="container">
    <AppHeader/>
    <form id="loan-form" v-on:submit.prevent="processLoan">
      <div class="item">
        <label for="taxId">TaxId<span>*</span></label>
        <input id="taxId" type="text" name="taxId" required v-model="taxId"/>
      </div>
      <div class="item">
        <label for="businessName">Business Name<span>*</span></label>
        <input id="businessName" type="text" name="businessName" required v-model="businessName"/>
      </div>
      <div class="item">
        <label for="amount">Loan Amount<span>*</span></label>
        <input id="amount" type="number" name="amount" required v-model="amount"/>
      </div>
      <input class="submit-button" type="submit" value="Submit">
    </form>
  <br/>
  <h2>{{applicationState}}</h2>
  </div>
</template>

<script>
import axios from 'axios'
import AppHeader from './components/Header'

export default {
  name: 'App',
  data() {
    return {
      taxId: "",
      businessName: "",
      amount: "",
      applicationState: ""
    }
  },
  components: {
    AppHeader,
  },
  methods: {
      processLoan() {
        let body = {
          "amount": this.amount
        }
        axios.post('http://localhost:5005/evaluate-loan', body)
          .then(resp => {
              if (resp.status == 200) {
                this.applicationState = resp.data.message;
                console.log(this.applicationState)
              }
              else {
                alert("Sorry. Your application coudn't be evaluated")
              }
          })

      }
  
    }
}

</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Poppins', sans-serif;
  }
  .container {
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    border: 2px solid steelblue;
    padding: 30px;
    border-radius: 5px;
  }
  .btn {
    display: inline-block;
    background: #000;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 15px;
    font-family: inherit;
  }
  .btn:focus {
    outline: none;
  }
  .btn:active {
    transform: scale(0.98);
  }
  .btn-block {
    display: block;
    width: 100%;
  }
  
  label {
    padding: 0;
    margin-right: 1em;
    outline: none;
    font-family: Roboto, Arial, sans-serif;
    font-size: 14px;
    color: #666;
    line-height: 22px;
  }
  
  .item {
    position: relative;
    margin: 10px 0;
  }
  .item span {
    color: red;
  }
  .submit-button {
    cursor: pointer;
    display: inline-block;
    background: #333;
    color: white;
    font-size: 18px;
    border: 0;
    padding: 0.5rem 1.5rem;
  }
  
  .submit-button:focus {
    outline: none;
  }
  
  .submit-button:hover {
    transform: scale(0.98);
  }
</style>
