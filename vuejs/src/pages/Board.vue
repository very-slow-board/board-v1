<template>
  <q-page class="page__container board">
    <page-header :title="title" />
    <board-list></board-list>
  </q-page>
</template>

<script>
import PageHeader from '../components/common/PageHeader.vue'
import BoardList from '../components/board/BoardList.vue'

export default {
  data () {
    return {
      title: 'Board'
    }
  },

  components: {
    PageHeader,
    BoardList
  }
}
</script>

<style lang="scss">
.board {
  &__content {
    padding: 20px;
  }
}
</style>
