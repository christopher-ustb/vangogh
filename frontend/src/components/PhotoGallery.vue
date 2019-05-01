<template>
  <md-app>
    <md-app-toolbar md-mode="fixed" class="md-primary">
        <h1 class="md-title">Vangogh</h1>
    </md-app-toolbar>
    <md-app-drawer md-persistent="mini">
      <div class="menu-item-box">
        <router-link to="/">
          <a>
            <md-icon>photo</md-icon>
            <div>照片</div>
          </a>
        </router-link>
      </div>
      <div class="menu-item-box">
        <router-link to="/people">
          <a>
            <md-icon>people</md-icon>
            <div>人物</div>
          </a>
        </router-link>
      </div>
      <div class="menu-item-box">
        <router-link to="/places">
          <a>
            <md-icon>place</md-icon>
            <div>地点</div>
          </a>
        </router-link>
      </div>
      <div class="menu-item-box">
        <router-link to="/albums">
          <a>
            <md-icon>photo_album</md-icon>
            <div>专辑</div>
          </a>
        </router-link>
      </div>
    </md-app-drawer>
    <md-app-content>
      <infi-scroll-images-show-window></infi-scroll-images-show-window>
    </md-app-content>
  </md-app>
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
.menu-item-box {
  text-align: center;
  padding-top: 20px;
  padding-bottom: 20px;
}
</style>
