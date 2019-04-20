<template>
  <div>
    <div v-for="(row, index) in rowImages" :key="index" :style="{height: row.height + 'px'}" class="row-box">
      <progressive-image
        v-for="rimg in row.imgs"
        :key="rimg.id"
        :style="{left: rimg.displayPositionLeft + 'px'}"
        :tiny-thumbnail="$STATIC_URL_PREFIX + rimg.thumbnail32"
        :large-thumbnail="$STATIC_URL_PREFIX + rimg.thumbnail1024"
        :figure-width="rimg.displayWidth"
        :figure-height="rimg.displayHeight">
      </progressive-image>
    </div>
  </div>
</template>

<script>
import ProgressiveImage from '@/components/ProgressiveImage'
export default {
  name: 'EqualHeightImagesRow',
  data () {
    return {
      rowImages: [{
        h: 0,
        imgs: []
      }]
    }
  },
  props: {
    'images': Array,
    'rowWidth': Number
  },
  created () {
    const imagesToArrange = [...this.images]
    const paddingX = 4
    const rowWidth = this.rowWidth
    const maxRatio = 5
    const maxHeight = rowWidth / maxRatio
    while (imagesToArrange.length > 0) {
      const img = imagesToArrange.pop()
      const row = this.rowImages[this.rowImages.length - 1]
      row.imgs.push(img)
      let widthHeightRatio = 0
      row.imgs.forEach((rowImg) => {
        widthHeightRatio += rowImg.width / rowImg.height
      })
      row.height = rowWidth / widthHeightRatio
      if (row.height < maxHeight) {
        this.rowImages.push({
          h: 0,
          imgs: []
        })
      }
    }
    this.rowImages.forEach((row) => {
      let marginLeft = 0
      row.imgs.forEach((img) => {
        img.displayPositionLeft = marginLeft
        img.displayHeight = Math.min(row.height, maxHeight)
        img.displayWidth = (img.displayHeight * img.width / img.height) - paddingX
        marginLeft += (img.displayWidth + paddingX)
      })
    })
  },
  components: {
    'progressive-image': ProgressiveImage
  }
}
</script>

<style>
.row-box {
  position: relative;
  margin-bottom: 4px;
}
</style>
