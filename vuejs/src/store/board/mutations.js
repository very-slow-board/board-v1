/**
 * vuex의 state는 mutations에서만 변경이 이루어져야 함
 */
const mutations = {
  SET_POST_LIST (state, postList) {
    state.postList = postList
  }
}

export default mutations
