<template>
  <div>
    <md-field>
      <label>name</label>
      <md-input v-model="name"></md-input>
    </md-field>
  </div>
</template>

<script>
export default {
  name: 'TestDraft',
  data () {
    return {
      name: 'x'
    }
  }
}
</script>
