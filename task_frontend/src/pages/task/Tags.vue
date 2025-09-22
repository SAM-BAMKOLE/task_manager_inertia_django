<script setup>
import { Link } from "@inertiajs/vue3";

const props = defineProps({ tags: Array });
</script>
<template>
  <!-- Tags Page -->
  <div id="tags-page">
    <div class="mb-6 flex justify-between items-center">
      <div>
        <h2 class="text-2xl font-bold">Tags</h2>
        <p class="text-base-content/60">Organize tasks with tags</p>
      </div>
      <!-- <button class="btn btn-primary">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          />
        </svg>
        New Tag
      </button> -->
    </div>

    <div
      v-if="tags?.length"
      class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
    >
      <div v-for="tag in tags" :key="tag.id" class="card bg-base-100 shadow-md">
        <div class="card-body">
          <div class="flex justify-between items-center">
            <h3 class="card-title">{{ tag.name }}</h3>
            <div class="flex gap-2">
              <Link :href="`/task/tag/${tag.id}`" class="btn btn-ghost btn-xs"
                >View Tasks</Link
              >
              <!-- <button class="btn btn-ghost btn-xs text-error">Delete</button> -->
            </div>
          </div>
          <p class="text-base-content/60">{{ tag.task__count }} tasks</p>
        </div>
      </div>
    </div>
    <div v-else class="">
      <h3 class="font-medium">
        You don't have any task with tags created yet!
      </h3>
    </div>
  </div>
  <!-- End Tags Page -->
</template>
