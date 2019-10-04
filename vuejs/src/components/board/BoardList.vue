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
          key="writer"
          :props="props"
          v-text="props.row.writer"
        ></q-td>
        <q-td
          key="writer"
          :props="props"
          v-text="props.row.createDttm"
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
export default {
  data () {
    return {
      columns: [
        { name: 'title', align: 'center', label: '제목', field: 'title', sortable: true },
        { name: 'writer', align: 'center', label: '작성자', field: 'writer', sortable: true },
        { name: 'createDttm', align: 'center', label: '작성일', field: 'createDttm', sortable: true },
        { name: 'event', align: 'center', label: '', field: 'event', sortable: false }
      ],
      postList: [
        {
          id: 1,
          title: '안녕하세요?',
          writer: 'hayoung',
          createDttm: '2019-10-04'
        },
        {
          id: 2,
          title: '안녕하세요??',
          writer: 'hayoung',
          createDttm: '2019-10-04'
        },
        {
          id: 3,
          title: '안녕하세요???',
          writer: 'hayoung',
          createDttm: '2019-10-04'
        },
        {
          id: 4,
          title: '안녕하세요????',
          writer: 'hayoung',
          createDttm: '2019-10-04'
        }
      ]
    }
  },

  methods: {
    editPost (post) {
      console.log('editPost event')
    },

    deletePost (post) {
      console.log('deletePost event')
    }
  }
}
</script>
