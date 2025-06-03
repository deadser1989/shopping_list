<template>
  <div class="container">
    <button @click="goHome" class="home-btn">
      <Home :size="30" />
    </button>

    <h1 class="title animate__animated animate__bounce">ВАШИ СПИСКИ ПОКУПОК</h1>

    <div class="list-wrapper">

      <div
        v-for="list in shoppingLists"
        :key="list.id"
        class="shopping-list-card"
      >
        <!-- Возможность редактировать название списка только в режиме редактирования -->
        <input
          v-if="editMode && list.id === editingListId"
          v-model="list.name"
          class="edit-input"
          @blur="saveName(list)"
        />
        <span
          v-else
          @click="goToList(list.id)"
          class="list-name"
        >
          🛒 {{ list.name }}
        </span>

        <!-- Кнопка для удаления списка  -->
        <button
          v-if="editMode"
          @click="deleteList(list.id)"
          class="delete-btn"
        >
          <X :size="30" /> 
        </button>
      </div>
    </div>

    <div class="buttons-container">
      <button 
        :class="{'edit-btn-active': editMode, 'edit-btn': !editMode}" 
        @click="toggleEditMode"
      >
        <Edit2 :size="32" /> 
      </button>
      <button @click="createNewList" class="create-btn">
        <span class="plus">+</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { Home, Edit2, X } from 'lucide-vue-next'; 

const router = useRouter();
const shoppingLists = ref([]);
const editMode = ref(false);  
const editingListId = ref(null);  // ID редактируемого списка

onMounted(() => {
  const savedLists = JSON.parse(localStorage.getItem('shoppingLists')) || [];
  shoppingLists.value = savedLists;
});

const createNewList = () => {
  const id = Date.now();
  const newName = `Новый список ${shoppingLists.value.length + 1}`;
  const newList = { id, name: newName, items: [] };

  shoppingLists.value.push(newList);
  updateStorage();
};

const updateStorage = () => {
  localStorage.setItem('shoppingLists', JSON.stringify(shoppingLists.value));
};

const goToList = (id) => {
  if (!editMode.value) {
    router.push(`/shopping-list/${id}`);
  }
};

const toggleEditMode = () => {
  editMode.value = !editMode.value;
  if (!editMode.value) {
    editingListId.value = null;
  }
};

const saveName = (list) => {
  updateStorage();
  editMode.value = false;
  editingListId.value = null;
};

const deleteList = (id) => {
  shoppingLists.value = shoppingLists.value.filter((list) => list.id !== id);
  updateStorage();
};

const goHome = () => {
  router.push('/');
};
</script>

<style scoped>
body {
  background: linear-gradient(to bottom right, #005a78, #4f0080);
  font-family: 'Roboto', 'Open Sans', 'Montserrat', 'PT Sans', sans-serif;
  height: 100vh;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  max-width: 600px;
  margin: 100px auto;
  padding: 40px;
  text-align: center;
  border-radius: 15px;
  background-color: transparent; 
}

/* Кнопка домой */
.home-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  background-color: transparent;
  border: none;
  font-size: 30px;
  color: #fff;
  cursor: pointer;
}

.home-btn:hover {
  color: #ffc402;
}

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

/* Стиль для обертки списка */
.list-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center; 
  margin-top: 20px;
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

.create-btn, .edit-btn {
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

.edit-btn {
  background-color: #ccc;
}

.edit-btn-active {
  background-color: #f44236;
}

.edit-btn:hover, .edit-btn-active:hover {
  background-color: #d63e31;
}

.plus {
  font-size: 40px;
}

.pen {
  font-size: 40px;
}

/* Стиль карточек списков */
.shopping-list-card {
  width: 90%;
  max-width: 400px;
  background: linear-gradient(135deg, #6a31b4, #7930cd);
  padding: 15px;
  border-radius: 15px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: transform 0.2s ease;
  margin-bottom: 15px;
  position: relative;
}

.shopping-list-card:hover {
  transform: scale(1.05);
}

.shopping-list-card .list-name {
  color: #fff;
  font-size: 18px;
  font-weight: bold;
}

/* Поле для редактирования названия списка */
.edit-input {
  width: 100%;
  padding: 10px;
  font-size: 18px;
  border: 2px solid #ccc;
  border-radius: 8px;
}

/* Кнопка удаления списка */
.delete-btn {
  position: absolute;
  right: 10px;
  top: 50%; 
  transform: translateY(-50%); 
  background-color: red;
  color: white;
  border: none;
  padding: 8px;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.delete-btn:hover {
  background-color: darkred;
}

.minus {
  font-size: 18px;
}
</style>
