<script setup>
import { useForm, router } from "@inertiajs/vue3";
const props = defineProps({
  tasks_stats: Object,
  user: Object,
  errors: Object,
});
const form = useForm({
  first_name: props.user.first_name,
  last_name: props.user.last_name,
  email: props.user.email,
  _method: "PUT",
});
function submitProfileUpdate() {
  form.post("/profile/", { forceFormData: true });
}
</script>

<template>
  <!-- Profile Page -->
  <div id="profile-page">
    <div class="mb-6">
      <h2 class="text-2xl font-bold">Profile</h2>
      <p class="text-base-content/60">Manage your account settings</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2">
        <div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h3 class="card-title">Personal Information</h3>
            <form class="space-y-4" @submit.prevent="submitProfileUpdate">
              <div class="form-control">
                <label class="label">
                  <span class="label-text">First Name</span>
                </label>
                <input
                  type="text"
                  v-model="form.first_name"
                  class="input input-bordered block w-full max-w-2xl"
                />
                <ul
                  v-if="errors?.first_name"
                  class="mt-1 text-xs font-medium list-disc list-inside text-red-500"
                >
                  <li v-for="error in errors.first_name" class="">
                    {{ error }}
                  </li>
                </ul>
              </div>
              <div class="form-control">
                <label class="label">
                  <span class="label-text">Last Name</span>
                </label>
                <input
                  type="text"
                  v-model="form.last_name"
                  class="input input-bordered block w-full max-w-2xl"
                />
              </div>
              <div class="form-control">
                <label class="label">
                  <span class="label-text"
                    >Email Address (If you change, remember to use it when next
                    you Login)</span
                  >
                </label>
                <input
                  type="email"
                  v-model="form.email"
                  class="input input-bordered block w-full max-w-2xl"
                />
              </div>
              <div class="form-control mt-6">
                <button
                  type="submit"
                  class="btn btn-primary"
                  :disabled="form.processing"
                >
                  Update Profile
                </button>
              </div>
            </form>
          </div>
        </div>
        <!-- 
        <div class="card bg-base-100 shadow-md mt-6">
          <div class="card-body">
            <h3 class="card-title">Change Password</h3>
            <form class="space-y-4">
              <div class="form-control">
                <label class="label">
                  <span class="label-text">Current Password</span>
                </label>
                <input type="password" class="input input-bordered" />
              </div>
              <div class="form-control">
                <label class="label">
                  <span class="label-text">New Password</span>
                </label>
                <input type="password" class="input input-bordered" />
              </div>
              <div class="form-control">
                <label class="label">
                  <span class="label-text">Confirm New Password</span>
                </label>
                <input type="password" class="input input-bordered" />
              </div>
              <div class="form-control mt-6">
                <button type="submit" class="btn btn-primary">
                  Update Password
                </button>
              </div>
            </form>
          </div>
        </div>
         -->
      </div>

      <div>
        <div class="card bg-base-100 shadow-md mt-6">
          <div class="card-body">
            <h3 class="card-title">Account Statistics</h3>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span>Total Tasks</span>
                <span class="font-semibold">{{ tasks_stats.count }}</span>
              </div>
              <div class="flex justify-between">
                <span>Completed Tasks</span>
                <span class="font-semibold">{{
                  tasks_stats.completed_count
                }}</span>
              </div>
              <div class="flex justify-between">
                <span>Pending Tasks</span>
                <span class="font-semibold">{{
                  tasks_stats.uncompleted_count
                }}</span>
              </div>
              <div class="flex justify-between">
                <span>Overdue Tasks</span>
                <span class="font-semibold">{{
                  tasks_stats.overdue_count
                }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Profile Page -->
</template>
