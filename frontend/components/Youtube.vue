<template>
  <div class="mt-3 videos">
    <div v-for="video in videos" :key="video.video_tag">
      <b-row
        class="mb-2"
      >
        <b-card no-body class="overflow-hidden" style="width: 800px;">
          <b-row no-gutters>
            <b-col md="3">
              <b-card-img :src="video.thumbnail" class="rounded-0" />
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
        <!--b-col class="col-2">
          <a :href="video.video_url">
            <b-img thumbnail :src="video.thumbnail" />
          </a>
        </b-col>
        <b-col class="col-8">
          <h6>{{ video.video_title }}</h6>
          <a><small>{{ video.video_description }}</small></a>
        </b-col-->
      </b-row>
    </div>
  </div>
</template>
<script>
export default {
  /* eslint-disable */
  props: ['videos'],
  data () {
    return {
    }
  }
}
</script>
<style>
</style>
