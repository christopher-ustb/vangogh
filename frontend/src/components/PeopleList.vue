<template>
  <ul>
    <li v-for="p in people" :key="p.id">{{ p.name }}</li>
  </ul>
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
      this.people = resp.body.results
    })
  }
}
</script>
