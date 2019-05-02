<template>
  <div>
    <div>
      <md-avatar>
        <img :src="$STATIC_URL_PREFIX + person.url" alt="Avatar">
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
    this.$http.get(this.$API_URL_PREFIX + '/api/people/' + this.$route.params.id).then(function (resp) {
      if (resp.ok) {
        this.person = resp.body
      }
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
