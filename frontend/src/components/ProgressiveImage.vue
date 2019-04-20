<template>
  <figure :style="{width: figureWidth + 'px', height: figureHeight + 'px'}"
    v-on:scroll="checkViewportToLoad"
    @click="checkViewportToLoad"
    class="pgsv-image">
    <img :src="tinyThumbnail">
    <img v-if="loaded" :src="largeThumbnail">
  </figure>
</template>

<script>
export default {
  name: 'ProgressiveImage',
  data () {
    return {
      // TODO load when needed
      loaded: true
    }
  },
  props: [
    'figureWidth', 'figureHeight',
    'tinyThumbnail', 'largeThumbnail'
  ],
  methods: {
    loadLarge () {
      setTimeout(() => {
        this.loaded = true
      }, 1000)
    },
    checkViewportToLoad () {
      let rect = this.$el.getBoundingClientRect()
      console.log(rect)
    }
  }
}
</script>

<style>
figure {
    display: block;
    margin-block-start: 0;
    margin-block-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
}
.pgsv-image {
  position: absolute;
  left: 0;
  top: 0;
  overflow: hidden;
}
.pgsv-image img {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  opacity: 1;
  transition: 1s ease opacity;
  -webkit-transition: 1s ease opacity;
}
</style>
