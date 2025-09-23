<script setup>
import { Link, Form, useForm, router } from "@inertiajs/vue3";
import { computed } from "vue";
const props = defineProps({
  tasks: Array,
  title: String,
  description: String,
});

const tasks = computed(() => props.tasks);

const deleteForm = useForm({ _method: "DELETE" });
function deleteTask(id) {
  deleteForm.post(`/task/delete/${id}`, { forceFormData: true });
  // router.get("/dashboard/");
  router.reload();
}
</script>
<template>
  <!-- Dashboard Page -->
  <div id="dashboard-page">
    <div class="mb-6">
      <h2 class="text-2xl font-bold">{{ title }}</h2>
      <p class="text-base-content/60">{{ description }}</p>
    </div>

    <!-- Stats Overview -->
    <div class="">
      <!-- Recent Tasks -->
      <div class="card bg-base-100 shadow-md mb-6">
        <div class="card-body">
          <h3 class="card-title">Recent Tasks</h3>
          <div class="overflow-x-auto">
            <table class="table">
              <thead>
                <tr>
                  <th>Task</th>
                  <th>Due Date</th>
                  <th>Priority</th>
                  <th>Tags</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="task in tasks">
                  <td>
                    <div class="flex items-center gap-3">
                      <input
                        type="checkbox"
                        class="checkbox checkbox-primary checkbox-sm"
                        v-model="task.is_completed"
                        @change="
                          () =>
                            router.post(
                              `/task/update/${task.id}`,
                              {
                                _method: 'PATCH',
                              },
                              { forceFormData: true }
                            )
                        "
                      />
                      <div class="min-w-[12rem]">
                        <div class="font-bold">{{ task.title }}</div>
                        <div class="text-sm text-base-content/60">
                          {{ task.description }}
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="whitespace-nowrap">{{ task.due_date }}</td>
                  <td>
                    <span
                      class="badge badge-sm"
                      :class="
                        task.priority === 'HIGH'
                          ? 'badge-error'
                          : task.priority === 'MEDIUM'
                          ? 'badge-warning'
                          : 'badge-success'
                      "
                      >{{ task.priority }}</span
                    >
                  </td>

                  <td class="text-center">
                    <div v-if="task.tags?.length" class="flex flex-wrap gap-1">
                      <span
                        v-for="tag in task.tags"
                        class="badge badge-outline badge-sm whitespace-nowrap"
                        >{{ tag.name }}</span
                      >
                    </div>
                    <div v-else class="">-----</div>
                  </td>
                  <td>
                    <div class="flex gap-2">
                      <Form :action="`/task/edit/${task.id}`">
                        <button class="btn btn-ghost btn-xs">Edit</button>
                      </Form>
                      <button
                        class="btn btn-ghost btn-xs text-error"
                        @click="deleteTask(task.id)"
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Dashboard Page -->
</template>
