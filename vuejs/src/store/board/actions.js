/**
 * actions : 비동기 로직 작성
 */
import { board } from '@service'

const actions = {
  FETCH_POST_LIST ({ commit }) {
    board.fetch()
      .then(res => {
        commit('SET_POST_LIST', res.items)
      })
  }
}
export default actions
