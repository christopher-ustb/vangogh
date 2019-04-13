<template>
  <div>
    <!-- <img v-for="photo in photos" :key="photo.id" v-bind:src="'http://localhost:8000/static' + photo.thumbnail" style="width: 500px"> -->
    <gallery :images="photos" :index="index" @close="index = null"></gallery>
    <div
      class="image"
      v-for="(image, imageIndex) in photos"
      :key="imageIndex"
      @click="index = imageIndex"
      :style="{ backgroundImage: 'url(' + image + ')', width: '300px', height: '200px' }"
    ></div>
  </div>
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
    this.$http.get('http://localhost:8000/api/photos/').then(function (resp) {
      console.log(resp)
      this.photos = resp.body.results.map(p => { return 'http://localhost:8000/static' + p.thumbnail })
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
