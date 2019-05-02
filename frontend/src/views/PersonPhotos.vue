<template>
  <div>
    <div>
      <md-avatar>
        <img v-if="person.coverFace" :src="$STATIC_URL_PREFIX + person.coverFace.image_path" alt="Avatar">
      </md-avatar>
      <!-- <span>{{ person.name }}</span> -->
      <md-field>
        <label>name</label>
        <md-input v-model="person.name"></md-input>
        <a @click="updateName">
          <md-icon>done</md-icon>
        </a>
      </md-field>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PersonPhotos',
  data () {
    return {
      person: {
        id: this.$route.params.id
      }
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
  },
  methods: {
    updateName () {
      this.$http.put(this.$API_URL_PREFIX + '/api/people/' + this.$route.params.id + '/', {
        name: this.person.name
      })
    }
  }
}
</script>
