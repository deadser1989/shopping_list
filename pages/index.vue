<template>
  <div class="container">
    <h1 class="title animate__animated animate__bounce">ВАШ ЛИСТ ДЛЯ ПОКУПОК</h1>
    <p class="mini-app-text">Это Telegram Mini App для списка покупок</p>
  </div>

  <!-- Кнопки для перехода на страницы, размещенные внизу -->
  <div class="btn-container">
    <NuxtLink to="/home-page" class="btn">Открыть списки покупок</NuxtLink>
    <NuxtLink to="/product-cards" class="btn">Продуктовые карты</NuxtLink>
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
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

/* Контейнер */
.container {
  max-width: 600px;
  margin: 100 auto;
  padding: 40px;
  text-align: center;
  border-radius: 15px;
  position: relative; /* Позволяет позиционировать кнопки относительно контейнера */
}

/* Заголовок */
h1 {
  font-size: 36px;
  color: #fdffd3;
  text-shadow: 5px 5px 10px rgba(41, 7, 35, 0.993);
  margin-bottom: 10px;
}

/* Стеклянные кнопки */
.btn {
  display: inline-block;
  padding: 10px 20px; /* Уменьшаем ширину кнопок */
  background-color: rgba(255, 255, 255, 0.1); /* Легкий стеклянный эффект */
  color: rgb(255, 254, 235);
  text-decoration: none;
  border-radius: 10px;
  margin-top: 20px;
  transition: background-color 0.3s ease;
  font-size: 16px; /* Уменьшение размера шрифта */
  font-weight: 600;
  width: 100%; /* Кнопки одинакового размера */
  max-width: 350px; /* Уменьшаем максимальную ширину кнопок */
  text-align: center; /* Центрируем текст */
  backdrop-filter: blur(5px); /* Легкое размытие фона для стеклянного эффекта */
  -webkit-backdrop-filter: blur(5px); /* Для браузеров, поддерживающих webkit */
}

.btn:hover {
  background-color: rgba(255, 255, 255, 0.2); /* Сделаем немного более мутными при наведении */
}

/* Фиксированное позиционирование кнопок внизу экрана */
.btn-container {
  width: 100%;
  display: flex;
  flex-direction: column; /* Размещение кнопок друг под другом */
  align-items: center;
  position: fixed;
  bottom: 110px; /* Поднимаем кнопки чуть выше */
  left: 50%;
  transform: translateX(-50%);
}

/* Отступ между кнопками */
.btn + .btn {
  margin-top: 25px; /* Увеличиваем отступ между кнопками */
}
</style>
