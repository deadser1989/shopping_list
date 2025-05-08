<template>
  <div class="container">
    <button @click="goHome" class="home-btn">
      <Home :size="30" />
    </button>

    <h1 class="title animate__animated animate__bounce">ПРОДУКТОВЫЕ КАРТЫ</h1>
    <p class="mini-app-text">Добавьте скидочные карты магазинов</p>

    <div class="cards-container">
      <div 
        v-for="card in productCards" 
        :key="card.id" 
        class="card-item"
        @click="showCardDetails(card)"
      >
        <div class="card-header">
          <img :src="getStoreLogo(card.store)" class="store-logo" />
          <h3>{{ card.store }}</h3>
        </div>
        <div class="card-barcode">
          <img :src="generateBarcode(card.barcode)" v-if="card.barcode" />
          <p v-else class="no-barcode">QR-код не добавлен</p>
        </div>
      </div>
    </div>

    <div class="buttons-container">
      <button @click="showAddCardModal" class="create-btn">
        <span class="plus">+</span>
      </button>
    </div>

    <!-- Модальное окно добавления карты -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <button class="close-btn" @click="closeModal">
          <X :size="24" />
        </button>
        
        <h2>Добавить новую карту</h2>
        
        <div class="form-group">
          <label>Магазин:</label>
          <select v-model="newCard.store" class="form-input">
            <option v-for="store in popularStores" :value="store">{{ store }}</option>
            <option value="other">Другой магазин</option>
          </select>
          
          <input 
            v-if="newCard.store === 'other'" 
            v-model="newCard.customStore" 
            placeholder="Введите название магазина" 
            class="form-input"
          >
        </div>
        
        <div class="form-group">
          <label>Штрих-код/QR-код:</label>
          <input 
            v-model="newCard.barcode" 
            placeholder="Введите номер карты" 
            class="form-input"
          >
          <button @click="scanBarcode" class="scan-btn">
            <Scan :size="20" /> Сканировать
          </button>
        </div>
        
        <button @click="addProductCard" class="submit-btn">Добавить карту</button>
      </div>
    </div>

    <!-- Модальное окно просмотра карты -->
    <div v-if="selectedCard" class="card-modal-overlay" @click.self="selectedCard = null">
      <div class="card-modal-content">
        <button class="close-btn" @click="selectedCard = null">
          <X :size="24" />
        </button>
        
        <div class="card-modal-header">
          <img :src="getStoreLogo(selectedCard.store)" class="store-logo-large" />
          <h2>{{ selectedCard.store }}</h2>
        </div>
        
        <div class="card-modal-barcode">
          <img :src="generateBarcode(selectedCard.barcode)" v-if="selectedCard.barcode" />
          <p v-else class="no-barcode">QR-код не добавлен</p>
          <p class="barcode-number">{{ selectedCard.barcode }}</p>
        </div>
        
        <button @click="deleteCard(selectedCard.id)" class="delete-card-btn">
          Удалить карту
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Home, X, Scan } from 'lucide-vue-next';
import JsBarcode from 'jsbarcode';
import { useRouter } from 'vue-router';

const router = useRouter();
const productCards = ref([]);
const showModal = ref(false);
const selectedCard = ref(null);

// Популярные магазины для выпадающего списка
const popularStores = ref([
  'Перекресток',
  'Пятерочка',
  'Магнит',
  'Лента',
  'Ашан',
  'Метро',
  'Дикси',
  'ВкусВилл'
]);

// Данные новой карты
const newCard = ref({
  store: 'Перекресток',
  customStore: '',
  barcode: ''
});

onMounted(() => {
  loadCards();
});

const loadCards = () => {
  const savedCards = localStorage.getItem('productCards');
  if (savedCards) {
    productCards.value = JSON.parse(savedCards);
  }
};

const saveCards = () => {
  localStorage.setItem('productCards', JSON.stringify(productCards.value));
};

