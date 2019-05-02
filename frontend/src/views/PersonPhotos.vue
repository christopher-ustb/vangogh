<template>
  <div>
    <div>
      <md-avatar>
        <img v-if="person.coverFace" :src="$STATIC_URL_PREFIX + person.coverFace.image_path" alt="Avatar">
      </md-avatar>
      <md-field>
        <label>name</label>
        <md-input v-model="person.name"></md-input>
        <a @click="updateName">
          <md-icon>done</md-icon>
        </a>
      </md-field>
    </div>
    <scroll-master @on-bottom="loadMoreFaces" :offset="400">
      <equal-height-images-row
        v-if="personFacePhotos.length"
        :images="personFacePhotos"
        :row-width="1000"
      ></equal-height-images-row>
    </scroll-master>
  </div>
</template>

<script>
import ScrollMaster from '@/components/ScrollMaster'
import EqualHeightImagesRow from '@/components/EqualHeightImagesRow'
export default {
  name: 'PersonPhotos',
  data () {
    return {
      person: {
        id: this.$route.params.id
      },
      personFacePhotos: []
    }
  },
  created () {
    this.$http.get(
      this.$API_URL_PREFIX + '/api/people/' + this.$route.params.id + '/'
    ).then(function (resp) {
      if (resp.ok) {
        const p = resp.body
        p.coverFace = null
        this.person = p
      }
    }).then(function () {
      if (this.person.cover_face_id) {
        return this.$http.get(
          this.$API_URL_PREFIX + '/api/faces/' + this.person.cover_face_id + '/'
        )
      }
    }).then(function (faceResp) {
      this.person.coverFace = faceResp.body
    })
    this.loadMoreFaces()
  },
  methods: {
    updateName () {
      this.$http.put(this.$API_URL_PREFIX + '/api/people/' + this.$route.params.id + '/', {
        name: this.person.name
      })
    },
    loadMoreFaces () {
      this.$http.get(
        this.$API_URL_PREFIX + '/api/people/' + this.$route.params.id + '/faces/'
      ).then(function (resp) {
        if (resp.ok) {
          // TODO turn page
          this.personFacePhotos.push(...resp.body.results.map((face) => {
            return face.photo
          }))
        }
      })
    }
  },
  components: {
    'scroll-master': ScrollMaster,
    'equal-height-images-row': EqualHeightImagesRow
  }
}
</script>
