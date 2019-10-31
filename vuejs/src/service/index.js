import axios from 'axios'

const domain = 'http://localhost:8000/api'

const request = {
  get (path) {
    return axios.get(`${domain + path}/?format=json`)
  },

  put (path, data) {
    return axios.put(`${domain + path}`, data)
  },

  post (path, data) {
    return axios.post(`${domain + path}`, data)
  }
}

export const board = {
  fetch () {
    return request.get('/boards')
      .then(({ data }) => data)
  }
}
