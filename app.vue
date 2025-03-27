<template>
	<NuxtLayout>
		<Header />
		<NuxtPage />
		<Footer />
	</NuxtLayout>
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

  <script>
  import 'animate.css'
  </script>

<style>
@import url("animate.css");
</style>