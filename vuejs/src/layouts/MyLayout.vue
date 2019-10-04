<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar
        class="bg-deep-purple-14 text-white glossy"
      >
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          icon="menu"
          aria-label="Menu"
        />

        <q-toolbar-title class="toolbar__title">
          Very Slow Board
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!-- User 기능 추가 시 메뉴 Open -->
    <!-- <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-2"
    >
      <q-list>
        <q-item clickable to="/board">
          <q-item-section>
            <q-item-label>Board</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable to="/user">
          <q-item-section>
            <q-item-label>User</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer> -->

    <q-page-container class="bg-grey-2">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'MyLayout',

  data () {
    return {
      leftDrawerOpen: false
    }
  }
}
</script>

<style lang="scss">
.toolbar__title {
  font-size: 16px;
  font-weight: 500;
}
</style>
