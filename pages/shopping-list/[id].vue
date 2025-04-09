<template>
  <div class="container">
    <!-- Кнопка Назад -->
    <button class="floating-icon back-icon" @click="goBack">
      <ArrowLeft :size="20" />
    </button>

    <!-- Заголовок -->
    <h1 class="title">{{ listName || "Список покупок" }}</h1>

    <!-- Форма добавления продукта -->
    <div class="form-container">
      <label for="new-item">Новый продукт:</label>
      <input
        type="text"
        id="new-item"
        v-model="newItem"
        placeholder="Название продукта"
        @keyup.enter="addItem"
      />
      <button class="glass-button add-button" @click="addItem">Добавить</button>
    </div>

    <!-- Список продуктов -->
    <div class="list-container">
      <h2>Добавленные продукты:</h2>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }}
          <button @click="removeItem(item.id)" class="glass-button remove-button">Удалить</button>
        </li>
      </ul>
      <p v-if="items.length === 0">Список пуст.</p>
    </div>

    <!-- Кнопка Поделиться -->
    <button class="floating-icon share-icon" @click="shareList">
      <Share2 :size="20" />
    </button>

    <!-- Кнопка Пользователи -->
    <button class="floating-icon user-icon" @click="showUsers = true">
      <User :size="20" />
    </button>

    <!-- Модальное окно пользователей -->
    <div v-if="showUsers" class="modal-overlay" @click.self="showUsers = false">
      <div class="user-modal">
        <button class="close-btn" @click="showUsers = false">✖</button>
        <h3>Пользователи со списком:</h3>
        <p v-if="users.length === 0">Добавленных пользователей нет.</p>
        <ul>
          <li v-for="user in users" :key="user">{{ user }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { ArrowLeft, Share2, User } from 'lucide-vue-next';

const router = useRouter();
const route = useRoute();
const listId = route.params.id;

const listName = ref('');
const newItem = ref('');
const items = ref([]);
const showUsers = ref(false);
const users = ref([]);

const goBack = () => {
  router.push('/home-page');
};

const addItem = () => {
  if (newItem.value.trim()) {
    items.value.push({ id: Date.now(), name: newItem.value.trim() });
    updateStorage();
    newItem.value = '';
  }
};

const removeItem = (id) => {
  items.value = items.value.filter(item => item.id !== id);
  updateStorage();
};

const updateStorage = () => {
  const savedLists = JSON.parse(localStorage.getItem('shoppingLists')) || [];
  const index = savedLists.findIndex(list => list.id == listId);
  if (index !== -1) {
    savedLists[index].items = items.value;
    localStorage.setItem('shoppingLists', JSON.stringify(savedLists));
  }
};

const shareList = () => {
  alert("Функция «Поделиться списком» пока не реализована.");
};

onMounted(() => {
  const savedLists = JSON.parse(localStorage.getItem('shoppingLists')) || [];
  const currentList = savedLists.find(list => list.id == listId);
  if (currentList) {
    listName.value = currentList.name;
    items.value = currentList.items || [];
  }

  users.value = ['Иван', 'Мария']; // Заглушка
});
</script>

<style scoped>
/* Контейнер с прозрачным фоном, чтобы был виден глобальный фон */
.container {
  padding: 20px;
  min-height: 100vh;
  background: transparent; /* Прозрачный фон */
  color: white;
  box-sizing: border-box;
  padding-bottom: 100px;
}

/* Заголовок */
.title {
  font-size: 32px;
  margin-bottom: 20px;
  text-align: center;
  color: #ffd;
}

/* Форма добавления продукта */
.form-container {
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-container input {
  padding: 10px;
  font-size: 16px;
  margin: 10px 0;
  width: 100%;
  max-width: 400px;
  border-radius: 10px;
  border: 1px solid #ccc;
}

/* Список продуктов */
.list-container ul {
  list-style: none;
  padding: 0;
}

.list-container li {
  background-color: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 10px 15px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Кнопки */
.glass-button {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(10px);
  padding: 8px 16px;
  font-size: 14px;
  border-radius: 12px;
  color: #fff;
  cursor: pointer;
  transition: all 0.2s;
}

.glass-button:hover {
  transform: scale(1.05);
  background: rgba(255, 255, 255, 0.2);
}

.add-button {
  background-color: rgba(0, 128, 0, 0.3);
  border: 1px solid rgba(0, 255, 0, 0.4);
}

.remove-button {
  background-color: rgba(128, 0, 0, 0.3);
  border: 1px solid rgba(255, 0, 0, 0.4);
}

/* Плавающие кнопки */
.floating-icon {
  position: fixed;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  backdrop-filter: blur(10px);
  color: white;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s;
}

.floating-icon:hover {
  transform: scale(1.1);
}

.back-icon {
  top: 20px;
  left: 20px;
}

.share-icon {
  bottom: 20px;
  right: 20px;
}

.user-icon {
  bottom: 20px;
  left: 20px;
}

/* Модалка */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(10, 10, 30, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 200;
}

.user-modal {
  background: #002040;
  padding: 20px;
  border-radius: 12px;
  width: 300px;
  color: white;
  position: relative;
  text-align: center;
}

.user-modal ul {
  margin-top: 10px;
  padding-left: 0;
  list-style: none;
}

.user-modal li {
  margin-bottom: 8px;
  font-weight: 500;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: transparent;
  color: white;
  border: none;
  font-size: 20px;
  cursor: pointer;
}
</style>
