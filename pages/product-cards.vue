<template>
  <div class="container">
    <!-- Кнопка для перехода на главную страницу -->
    <NuxtLink to="/home-page" class="home-btn">🏠</NuxtLink>

    <h1 class="title animate__animated animate__bounce">ПРОДУКТОВЫЕ КАРТЫ</h1>
    <p class="mini-app-text">Добавьте продуктовые карты для магазинов</p>

    <div class="buttons-container">
      <!-- Кнопка добавления карты (пока не рабочая) -->
      <button @click="addProductCard" class="create-btn">
        <span class="plus">+</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Функция для добавления продуктовой карты (пока не рабочая)
const addProductCard = () => {
  alert("Функция добавления карты еще не работает");
};
</script>

<style scoped>
/* Общий стиль текста */
.mini-app-text {
  font-family: 'Exo 2', sans-serif;
  font-size: 22px;
  font-weight: 500;
  color: #ffc402;
  text-align: center;
}

/* Специальные стили для заголовка */
.title {
  font-family: 'Exo 2', sans-serif;
  font-size: 37px;
  font-weight: 600;
  color: #eaffda;
  text-align: center;
  text-shadow: 2px 2px 5px rgba(48, 0, 38, 0.247);
}

/* Фон для всей страницы */
body {
  background: linear-gradient(to bottom right, #005a78, #4f0080);
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
  text-shadow: 5px 5px 10px rgba(41, 7, 35, 0.993);
  margin-bottom: 10px;
}

/* Кнопка "Домой" */
.home-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  font-size: 30px;
  color: white;
  text-decoration: none;
  background-color: transparent;
  border: none;
  cursor: pointer;
  transition: color 0.3s;
}

.home-btn:hover {
  color: #fdffd3;
}

/* Кнопки добавления и редактирования */
.buttons-container {
  position: fixed;
  bottom: 30px;
  right: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.create-btn {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  font-size: 32px;
  color: white;
  border: none;
  margin-bottom: 15px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.create-btn {
  background-color: #00aa88;
}

.create-btn:hover {
  background-color: #00856d;
}

.plus {
  font-size: 40px;
}
</style>
