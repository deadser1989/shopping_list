<template>
  <div class="container">
    <h1 class="title">{{ listName || "Список покупок" }}</h1>

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
    <NuxtLink to="/home-page" class="back-btn">← Назад</NuxtLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const listId = route.params.id; // Получаем ID из URL

const listName = ref('');
const newItem = ref('');
const items = ref([]);

onMounted(() => {
  const savedLists = JSON.parse(localStorage.getItem('shoppingLists')) || [];
  const currentList = savedLists.find(list => list.id == listId);

  if (currentList) {
    listName.value = currentList.name;
    items.value = currentList.items;
  }
});

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
</script>

<style scoped>
/* Стили такие же */
</style>
