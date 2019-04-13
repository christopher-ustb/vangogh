import Vue from 'vue'
import Router from 'vue-router'
import PhotoGallery from '@/components/PhotoGallery'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'PhotoGallery',
      component: PhotoGallery
    }
  ]
})
