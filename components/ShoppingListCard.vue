<template>
    <div class="shopping-list-card">
      <p class="list-name">🛒 {{ list.name }}</p>
    </div>
  </template>
  
  <script setup>
  defineProps({
    list: Object
  })
  </script>
  
  <style scoped>
  .shopping-list-card {
    width: 90%;
    max-width: 400px;
    background: linear-gradient(135deg, #6a31b4, #7930cd);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: transform 0.2s ease;
    animation: fadeInUp 0.3s ease;
  }
  .shopping-list-card:hover {
    transform: scale(1.05);
  }
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  </style>