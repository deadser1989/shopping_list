<template>
  <div class="container">
    <h1 class="title animate__animated animate__bounce">ВАШ ЛИСТ ДЛЯ ПОКУПОК</h1>
    <p class="mini-app-text">Это Telegram Mini App для списка покупок</p>

    <!-- Кнопка для перехода на Home Page -->
    <NuxtLink to="/home-page" class="btn">Открыть списки покупок</NuxtLink>
  </div>
</template>

<script setup>
import 'animate.css'; 
</script>

<style scoped>
/* Общий стиль текста */
.mini-app-text {
  font-family: 'Exo 2', sans-serif; 
  font-size: 22px;
  font-weight: 500;
  color: #ffc814;
  text-align: center;
}

/* Специальные стили для заголовка */
.title {
  font-family: 'Exo 2', sans-serif; 
  font-size: 40px; 
  font-weight: 700;
  color: #eaffda; 
  text-align: center;
  text-shadow: 2px 2px 5px rgba(48, 0, 38, 0.247); 
}
</style>

<style>
/* Фон для всей страницы */
body {
  background: linear-gradient(to bottom right, #410076, #6a0065);
  font-family: 'Roboto', 'Open Sans', 'Montserrat', 'PT Sans', sans-serif;
  height: 100vh;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Контейнер */
.container {
  max-width: 600px;
  margin: 100 auto;
  padding: 40px;
  text-align: center;
  border-radius: 15px;
}

/* Заголовок */
h1 {
  font-size: 36px;
  color: #fdffd3;
  text-shadow: 1px 1px 3px rgba(54, 54, 54, 0.8);
  margin-bottom: 10px;
}

/* Кнопка */
.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #008db4;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  margin-top: 20px;
}

.btn:hover {
  background-color: #005e9d;
}
</style>
