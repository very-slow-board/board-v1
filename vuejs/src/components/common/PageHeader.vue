<template>
  <h1
    class="page__header"
    v-text="title"
  ></h1>
</template>

<script>
export default {
  props: {
    title: String
  }
}
</script>

<style lang="scss">
.page__header {
  color: #333;
  font-size: 24px;
  font-weight: bold;
  margin: 30px 0 20px 0;
  padding: 0;
  line-height: 30px;
}
</style>
