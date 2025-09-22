<script setup>
import { useForm, Link } from "@inertiajs/vue3";
import { ref } from "vue";

defineOptions({ layout: null });
defineProps({ errors: Object });

const form = useForm({
  email: "",
  first_name: "",
  last_name: "",
  password1: "",
  password2: "",
});
const onSubmit = () => {
  form.post("/register/", { forceFormData: true });
};
</script>
<template>
  <!-- Register Page -->
  <div
    id="register-page"
    class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary/10 to-secondary/10 py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-md w-full space-y-8 bg-base-100 p-8 rounded-xl shadow-lg">
      <div>
        <h2 class="mt-6 text-center text-3xl font-bold text-primary">
          Create your account
        </h2>
        <p class="mt-2 text-center text-sm text-base-content/60">
          Join TaskFlow to boost your productivity
        </p>
        <ul
          v-if="errors"
          class="text-xs text-red-500 font-medium mt-4 list-inside list-disc space-y-1"
        >
          <li v-for="(error, key) in errors" :key="key">{{ error }}</li>
        </ul>
      </div>
      <form @submit.prevent="onSubmit" class="mt-8 space-y-6">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="first_name" class="sr-only">First Name</label>
            <input
              id="first_name"
              name="first_name"
              type="text"
              autocomplete="fist_name"
              required
              v-model="form.first_name"
              class="input input-bordered rounded-none relative block w-full rounded-t-md focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="First Name"
            />
          </div>
          <div>
            <label for="last_name" class="sr-only">Last Name</label>
            <input
              id="last_name"
              name="last_name"
              type="text"
              autocomplete="last_name"
              required
              v-model="form.last_name"
              class="input input-bordered rounded-none relative block w-full focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="Last Name"
            />
          </div>
          <div>
            <label for="email" class="sr-only">Email address</label>
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              v-model="form.email"
              class="input input-bordered rounded-none relative block w-full focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="Email address"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              name="password1"
              type="password"
              autocomplete="new-password"
              required
              v-model="form.password1"
              class="input input-bordered rounded-none relative block w-full focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="Password"
            />
          </div>
          <div>
            <label for="password-confirmation" class="sr-only"
              >Confirm Password</label
            >
            <input
              id="password-confirmation"
              name="password2"
              type="password"
              autocomplete="new-password"
              required
              v-model="form.password2"
              class="input input-bordered rounded-none relative block w-full rounded-b-md focus:z-10 focus:outline-0 focus:ring-[0.5px] focus:ring-blue-600"
              placeholder="Confirm Password"
            />
          </div>
        </div>

        <div class="flex items-center">
          <input
            id="terms"
            name="terms"
            type="checkbox"
            class="checkbox checkbox-primary checkbox-sm"
            required
          />
          <label for="terms" class="ml-2 block text-sm text-base-content"
            >I agree to the
            <a href="#" class="font-medium text-primary hover:text-primary/80"
              >Terms and Conditions</a
            ></label
          >
        </div>

        <div>
          <button
            :disabled="form.processing"
            type="submit"
            class="group relative w-full flex justify-center btn btn-primary"
          >
            Create Account
          </button>
        </div>

        <div class="text-center">
          <p class="text-sm text-base-content/60">
            Already have an account?
            <Link
              href="/login"
              class="font-medium text-secondary hover:text-secondary/80"
              >Sign in</Link
            >
          </p>
        </div>
      </form>
    </div>
  </div>
  <!-- End Register Page -->
</template>
