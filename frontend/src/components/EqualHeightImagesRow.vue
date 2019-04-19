<template>
  <div>
    <progressive-image
      v-for="rimg in rowImages"
      :key="rimg.id"
      :style="{left: 0}"
      :tiny-thumbnail="$STATIC_URL_PREFIX + rimg.thumbnail32"
      :large-thumbnail="$STATIC_URL_PREFIX + rimg.thumbnail1024"
      figure-width="200" figure-height="150">
    </progressive-image>
  </div>
</template>

<script>
import ProgressiveImage from '@/components/ProgressiveImage'
export default {
  name: 'EqualHeightImagesRow',
  data () {
    return {
      rowImages: []
    }
  },
  props: [
    'images'
  ],
  created () {
    const rowWidth = 1000
    const maxHeight = 200
    let height = 999999
    while (height > maxHeight) {
      const img = this.images.pop()
      this.rowImages.push(img)
      let widthHeightRatio = 0
      this.rowImages.forEach((rowImg) => {
        widthHeightRatio += rowImg.width / rowImg.height
      })
      height = rowWidth / widthHeightRatio
    }
  },
  components: {
    'progressive-image': ProgressiveImage
  }
}
</script>
