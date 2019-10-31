<template>
  <q-table
    :columns="columns"
    :data="postList"
  >
    <template v-slot:body="props">
      <q-tr
        :props="props"
        class="cursor-point"
      >
        <q-td
          key="title"
          :props="props"
          v-text="props.row.title"
        ></q-td>
        <q-td
          key="event"
          :props="props"
          class="text-grey-8 q-gutter-xs"
        >
          <q-btn
            size="10px"
            flat
            round
            dense
            icon="fas fa-ellipsis-v"
          >
            <q-menu>
              <q-list>
                  <q-item
                  clickable
                  v-close-popup
                  @click.native="editPost(props.row)"
                >
                  <q-item-section>편집</q-item-section>
                </q-item>
                <q-item
                  clickable
                  v-close-popup
                  @click.native="deletePost(props.row)"
                >
                  <q-item-section>삭제</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data () {
    return {
      columns: [
        { name: 'title', align: 'center', label: '제목', field: 'title', sortable: true },
        { name: 'event', align: 'center', label: '', field: 'event', sortable: false }
      ]
      // postList: []
    }
  },

  computed: {
    ...mapState('board', {
      postList: state => state.postList
    })
  },

  methods: {
    ...mapActions('board', [
      'FETCH_POST_LIST'
    ]),

    fetch () {
      this.FETCH_POST_LIST()
    },

    editPost (post) {
      console.log('editPost event')
    },

    deletePost (post) {
      console.log('deletePost event')
    }
  },

  created () {
    this.fetch()
  }
}
</script>
