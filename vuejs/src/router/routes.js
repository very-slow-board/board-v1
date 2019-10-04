import Layout from 'layouts/Mylayout.vue'
import Board from 'pages/Board.vue'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        component: Board
      }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
