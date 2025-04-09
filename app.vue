<template>
  <NuxtLayout>
    <div class="background">
      <Header />
      <NuxtPage />
      <Footer />
    </div>
  </NuxtLayout>
</template>

<script setup>
import { useHead } from '@vueuse/head'

useHead({
  script: [
    {
      src: 'https://telegram.org/js/telegram-web-app.js',
      async: true,
    },
  ],
})
</script>

<script>
import 'animate.css'
</script>

<style>
@import url("animate.css");

html, body {
  margin: 0;
  padding: 0;
  font-family: 'Open Sans', 'Roboto', 'Montserrat', sans-serif;
  color: white;
  background: transparent;
  min-height: 100vh;
}

/* Фон страницы с градиентом, растягивающийся на весь экран */
.background {
  min-height: 100vh;
  background: linear-gradient(135deg, #005a78, #4f0080); /* Градиент для всей страницы */
  background-size: cover; /* Растягиваем градиент на весь экран */
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
  overflow-x: hidden;
}

/* Контейнер без фона - полностью прозрачный */
.container {
  max-width: 700px;
  width: 100%;
  padding: 20px;
  margin: 0 auto;
  background: transparent; /* Прозрачный фон */
  box-sizing: border-box;
  color: white;
}

/* Глобальный стеклянный стиль кнопок */
.glass-button {
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.28);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: white;
  padding: 12px 24px;
  transition: all 0.3s ease;
  font-weight: 600;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  cursor: pointer;
}

.glass-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

/* Адаптивные заголовки */
h1, h2, h3 {
  text-align: center;
  margin: 20px 0;
}

/* Кнопки иконок */
.icon-btn {
  width: 30px;
  height: 30px;
  padding: 0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Адаптивность */
@media (max-width: 600px) {
  .glass-button {
    padding: 10px 16px;
    font-size: 14px;
  }

  .container {
    padding: 15px;
  }
}
</style>
