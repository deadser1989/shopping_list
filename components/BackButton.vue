<template>
    <button class="back-btn" @click="$emit('click')">← Назад</button>
  </template>
  
  <style scoped>
  .back-btn {
    position: absolute;
    top: 20px;
    left: 20px;
    background: transparent;
    color: white;
    font-size: 18px;
    border: none;
    cursor: pointer;
  }
  </style>