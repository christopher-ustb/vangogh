<template>
  <div>
    <slot/>
  </div>
</template>

<script>
import {debounce} from 'lodash'

export default {
  props: {
    debounce: {
      type: Number,
      default: 200
    },
    offset: {
      type: Number,
      default: 0
    }
  },
  data () {
    return {
      handleOnScroll: undefined,
      scrollDirection: 'down'
    }
  },
  created () {
    this.pageYOffset = 0
    if (this.debounce) {
      this.handleOnScroll = debounce(this._handleOnScroll.bind(this), this.debounce, { trailing: true })
    } else {
      this.handleOnScroll = this._handleOnScroll.bind(this)
    }
  },
  mounted () {
    document.addEventListener('scroll', this.handleOnScroll)
    this.handleOnScroll()
  },
  destroyed () {
    document.removeEventListener('scroll', this.handleOnScroll)
  },
  methods: {
    _handleOnScroll () {
      this.scrollDirection = window.pageYOffset > this.pageYOffset ? 'down' : 'up'
      this.pageYOffset = window.pageYOffset
      const scrollNode = document.scrollingElement || document.documentElement
      if (scrollNode.scrollHeight - this.offset <= scrollNode.scrollTop + window.innerHeight) {
        this.$emit('on-bottom')
      }
    }
  }
}
</script>

<style>

</style>