const showAddCardModal = () => {
  resetNewCard();
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

const resetNewCard = () => {
  newCard.value = {
    store: 'Перекресток',
    customStore: '',
    barcode: ''
  };
};

const addProductCard = () => {
  if (!newCard.value.barcode) {
    alert('Пожалуйста, введите номер карты');
    return;
  }

  const storeName = newCard.value.store === 'other' 
    ? newCard.value.customStore 
    : newCard.value.store;

  if (!storeName) {
    alert('Пожалуйста, укажите магазин');
    return;
  }

  const card = {
    id: Date.now(),
    store: storeName,
    barcode: newCard.value.barcode,
    createdAt: new Date().toISOString()
  };

  productCards.value.push(card);
  saveCards();
  closeModal();
};

const deleteCard = (id) => {
  productCards.value = productCards.value.filter(card => card.id !== id);
  saveCards();
  selectedCard.value = null;
};

const showCardDetails = (card) => {
  selectedCard.value = card;
};

const scanBarcode = () => {
  // В реальном приложении здесь будет вызов API для сканирования
  // Для демо просто имитируем сканирование
  alert('В реальном приложении здесь будет открываться сканер камеры');
};

const generateBarcode = (barcode) => {
  if (!barcode) return null;
  
  try {
    const canvas = document.createElement('canvas');
    JsBarcode(canvas, barcode, {
      format: 'CODE128',
      width: 2,
      height: 60,
      displayValue: false
    });
    return canvas.toDataURL();
  } catch (e) {
    console.error('Error generating barcode:', e);
    return null;
  }
};

const getStoreLogo = (storeName) => {
  // В реальном приложении можно использовать API для получения логотипов
  // или хранить локально набор популярных логотипов
  const logos = {
    'Перекресток': '/images/stores/perekrestok.png',
    'Пятерочка': '/images/stores/pyaterochka.png',
    'Магнит': '/images/stores/magnit.png',
    'Лента': '/images/stores/lenta.png',
    'Ашан': '/images/stores/ashan.png',
    'Метро': '/images/stores/metro.png',
    'Дикси': '/images/stores/dixy.png',
    'ВкусВилл': '/images/stores/vkusvill.png'
  };
  
  return logos[storeName] || '/images/stores/default-store.png';
};

const goHome = () => {
  router.push('/');
};
</script>

<style scoped>
/* Общие стили текста */
.mini-app-text {
  font-family: 'Exo 2', sans-serif;
  font-size: 22px;
  font-weight: 500;
  color: #ffc402;
  text-align: center;
  margin-bottom: 30px;
}

/* Специальные стили для заголовка */
.title {
  font-family: 'Exo 2', sans-serif;
  font-size: 37px;
  font-weight: 600;
  color: #eaffda;
  text-align: center;
  text-shadow: 2px 2px 5px rgba(48, 0, 38, 0.247);
  margin-bottom: 15px;
}

/* Контейнер */
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  position: relative;
  min-height: 100vh;
  padding-bottom: 100px;
}

/* Кнопка "Домой" */
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

/* Контейнер для карточек */
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

/* Стиль карточки магазина */
.card-item {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  padding: 15px;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
  backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.card-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.store-logo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
  object-fit: cover;
}

.card-barcode img {
  width: 100%;
  height: auto;
  max-height: 80px;
  object-fit: contain;
}

.no-barcode {
  color: rgba(255, 255, 255, 0.5);
  font-style: italic;
}

/* Кнопки добавления */
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
  background-color: #00aa88;
}

.create-btn:hover {
  background-color: #00856d;
}

.plus {
  font-size: 40px;
}

/* Модальные окна */
.modal-overlay, .card-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content, .card-modal-content {
  background: linear-gradient(135deg, #005a78, #4f0080);
  padding: 25px;
  border-radius: 15px;
  width: 90%;
  max-width: 400px;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: transparent;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 20px;
}

/* Форма добавления карты */
.form-group {
  margin-bottom: 20px;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #eaffda;
}

.form-input {
  width: 100%;
  padding: 12px;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  background: rgba(0, 0, 0, 0.2);
  color: white;
  font-size: 16px;
  margin-bottom: 10px;
}

.scan-btn {
  width: 100%;
  padding: 10px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: background 0.3s;
}

.scan-btn:hover {
  background: rgba(255, 255, 255, 0.2);
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background: #00aa88;
  border: none;
  border-radius: 10px;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.submit-btn:hover {
  background: #00856d;
}

/* Модальное окно просмотра карты */
.card-modal-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  gap: 15px;
}

.store-logo-large {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
}

.card-modal-barcode {
  margin: 25px 0;
}

.card-modal-barcode img {
  width: 100%;
  max-height: 150px;
  object-fit: contain;
}

.barcode-number {
  margin-top: 10px;
  font-family: monospace;
  font-size: 16px;
  word-break: break-all;
}

.delete-card-btn {
  width: 100%;
  padding: 12px;
  background: rgba(255, 0, 0, 0.3);
  border: 1px solid rgba(255, 0, 0, 0.5);
  border-radius: 10px;
  color: white;
  cursor: pointer;
  transition: background 0.3s;
}

.delete-card-btn:hover {
  background: rgba(255, 0, 0, 0.4);
}
</style>