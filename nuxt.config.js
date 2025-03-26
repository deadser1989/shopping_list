export default defineNuxtConfig({
  ssr: false, 
  app: {
    baseURL: '/shopping_list/', 
  },
  modules: ['@pinia/nuxt'],
});
