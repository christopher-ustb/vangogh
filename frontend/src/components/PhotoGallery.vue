<template>
  <md-app>
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
    <md-app-content>
      <gallery :images="photos" :index="index" @close="index = null"></gallery>
      <div
        class="image"
        v-for="(image, imageIndex) in photos"
        :key="imageIndex"
        @click="index = imageIndex"
        :style="{ backgroundImage: 'url(' + image + ')', width: '300px', height: '200px' }"
      ></div>
    </md-app-content>
  </md-app>
</template>

<script>
import VueGallery from 'vue-gallery'
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
      this.photos = resp.body.results.map(p => { return this.$STATIC_URL_PREFIX + p.thumbnail })
    })
  },
  components: {
    'gallery': VueGallery
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
