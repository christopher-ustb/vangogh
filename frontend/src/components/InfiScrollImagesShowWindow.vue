<template>
  <div ref="showWindow">
    <equal-height-images-row v-if="photos.length" :images="photos" :row-width="containerWidth">
    </equal-height-images-row>
  </div>
</template>

<script>
import EqualHeightImagesRow from '@/components/EqualHeightImagesRow'
export default {
  name: 'InfiScrollImagesShowWindow',
  data () {
    return {
      photos: [],
      scrollDirection: 'down'
    }
  },
  created () {
    this._loadMorePhotos()
    window.addEventListener('scroll', this.handleScroll)
    this.pageYOffset = 0
  },
  mounted () {
    this.containerWidth = this.$refs.showWindow.offsetWidth
  },
  methods: {
    handleScroll () {
      this.scrollDirection = window.pageYOffset > this.pageYOffset ? 'down' : 'up'
      this.pageYOffset = window.pageYOffset
      const scrollNode = document.scrollingElement || document.documentElement
      if (scrollNode.scrollHeight - 300 <= scrollNode.scrollTop + window.innerHeight) {
        if (this.nextPageUrl && !this.loading) {
          this._loadMorePhotos(this.nextPageUrl)
        }
      }
    },
    _loadMorePhotos (url) {
      url = url || (this.$API_URL_PREFIX + '/api/photos/')
      this.loading = true
      this.$http.get(url).then(function (resp) {
        if (resp.ok) {
          this.photos.push(...resp.body.results)
          this.nextPageUrl = resp.body.next
        }
        this.loading = false
      })
    }
  },
  components: {
    'equal-height-images-row': EqualHeightImagesRow
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>
