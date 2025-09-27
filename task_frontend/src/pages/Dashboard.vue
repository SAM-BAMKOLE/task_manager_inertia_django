<script setup>
import Layout from "../components/Layout.vue";
import { Link, Form, useForm, router } from "@inertiajs/vue3";
import { computed } from "vue";

defineOptions({ layout: Layout });
const props = defineProps({
  tasks_data: Object,
  additional_data: Object,
  name: String,
});

const tasks = computed(() => props.tasks_data.latest_tasks);
const completed = computed(() => props.tasks_data.completed_count);
const uncompleted = computed(() => props.tasks_data.uncompleted_count);
const overdue = computed(() => props.tasks_data.overdue_count);
const taskCount = computed(() => props.tasks_data.count);

const deleteForm = useForm({ _method: "DELETE" });
function deleteTask(id) {
  deleteForm.post(`/task/delete/${id}`, { forceFormData: true });
}
</script>
<template>
  <!-- Dashboard Page -->
  <div id="dashboard-page">
    <div class="mb-6 flex gap-4 justify-between items-center">
      <div class="">
        <h2 class="text-2xl font-bold">Dashboard</h2>
        <p class="text-base-content/60">
          Welcome back, {{ name }}! Here's your task overview.
        </p>
      </div>
      <Link href="/task/create" class="btn-sm btn btn-primary md:hidden">
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
        New Task
      </Link>
    </div>

    <!-- Stats Overview -->
    <div v-if="tasks && tasks.length > 0" class="">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div class="stat bg-base-200 rounded-lg">
          <div class="stat-figure text-primary">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-8 w-8"
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
          </div>
          <div class="stat-title">Total Tasks</div>
          <div class="stat-value">{{ taskCount }}</div>
          <div class="stat-desc">All your tasks</div>
        </div>

        <div class="stat bg-base-200 rounded-lg">
          <div class="stat-figure text-success">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-8 w-8"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <div class="stat-title">Completed</div>
          <div class="stat-value">{{ completed }}</div>
          <div class="stat-desc">
            {{ ((completed / taskCount) * 100).toFixed(2) ?? 0 }}% of tasks
          </div>
        </div>

        <div class="stat bg-base-200 rounded-lg">
          <div class="stat-figure text-warning">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-8 w-8"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <div class="stat-title">Pending</div>
          <div class="stat-value">{{ uncompleted }}</div>
          <div class="stat-desc">To be completed</div>
        </div>

        <div class="stat bg-base-200 rounded-lg">
          <div class="stat-figure text-error">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-8 w-8"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
              />
            </svg>
          </div>
          <div class="stat-title">Overdue</div>
          <div class="stat-value">{{ overdue }}</div>
          <div class="stat-desc">Needs attention</div>
        </div>
      </div>

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
                <!-- 
              <tr>
                <td>
                  <div class="flex items-center gap-3">
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                    />
                    <div>
                      <div class="font-bold">Complete project proposal</div>
                      <div class="text-sm text-base-content/60">
                        Design & Development
                      </div>
                    </div>
                  </div>
                </td>
                <td>Today</td>
                <td>
                  <span class="badge badge-warning badge-sm">Medium</span>
                </td>
                <td>
                  <span class="badge badge-ghost badge-sm">In Progress</span>
                </td>
                <td>
                  <button class="btn btn-ghost btn-xs">Edit</button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="flex items-center gap-3">
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                      checked
                    />
                    <div>
                      <div class="font-bold">Team meeting</div>
                      <div class="text-sm text-base-content/60">
                        Weekly sync
                      </div>
                    </div>
                  </div>
                </td>
                <td>Yesterday</td>
                <td><span class="badge badge-success badge-sm">Low</span></td>
                <td>
                  <span class="badge badge-success badge-sm">Completed</span>
                </td>
                <td>
                  <button class="btn btn-ghost btn-xs">Edit</button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="flex items-center gap-3">
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                    />
                    <div>
                      <div class="font-bold">Client presentation</div>
                      <div class="text-sm text-base-content/60">
                        Prepare slides
                      </div>
                    </div>
                  </div>
                </td>
                <td>Tomorrow</td>
                <td><span class="badge badge-error badge-sm">High</span></td>
                <td>
                  <span class="badge badge-ghost badge-sm">Not Started</span>
                </td>
                <td>
                  <button class="btn btn-ghost btn-xs">Edit</button>
                </td>
              </tr>
               -->
                <tr v-for="task in tasks">
                  <td>
                    <div class="flex items-center gap-3">
                      <input
                        type="checkbox"
                        class="checkbox checkbox-primary checkbox-sm"
                        v-model="task.is_completed"
                        @change="
                          () => {
                            router.post(
                              `/task/update/${task.id}`,
                              {
                                _method: 'PATCH',
                              },
                              { forceFormData: true }
                            );
                            router.reload();
                          }
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
                  <!-- <td>
                    <span class="badge badge-ghost badge-sm">{{
                      task.status ?? "----"
                    }}</span>
                  </td> -->

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
          <div class="card-actions justify-end mt-4">
            <a href="/task/" class="btn btn-primary btn-sm">View All Tasks</a>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="my-6">
      <p class="font-semibold text-base-content/60">
        You currently don't have any tasks
      </p>
      <Link href="/task/create/" class="mt-3 btn btn-primary btn-sm"
        >Add your first task</Link
      >
    </div>
  </div>
  <!-- End Dashboard Page -->
</template>
