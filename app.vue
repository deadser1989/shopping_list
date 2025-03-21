<template>
    <NuxtPage />
  </template>
  
  <script setup>
  import { useHead } from '@vueuse/head';
  
  useHead({
    script: [
      {
        src: 'https://telegram.org/js/telegram-web-app.js',
        async: true,
      },
    ],
  });
  </script>