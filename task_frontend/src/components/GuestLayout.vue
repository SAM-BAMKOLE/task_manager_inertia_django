<script setup>
import { Link } from "@inertiajs/vue3";
</script>
<template>
  <!-- Navbar -->
  <nav class="bg-base-100 shadow-sm">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
      <div
        class="p-4 border-b border-base-300 w-full flex justify-between items-center"
      >
        <Link href="/">
          <h1 class="text-xl font-bold text-primary flex items-center gap-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
              />
            </svg>
            TaskFlow
          </h1>
        </Link>
        <Link href="/register">
          <button class="btn btn-primary btn-sm normal-case">Register</button>
        </Link>
      </div>
    </div>
  </nav>
  <slot />
  <!-- Footer -->
  <footer class="bg-base-200 border-t border-base-300 py-6 mt-16">
    <div
      class="max-w-4xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center text-sm text-base-content"
    >
      <span
        >&copy; {{ new Date().getFullYear() }} TaskFlow. All rights
        reserved.</span
      >
      <span
        >Made with <span class="text-primary">DaisyUI</span> &amp;
        <span class="text-primary">Vue.js</span></span
      >
    </div>
  </footer>
</template>
