<template>
  <div class="backdrop" @click.self="closeThisModal">
    <div class="modal" :class="{ dark:theme }">
      <slot>default content</slot>
      <div class="actions">
        <slot name="links"></slot>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['theme'],
  methods: {
    closeThisModal(){
      this.$emit('close');
    }
  }
}
</script>
<style>
.actions {
  display: flex;
  justify-content: center;
  text-align: center;
  margin: 30px 0 10px 0;
}
.actions a {
  color: #333;
  padding: 8px;
  border: 1px solid #eee;
  border-radius: 4px;
  text-decoration: none;
  margin: 10px;
}
.actions a:hover {
  background: #c047e2;
  color: #fff;
}
</style>