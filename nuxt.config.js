export default defineNuxtConfig({
  ssr: false,

  app: {
    baseURL: '/shopping_list/', 
  },
  
    css: ['~/assets/css/main.css'],
  modules: ['@pinia/nuxt'],
  compatibilityDate: '2025-03-27',
});