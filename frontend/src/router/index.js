import Vue from 'vue'
import Router from 'vue-router'
import TestDraft from '@/components/TestDraft'
import AllPhoto from '@/views/AllPhoto'
import PersonPhotos from '@/views/PersonPhotos'
import PeopleList from '@/views/PeopleList'
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
          path: 'person/:id',
          name: 'PersonPhotos',
          component: PersonPhotos
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
    },
    {
      path: '/test',
      component: TestDraft
    }
  ]
})
