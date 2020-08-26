<template>
  <div class="container">
    <div>
      <Logo />
      <h1 class="title">
        Youtube api
      </h1>
      <b-row>
        <b-col>
          <b-button
            :disabled="!isPolling"
            @click="startServer()"
          >
            Start server
          </b-button>
        </b-col>
        <b-col>
          <b-button
            :disabled="isPolling"
            @click="getVideos"
          >
            Refresh video store
          </b-button>
        </b-col>
      </b-row>
      <Youtube :videos="videos" />
      <!--div class="links">
        <a
          href="https://nuxtjs.org/"
          target="_blank"
          rel="noopener noreferrer"
          class="button--green"
        >
          Documentation
        </a>
        <a
          href="https://github.com/nuxt/nuxt.js"
          target="_blank"
          rel="noopener noreferrer"
          class="button--grey"
        >
          GitHub
        </a>
      </div-->
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import Youtube from '~/components/Youtube.vue'
export default {
  components: {
    Logo,
    Youtube
  },
  data () {
    return {
      videos: [],
      isPolling: true
    }
  },
  methods: {
    async getVideos () {
      const value = await this.$store.dispatch('youtube/refresh_video_store')
      if (value instanceof Error) {
        this.videos = []
      } else {
        this.videos = this.$store.getters['youtube/get_videos']
      }
      return true
    },
    async startServer () {
      await this.$store.dispatch('youtube/start_server')
      this.isPolling = false
    }
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
