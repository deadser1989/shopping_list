<template>
    <div class="modal-backdrop" @click.self="$emit('close')">
      <div class="modal">
        <h3>Название нового списка</h3>
        <input v-model="name" placeholder="Введите название" />
        <button @click="createList">Создать</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  const emit = defineEmits(['close', 'create'])
  const name = ref('')
  
  const createList = () => {
    if (name.value.trim()) {
      emit('create', name.value)
      emit('close')
    }
  }
  </script>
  
  <style scoped>
  .modal-backdrop {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal {
    background: white;
    padding: 20px;
    border-radius: 12px;
    width: 90%;
    max-width: 400px;
  }
  input {
    width: 100%;
    margin-top: 10px;
    padding: 8px;
  }
  button {
    margin-top: 10px;
  }
  </style>