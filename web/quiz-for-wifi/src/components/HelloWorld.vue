<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1{
  color: #ffffff;
}
@media screen and (max-width: 992px) {
  h1{
    font-size: 20px;
    margin-bottom: 0;
  }
}
</style>
