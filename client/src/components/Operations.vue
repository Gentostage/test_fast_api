<template>
  <div>
    <div class="row contest">
      <div class="row">
        <div v-if="error" class="col text-center">
          <div class="">Errors</div>
          <div class="error"><h6>{{ error }}</h6></div>
        </div>
      </div>
      <div class="col-12 align-content-center">
        <div class="row align-items-center">
          <div class="col-sm-2 offset-2">
            <input type="text" v-model="number1" class="form-control" id="number1" aria-describedby="emailHelp"
                   placeholder="number1">
          </div>
          +
          <div class="col-sm-2">
            <input type="text" v-model="number2" class="form-control" id="number2" aria-describedby="emailHelp"
                   placeholder="number2">
          </div>
          =
          <div class="col-sm-2">
            <input type="text" v-model="result" class="form-control" id="result" placeholder="result" readonly>
          </div>
          <div class="col-2">
            <button type="submit" @click="calculate" class="btn btn-primary">Посчитать</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'operation',
  data() {
    return {
      number1: '',
      number2: '',
      result: '',
      error: false,
      url_api: process.env.VUE_APP_URL_API
    }
  },
  methods: {
    calculate: function () {
      this.result = ''
      axios.post(this.url_api + '/api/operation/calc', {
            'number1': this.number1,
            'number2': this.number2
          }
      )
          .then(response => {
            this.error = false
            this.result = response.data.result
          })
          .catch(error => {
            let errors = error.response.data.errors
            this.error = errors[0]['msg']

          })
    }
  }
}
</script>

<style scoped>
.contest {
  width: 50%;
  margin-left: 25%;
  margin-top: 200px;
}

.error {
  color: red;
  margin-bottom: 15px;
}
</style>
