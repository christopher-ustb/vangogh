<template>
  <md-app>
    <md-app-toolbar md-mode="fixed" class="md-primary">
        <h1 class="md-title">Vangogh</h1>
    </md-app-toolbar>
    <md-app-drawer md-persistent="mini">
      <div class="menu-item-box">
        <router-link to="/">
          <md-icon>photo</md-icon>
          <div>照片</div>
        </router-link>
      </div>
      <div class="menu-item-box">
        <router-link to="/people">
          <md-icon>people</md-icon>
          <div>人物</div>
        </router-link>
      </div>
      <div class="menu-item-box">
        <router-link to="/places">
          <md-icon>place</md-icon>
          <div>地点</div>
        </router-link>
      </div>
      <div class="menu-item-box">
        <router-link to="/albums">
          <md-icon>photo_album</md-icon>
          <div>专辑</div>
        </router-link>
      </div>
    </md-app-drawer>
    <md-app-content>
      <router-view></router-view>
    </md-app-content>
  </md-app>
</template>

<script>
export default {
  name: 'BasicLayout'
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
