<script setup>
import { Head, Link } from "@inertiajs/vue3";
import GuestLayout from "../components/GuestLayout.vue";

defineOptions({ layout: GuestLayout });
defineProps({ title: String, description: String });
</script>

<template>
  <Head>
    <title>{{ title }}</title>
    <meta name="description" :content="description" />
  </Head>
  <!-- Hero Section -->
  <section class="bg-base-100 py-16 min-h-[80dvh] flex items-center">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-4xl font-extrabold text-primary mb-4">
        Welcome to TaskFlow
      </h2>
      <p class="text-lg text-base-content mb-8">
        Effortlessly manage your personal tasks and boost your productivity with
        a clean, intuitive interface.
      </p>
      <div class="flex flex-col sm:flex-row justify-center gap-4">
        <Link href="/register">
          <button class="btn btn-primary lg:btn-lg normal-case">
            Get Started
          </button>
        </Link>
        <Link href="/about">
          <button class="btn btn-outline btn-primary lg:btn-lg normal-case">
            Learn More
          </button>
        </Link>
      </div>
    </div>
  </section>
</template>
