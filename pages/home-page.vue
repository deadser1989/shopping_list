<template>
    <div class="home-container">
      <h1 class="title">Ваши списки покупок</h1>
  
      <!-- Список всех покупок -->
      <div class="lists-container">
        <div 
          v-for="list in shoppingLists" 
          :key="list.id" 
          class="shopping-list-card"
          @click="goToList(list.id)"
        >
          <p class="list-name">{{ list.name }}</p>
        </div>
      </div>
  
      <!-- Плавающая кнопка "Добавить" -->
      <div class="fab" @click="createNewList">
        <span class="tooltip">Создать новый список</span>
        <span class="plus">+</span>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  // Пример списков (в будущем можно загружать с сервера)
  const shoppingLists = ref([
    { id: 1, name: "Продукты на неделю" },
    { id: 2, name: "Купить для вечеринки" },
  ]);
  
  // Функция перехода в список
  const goToList = (id) => {
    router.push(`/shopping-list/${id}`);
  };
  
  // Функция создания нового списка
  const createNewList = () => {
    const newList = { id: Date.now(), name: `Новый список ${shoppingLists.value.length + 1}` };
    shoppingLists.value.push(newList);
  };
  </script>
  
  <style scoped>
  /* Основной контейнер */
  .home-container {
    padding: 20px;
    text-align: center;
  }
  
  /* Заголовок */
  .title {
    font-family: 'Exo 2', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 20px;
  }
  
  /* Контейнер для списков */
  .lists-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
  }
  
  /* Список покупок (карточка) */
  .shopping-list-card {
    width: 90%;
    max-width: 400px;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .shopping-list-card:hover {
    transform: scale(1.05);
    box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.3);
  }
  
  .list-name {
    font-size: 18px;
    font-weight: 600;
    color: #333;
  }
  
  /* Плавающая кнопка */
  .fab {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #008db4;
    color: white;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    cursor: pointer;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
    transition: background 0.2s ease, transform 0.2s ease;
  }
  
  .fab:hover {
    background: #005e9d;
    transform: scale(1.1);
  }
  
  /* Подсказка при наведении */
  .tooltip {
    position: absolute;
    right: 70px;
    background: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.2s ease;
  }
  
  .fab:hover .tooltip {
    opacity: 1;
    visibility: visible;
  }
  
  /* Иконка плюс */
  .plus {
    font-size: 32px;
    font-weight: bold;
  }
  </style>
  