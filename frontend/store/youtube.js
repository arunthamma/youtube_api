/* eslint-disable */
export const getters = {
  get_videos: state => state.video_store
}

export const actions = {
  async refresh_video_store ({ commit }) {
    await this.$axios.get('/get_video_data/')
      .then((res) => {
        if (res.status === 200) {
          commit('setVideoStore', res.data)
        }
      })
  },
  async start_server ({ commit }) {
    await this.$axios.post('/publishData/')
      .then((res) => {
        if (res.status === 200) {
          commit('setRunningState')
        }
      })
  }
}

export const mutations = {
  setVideoStore (state, responseData) {
    state.video_store = responseData
  },
  setRunningState (state) {
    state.isRunning = true
  }
}

export const state = () => ({
  video_store: [],
  isRunning: false
})
