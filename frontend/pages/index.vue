<template>
  <div class="container">
    <nav
      class="navbar navbar-expand-lg navbar-dark justify-content-between"
    >
      <a
        class="navbar-brand text-white"
        href=""
      >
        Youtube Api
      </a>
      <!--b-navbar-nav>
        <b-nav-item>
          <b-button
            variant="outline-light"
            size="lg"
            :disabled="isRunning"
            @click="startServer()"
          >
            Start Server
          </b-button>
        </b-nav-item>
      </b-navbar-nav-->
      <div style="margin-left:auto; margin-right:0;">
        <b-button
          variant="outline-light"
          size="sm"
          :disabled="!isRunning"
          @click="fetchVideos()"
        >
          Refresh Videos
        </b-button>
      </div>
    </nav>
    <Youtube
      :videos="videos"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Youtube from '~/components/Youtube.vue'

export default {
  components: {
    Youtube
  },
  data () {
    return {
      videos: []
    }
  },
  computed: {
    ...mapState({
      isRunning: state => state.youtube.isRunning
    })
  },
  methods: {
    async fetchVideos () {
      const value = await this.$store.dispatch('youtube/refresh_video_store')
      if (value instanceof Error) {
        this.videos = []
      } else {
        this.videos = this.$store.getters['youtube/get_videos']
      }
    },
    async startServer () {
      await this.$store.dispatch('youtube/start_server')
    }
  }
}
</script>

<style>
</style>
