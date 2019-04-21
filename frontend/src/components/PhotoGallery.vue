<template>
  <div style="width: 1350px">
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
      <infi-scroll-images-show-window></infi-scroll-images-show-window>
    <!-- </md-app-content>
  </md-app> -->
  </div>
</template>

<script>
import InfiScrollImagesShowWindow from '@/components/InfiScrollImagesShowWindow'
export default {
  name: 'PhotoGallery',
  data () {
    return {
    }
  },
  created () {
  },
  components: {
    'infi-scroll-images-show-window': InfiScrollImagesShowWindow
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
