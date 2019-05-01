import Vue from 'vue'
import Router from 'vue-router'
import PhotoGallery from '@/components/PhotoGallery'
import PeopleList from '@/components/PeopleList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'PhotoGallery',
      component: PhotoGallery
    },
    {
      path: '/people',
      name: 'PeopleList',
      component: PeopleList
    },
    {
      path: '/places',
      name: 'PeopleList',
      component: PeopleList
    },
    {
      path: '/albums',
      name: 'PeopleList',
      component: PeopleList
    }
  ]
})
