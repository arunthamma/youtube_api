<template>
  <div class="mt-4 videos">
    <div v-for="video in videos" :key="video.video_tag">
      <b-row
        class="mb-2"
      >
        <b-card no-body class="overflow-hidden" style="width: 800px;">
          <b-row no-gutters>
            <b-col md="3">
              <a :href="video.video_url">
                <b-card-img :src="video.thumbnail" class="rounded-0" />
              </a>
            </b-col>
            <b-col md="9">
              <b-card-body :title="video.video_title">
                <b-card-text>
                  <small>{{ video.video_description }}</small>
                </b-card-text>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
      </b-row>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    videos: {
      type: Array
    }
  }
}
</script>
<style>
</style>
