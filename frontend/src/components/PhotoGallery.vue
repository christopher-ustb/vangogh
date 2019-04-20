<template>
  <div>
  <!-- <md-app>
    <md-app-toolbar md-mode="fixed" class="md-primary">
        <h1 class="md-title">Vangogh</h1>
        <md-input placeholder="search"></md-input>
        <md-button>上传</md-button>
    </md-app-toolbar>
    <md-app-drawer md-persistent="mini">
      <div>照片</div>
      <div>人物</div>
      <div>地点</div>
      <div>专辑</div>
    </md-app-drawer>
    <md-app-content> -->
      <equal-height-images-row v-if="photos.length" :images="photos" :row-width="1200">
      </equal-height-images-row>
    <!-- </md-app-content>
  </md-app> -->
  </div>
</template>

<script>
import EqualHeightImagesRow from '@/components/EqualHeightImagesRow'
export default {
  name: 'PhotoGallery',
  data () {
    return {
      photos: [],
      index: null
    }
  },
  created () {
    this.$http.get(this.$API_URL_PREFIX + '/api/photos/').then(function (resp) {
      this.photos = resp.body.results
    })
  },
  components: {
    'equal-height-images-row': EqualHeightImagesRow
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.image {
    float: left;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    border: 1px solid #ebebeb;
    margin: 5px;
  }
</style>
