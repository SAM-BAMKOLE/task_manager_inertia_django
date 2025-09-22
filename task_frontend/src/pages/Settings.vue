<script setup></script>
<template>
  <!-- Settings Page -->
  <div id="settings-page">
    <div class="mb-6">
      <h2 class="text-2xl font-bold">Settings</h2>
      <p class="text-base-content/60">Customize your TaskFlow experience</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2">
        <div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h3 class="card-title">Appearance</h3>
            <div class="form-control">
              <label class="label cursor-pointer justify-start gap-4">
                <span class="label-text">Dark Mode</span>
                <input type="checkbox" class="toggle toggle-primary" />
              </label>
            </div>
            <div class="form-control">
              <label class="label">
                <span class="label-text">Theme Color</span>
              </label>
              <div class="flex gap-2">
                <div
                  class="w-8 h-8 rounded-full bg-primary cursor-pointer"
                ></div>
                <div
                  class="w-8 h-8 rounded-full bg-secondary cursor-pointer"
                ></div>
                <div
                  class="w-8 h-8 rounded-full bg-accent cursor-pointer"
                ></div>
                <div class="w-8 h-8 rounded-full bg-info cursor-pointer"></div>
                <div
                  class="w-8 h-8 rounded-full bg-success cursor-pointer"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <div class="card bg-base-100 shadow-md mt-6">
          <div class="card-body">
            <h3 class="card-title">Notifications</h3>
            <div class="form-control">
              <label class="label cursor-pointer justify-start gap-4">
                <span class="label-text">Email Notifications</span>
                <input type="checkbox" class="toggle toggle-primary" checked />
              </label>
            </div>
            <div class="form-control">
              <label class="label cursor-pointer justify-start gap-4">
                <span class="label-text">Task Reminders</span>
                <input type="checkbox" class="toggle toggle-primary" checked />
              </label>
            </div>
            <div class="form-control">
              <label class="label cursor-pointer justify-start gap-4">
                <span class="label-text">Overdue Alerts</span>
                <input type="checkbox" class="toggle toggle-primary" checked />
              </label>
            </div>
          </div>
        </div>

        <div class="card bg-base-100 shadow-md mt-6">
          <div class="card-body">
            <h3 class="card-title">Danger Zone</h3>
            <p class="text-base-content/60 mb-4">
              Once you delete your account, there is no going back. Please be
              certain.
            </p>
            <button class="btn btn-error btn-outline btn-sm">
              Delete Account
            </button>
          </div>
        </div>
      </div>

      <div>
        <div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h3 class="card-title">Preferences</h3>
            <div class="form-control">
              <label class="label">
                <span class="label-text">Default View</span>
              </label>
              <select class="select select-bordered">
                <option>Dashboard</option>
                <option selected>Tasks</option>
                <option>Calendar</option>
              </select>
            </div>
            <div class="form-control">
              <label class="label">
                <span class="label-text">Tasks Per Page</span>
              </label>
              <select class="select select-bordered">
                <option>10</option>
                <option selected>25</option>
                <option>50</option>
              </select>
            </div>
            <div class="form-control">
              <label class="label">
                <span class="label-text">Week Starts On</span>
              </label>
              <select class="select select-bordered">
                <option>Sunday</option>
                <option selected>Monday</option>
              </select>
            </div>
            <div class="form-control mt-6">
              <button type="submit" class="btn btn-primary">
                Save Preferences
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Settings Page -->
</template>
