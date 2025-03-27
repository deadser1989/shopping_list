<template>
  <div>
		<slot />
	</div>

  <div class="container">
    <h1>Мой список покупок</h1>
    <p v-if="userName"> {{ userName }}!</p>

    <div class="form-container">
      <label for="new-item">Новый продукт:</label>
      <input
        type="text"
        id="new-item"
        v-model="newItem"
        placeholder="Название продукта"
        @keyup.enter="addItem"
      />
      <button @click="addItem">Добавить</button>
    </div>

    <div class="list-container">
      <h2>Добавленные продукты:</h2>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }}
          <button @click="removeItem(item.id)" class="remove-button">Удалить</button>
        </li>
      </ul>
      <p v-if="items.length === 0">Список пуст.</p>
    </div>

    <!-- Кнопка "Назад" -->
    <NuxtLink to="/" class="back-btn">← На главный экран</NuxtLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const newItem = ref('');
const items = ref([]);
const userName = ref('');

const addItem = () => {
  if (newItem.value.trim()) {
    items.value.push({ id: Date.now(), name: newItem.value.trim() });
    newItem.value = '';
  }
};

const removeItem = (id) => {
  items.value = items.value.filter(item => item.id !== id);
};

onMounted(() => {
  if (window.Telegram && window.Telegram.WebApp) {
    window.Telegram.WebApp.ready();
    console.log('Telegram Web App SDK initialized');

    const user = window.Telegram.WebApp.initDataUnsafe?.user;
    if (user) {
      userName.value = user.first_name;
      console.log('User ID:', user.id);
      console.log('User first name:', user.first_name);

      const themeParams = window.Telegram.WebApp.themeParams;
      console.log("Theme Params:", themeParams);
      if (themeParams.bg_color) {
          document.body.style.backgroundColor = themeParams.bg_color;
          console.log(document.body.style.backgroundColor);
      }
    } else {
      console.warn('Не удалось получить информацию о пользователе.');
    }

    window.Telegram.WebApp.MainButton.text = 'Сохранить';
    window.Telegram.WebApp.MainButton.onClick(() => {
      const data = JSON.stringify(items.value);
      window.Telegram.WebApp.sendData(data);
    });
    window.Telegram.WebApp.MainButton.show();
  } else {
    console.warn('Telegram Web App SDK not available');
  }
});
</script>

<style scoped>

.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  width: 100%;
}

label {
  margin-bottom: 5px;
}

body {
  background-color: #ff6bfa !important;
}

input {
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}

button {
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  align-self: flex-start;
}

button:hover {
  background-color: #3e8e41;
}

.list-container {
  width: 100%;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border: 1px solid #eee;
  margin-bottom: 5px;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.remove-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.remove-button:hover {
  background-color: #da190b;
}

.back-btn {
  display: inline-block;
  margin-top: 15px;
  color: blue;
  text-decoration: none;
}

.back-btn:hover {
  text-decoration: underline;
}
</style>
