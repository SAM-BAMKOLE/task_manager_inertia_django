<script setup>
import { computed, ref } from "vue";
import { Link } from "@inertiajs/vue3";
const props = defineProps({ auth: Object, flash: Object });
const checkboxRef = ref(null);
function toggleSidebar() {
  checkboxRef.value.checked = !checkboxRef.value.checked;
}
const flash = computed(() => props.flash);
const auth = computed(() => props.auth);
</script>

<template>
  <div class="fixed z-100 top-10 w-full flex justify-center">
    <div v-if="flash?.success" class="alert alert-success">
      {{ flash.success }}
    </div>
    <div v-if="flash?.error" class="alert alert-error">
      {{ flash.error }}
    </div>
    <div v-if="flash?.info" class="alert alert-info">
      {{ flash.info }}
    </div>
  </div>

  <div class="drawer md:drawer-open">
    <input
      ref="checkboxRef"
      type="checkbox"
      id="my-drawer"
      class="drawer-toggle"
    />
    <div class="drawer-content">
      <!-- Top Navigation Bar -->
      <header
        class="h-16 flex items-center justify-between border-b border-base-300 bg-gray-100 px-6"
      >
        <div class="flex items-center gap-2">
          <button class="btn btn-ghost btn-sm md:hidden" @click="toggleSidebar">
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
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
          <div class="text-sm breadcrumbs">
            <ul>
              <li><Link href="/dashboard">Dashboard</Link></li>
              <li><Link href="/task/">Tasks</Link></li>
              <li>Today</li>
            </ul>
          </div>
        </div>

        <div class="flex items-center gap-4">
          <Link
            href="/task/create"
            class="btn btn-primary btn-sm hidden md:flex"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4"
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
            New Task
          </Link>
          <div class="dropdown dropdown-end">
            <div
              tabindex="0"
              role="button"
              class="btn btn-ghost btn-circle avatar"
            >
              <div
                class="w-8 h-8 p-1.5 rounded-full bg-primary text-primary-content flex items-center justify-center"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
              </div>
            </div>
            <ul
              tabindex="0"
              class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52 border border-base-300"
            >
              <li><Link href="/profile">Profile</Link></li>
              <!-- <li><Link href="/settings">Settings</Link></li> -->
              <li>
                <Link href="/logout/" class="text-error" method="post"
                  >Logout</Link
                >
              </li>
            </ul>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <main class="flex-1 overflow-y-auto p-5 bg-base-100 relative">
        <!-- <Suspense>
          <template #default> -->
        <slot />
        <!-- </template>
        </Suspense> -->
      </main>
    </div>
    <div class="drawer-side">
      <label
        for="my-drawer"
        aria-label="close sidebar"
        class="drawer-overlay"
      ></label>
      <div
        class="w-64 bg-base-200 h-full border-r border-base-300 flex flex-col"
      >
        <div class="p-4 border-b border-base-300">
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
        </div>
        <nav class="flex-1 p-4 space-y-2 overflow-y-auto">
          <Link
            href="/dashboard"
            class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors"
          >
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
                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
              />
            </svg>
            Dashboard
          </Link>
          <Link
            href="/task/"
            class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors"
          >
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
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
              />
            </svg>
            Tasks
          </Link>
          <Link
            href="/task/tags"
            class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors"
          >
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
                d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"
              />
            </svg>
            Tags
          </Link>
          <!-- <Link
          href="/task/calendar"
          class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors"
        >
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
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
            />
          </svg>
          Calendar
        </Link> -->
        </nav>
        <div class="p-4 border-t border-base-300">
          <Link
            href="/profile"
            class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors"
          >
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
                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
              />
            </svg>
            Profile
          </Link>
          <!-- <Link
          href="/settings"
          class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors"
        >
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
              d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
            />
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
            />
          </svg>
          Settings
        </Link> -->
          <Link
            method="post"
            href="/logout/"
            class="flex items-center gap-3 p-2 rounded-lg hover:bg-base-300 transition-colors text-error w-full"
          >
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
                d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
              />
            </svg>
            Logout
          </Link>
        </div>
      </div>
    </div>
  </div>
</template>
