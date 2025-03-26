export default defineNuxtConfig({
  ssr: false,

  app: {
    baseURL: '/shopping_list/', 
  },

  modules: ['@pinia/nuxt'],
  compatibilityDate: '2025-03-27',
});