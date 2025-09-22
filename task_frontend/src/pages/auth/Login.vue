<script setup>
import { Link, useForm } from "@inertiajs/vue3";

defineOptions({ layout: null });
const props = defineProps({ errors: Object, next: String });

// Note that the name has to be username as Django expects a username field
const form = useForm({ username: "", password: "", next: props.next });
const onSubmit = () => {
  form.post("/login/", { forceFormData: true });
};
</script>
<template>
  <!-- Login Page -->
  <div
    id="login-page"
    class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary/10 to-secondary/10 py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-md w-full space-y-8 bg-base-100 p-8 rounded-xl shadow-lg">
      <div>
        <h2 class="mt-6 text-center text-3xl font-bold text-primary">
          Welcome to TaskFlow
        </h2>
        <p class="mt-2 text-center text-sm text-base-content/60">
          Sign in to manage your tasks
        </p>
        <ul
          v-if="errors"
          class="text-xs text-red-500 font-medium mt-4 list-inside list-disc space-y-1"
        >
          <li v-for="(error, key) in errors" :key="key">{{ error }}</li>
        </ul>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="onSubmit">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input
              id="email-address"
              name="email"
              type="email"
              autocomplete="email"
              required
              v-model="form.username"
              class="input input-bordered rounded-none relative block w-full rounded-t-md focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="Email address"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              v-model="form.password"
              class="input input-bordered rounded-none relative block w-full rounded-b-md focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="Password"
            />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              class="checkbox checkbox-primary checkbox-sm"
            />
            <label
              for="remember-me"
              class="ml-2 block text-sm text-base-content"
              >Remember me</label
            >
          </div>

          <div class="text-sm">
            <Link
              href="#"
              class="font-medium text-primary hover:text-primary/80"
              >Forgot your password?</Link
            >
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center btn btn-primary"
          >
            Sign in
          </button>
        </div>

        <div class="text-center">
          <p class="text-sm text-base-content/60">
            Don't have an account?
            <Link
              href="/register"
              class="font-medium text-secondary hover:text-secondary/80"
              >Sign up</Link
            >
          </p>
        </div>
      </form>
    </div>
  </div>
  <!-- End Login Page -->
</template>
