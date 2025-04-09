<template>
  <div class="container">
    <h1 class="title animate__animated animate__bounce">ВАШ ЛИСТ ДЛЯ ПОКУПОК</h1>
    <p class="mini-app-text">Это Telegram Mini App для списка покупок</p>

    <!-- Картинка с тенью по контуру -->
    <img src="/images/shopping-cart.png" alt="Корзина покупок" class="plain-image" />
  </div>

  <div class="btn-container">
    <NuxtLink to="/home-page" class="btn">Открыть списки покупок</NuxtLink>
    <NuxtLink to="/product-cards" class="btn">Продуктовые карты</NuxtLink>
  </div>
</template>

<script setup>
import 'animate.css';
</script>

<style scoped>
.mini-app-text {
  font-family: 'Exo 2', sans-serif;
  font-size: 22px;
  font-weight: 500;
  color: #ffc402;
  text-align: center;
}

.title {
  font-family: 'Exo 2', sans-serif;
  font-size: 37px;
  font-weight: 600;
  color: #eaffda;
  text-align: center;
  text-shadow: 5px 5px 10px rgba(48, 0, 38, 0.247);
}

/* Картинка с тенью по контуру */
.plain-image {
  max-width: 260px;
  width: 100%;
  height: auto;
  display: block;
  margin: 75px auto;
  filter: drop-shadow(0 9px 16px rgb(4, 19, 64)); /* Тень по контуру изображения */
}

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

.container {
  max-width: 600px;
  margin: 100 auto;
  padding: 40px;
  text-align: center;
  border-radius: 15px;
  position: relative;
}

h1 {
  font-size: 36px;
  color: #fdffd3;
  text-shadow: 5px 15px 20px rgba(27, 5, 45, 0.993);
  margin-bottom: 10px;
}

/* Стеклянные кнопки */
.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: rgba(255, 255, 255, 0.1);
  color: rgb(255, 254, 235);
  text-decoration: none;
  border-radius: 10px;
  margin-top: 20px;
  transition: background-color 0.3s ease;
  font-size: 16px;
  font-weight: 600;
  width: 100%;
  max-width: 300px;
  text-align: center;
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(5px);
}

.btn:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.btn-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: fixed;
  bottom: 130px;
  left: 50%;
  transform: translateX(-50%);
}

.btn + .btn {
  margin-top: 30px;
}
</style>
