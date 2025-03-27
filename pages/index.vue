<template>
  <div class="container">
    <h1 class="animate__animated animate__bounce">ВАШ ЛИСТ ДЛЯ ПОКУПОК</h1>
    <p>Это Telegram Mini App для списка покупок.</p>

    <!-- Кнопка для перехода к списку покупок -->
    <NuxtLink to="/shopping-list" class="btn">Открыть список покупок</NuxtLink>
  </div>
</template>

<script setup>
import 'animate.css'; 
</script>

<script>
import '@/assets/css/main.css'
</script>


<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  margin-top: 20px;
}

.btn:hover {
  background-color: #45a049;
}
</style>
