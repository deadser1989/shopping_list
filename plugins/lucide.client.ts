import { defineNuxtPlugin } from '#app'
import { Heart, ShoppingCart, Home } from 'lucide-vue-next' // Импорт нужных иконок

export default defineNuxtPlugin((nuxtApp) => {
  // Регистрируем иконки вручную
  nuxtApp.vueApp.component('HeartIcon', Heart)
  nuxtApp.vueApp.component('ShoppingCartIcon', ShoppingCart)
  nuxtApp.vueApp.component('HomeIcon', Home)
})
