import Vue from 'vue'
import Router from 'vue-router'
import AllPhoto from '@/views/AllPhoto'
import PeopleList from '@/components/PeopleList'
import BasicLayout from '@/layouts/BasicLayout'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: BasicLayout,
      children: [
        {
          path: '',
          name: 'AllPhoto',
          component: AllPhoto
        },
        {
          path: 'people',
          name: 'PeopleList',
          component: PeopleList
        },
        {
          path: 'places',
          name: 'PlaceList',
          component: PeopleList
        },
        {
          path: 'albums',
          name: 'AlbumList',
          component: PeopleList
        }
      ]
    }
  ]
})
