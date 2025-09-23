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
  <div class="flex items-center justify-center min-h-[80dvh]">
    <section class="bg-base-100 py-16">
      <div class="max-w-3xl mx-auto text-center">
        <h2 class="text-4xl font-extrabold text-primary mb-4">
          About TaskFlow
        </h2>
        <p class="text-lg text-base-content mb-8">
          TaskFlow is your personal task manager designed to help you stay
          organized and productive every day.
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 text-left mt-8">
          <div class="card bg-base-200 shadow-sm p-6">
            <h3 class="font-bold text-primary mb-2">📝 Easy Task Creation</h3>
            <p>
              Create, edit, and delete tasks with a simple, intuitive interface.
            </p>
          </div>
          <div class="card bg-base-200 shadow-sm p-6">
            <h3 class="font-bold text-primary mb-2">📅 Calendar View</h3>
            <p>
              Visualize your tasks and deadlines in a beautiful calendar layout.
            </p>
          </div>
          <div class="card bg-base-200 shadow-sm p-6">
            <h3 class="font-bold text-primary mb-2">🏷️ Tag & Categorize</h3>
            <p>
              Organize tasks with custom tags and categories for easy filtering.
            </p>
          </div>
          <div class="card bg-base-200 shadow-sm p-6">
            <h3 class="font-bold text-primary mb-2">
              🔒 Secure Authentication
            </h3>
            <p>Keep your data safe with secure login and profile management.</p>
          </div>
        </div>
        <div class="mt-10 flex justify-center gap-4">
          <Link href="/register">
            <button class="btn btn-primary lg:btn-lg normal-case">
              Try TaskFlow
            </button>
          </Link>
          <Link href="/">
            <button class="btn btn-outline btn-primary lg:btn-lg normal-case">
              Back to Home
            </button>
          </Link>
        </div>
      </div>
    </section>
  </div>
</template>
