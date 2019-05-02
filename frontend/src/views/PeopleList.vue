<template>
<div>
  <div class="md-layout">
    <div v-for="p in people" :key="p.id" class="md-layout-item md-medium-size-12 md-small-size-17 md-xsmall-size-25">
      <router-link :to="'/person/' + p.id">
        <img v-if="p.coverFace" :src="$STATIC_URL_PREFIX + p.coverFace.image_path" style="width: 100%">
        <span>{{ p.name }}</span>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'PeopleList',
  data () {
    return {
      people: []
    }
  },
  created () {
    this.$http.get(this.$API_URL_PREFIX + '/api/people/').then(function (resp) {
      const repsPeopleResults = resp.body.results
      repsPeopleResults.map((p) => {
        p.coverFace = null
      })
      this.people = repsPeopleResults
      this.people.forEach((p) => {
        if (p.cover_face_id) {
          this.$http.get(
            this.$API_URL_PREFIX + '/api/faces/' + p.cover_face_id + '/'
          ).then(function (faceResp) {
            p.coverFace = faceResp.body
          })
        } else {
          p.coverFace = {}
        }
      })
    })
  }
}
</script>

<style scoped>
.person-avatar-img {
  width: 100%;
}
</style>
