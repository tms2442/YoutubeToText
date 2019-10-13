<template>
  <div class="home">
    <ToText msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ToText from '@/components/ToText.vue'

export default {
  name: 'home',
  components: {
    ToText
  }
}
</script>
