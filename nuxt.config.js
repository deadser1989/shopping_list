// nuxt.config.js
export default defineNuxtConfig({
  ssr: false,

  app: {
    baseURL: '/shopping_list/', 
  },
  
  css: ['~/assets/css/main.css'],
  
  modules: ['@pinia/nuxt', '@nuxt/fonts'],
  
  googleFonts: {
    families: {
      Roboto: [400, 700], // Укажите нужные начертания
      OpenSans: [400, 700],
      Montserrat: [400, 700],
      PTSans: [400, 700]
    }
  },

  compatibilityDate: '2025-03-27',
});