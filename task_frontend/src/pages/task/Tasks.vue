<script setup>
import { ref, computed } from "vue";
import { Link, router, usePage, useForm } from "@inertiajs/vue3";
const props = defineProps({ page_obj: Object });
const tasks = computed(() => props.page_obj.tasks);

const page = usePage();
const pageQuery = computed(function () {
  const page_url = new URL(page.url, window.location.origin);
  return Object.fromEntries(new URLSearchParams(page_url.search));
});

const filter = ref({
  search: pageQuery.value.search ?? "",
  status: pageQuery.value.status ?? "ALL",
  priority: pageQuery.value.priority ?? "ALL",
});

function filterBySearch(searchQuery) {
  router.get(
    page.url,
    { search: filter.value.search },
    { preserveState: true, replace: true }
  );
}
function filterByStatus(statusQuery) {
  router.get(
    page.url,
    { status: filter.value.status },
    { preserveState: true, replace: true }
  );
}
function filterByPriority(priorityQuery) {
  router.get(
    page.url,
    { priority: filter.value.priority },
    { preserveState: true, replace: true }
  );
}

function clearFilters() {
  filter.value = { search: "", status: "ALL", priority: "ALL" };
  router.get("/task/");
}

const deleteForm = useForm({ _method: "DELETE" });

function deleteTask(id) {
  deleteForm.post(`/task/delete/${id}`, { forceFormData: true });
  router.reload();
}

function prevPage() {
  const url = new URLSearchParams({
    ...pageQuery.value,
    page: pageQuery.value.page
      ? parseInt(pageQuery.value.page) - 1
      : props.page_obj.pagination.current_page - 1,
  });

  router.get(`/task/?${url}`, {}, { preserveState: true });
}
function nextPage() {
  const url = new URLSearchParams({
    ...pageQuery.value,
    page: pageQuery.value.page
      ? parseInt(pageQuery.value.page) + 1
      : props.page_obj.pagination.current_page + 1,
  });
  router.get(`/task/?${url}`, {}, { preserveState: true });
}

function updateTasksCompleted(e) {
  const query = pageQuery.value;
  router.post("/task/update/multiple/", {
    status: e,
    query,
    tasksIds: tasks.value.map((task) => task.id),
    _method: "PATCH",
  });
  router.reload();
}
</script>
<template>
  <!-- Tasks Page -->
  <div id="tasks-page">
    <div class="mb-6 flex gap-4 justify-between items-center">
      <div>
        <h2 class="text-2xl font-bold">Tasks</h2>
        <p class="text-base-content/60">Manage all your tasks in one place</p>
      </div>
      <Link href="/task/create" class="btn-sm btn btn-primary">
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

    <!-- Filters and Search -->
    <div class="card bg-base-100 shadow-md mb-6">
      <div class="card-body">
        <div class="flex flex-col md:flex-row gap-4">
          <div class="flex-1">
            <input
              type="text"
              v-model="filter.search"
              @keyup="filterBySearch"
              placeholder="Search tasks..."
              class="input input-bordered w-full"
            />
          </div>
          <div class="flex gap-2 flex-wrap">
            <select
              class="select select-bordered select-sm"
              v-model="filter.status"
              @change="filterByStatus"
            >
              <option disabled selected>Status</option>
              <option value="ALL">All</option>
              <option value="1">Completed</option>
              <option value="0">Pending</option>
              <option value="OVERDUE">Overdue</option>
            </select>
            <select
              class="select select-bordered select-sm"
              v-model="filter.priority"
              @change="filterByPriority"
            >
              <option disabled selected>Priority</option>
              <option value="ALL">All</option>
              <option value="HIGH">High</option>
              <option value="MEDIUM">Medium</option>
              <option value="LOW">Low</option>
            </select>
            <!-- <select class="select select-bordered select-sm">
              <option disabled selected>Tags</option>
              <option>Work</option>
              <option>Personal</option>
              <option>Urgent</option>
            </select> -->
            <button class="btn btn-sm btn-ghost" @click="clearFilters">
              Clear Filters
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tasks List -->
    <div class="card bg-base-100 shadow-md">
      <div class="card-body p-0">
        <div class="overflow-x-auto">
          <table class="table">
            <thead>
              <tr>
                <th class="w-1">
                  <label class="flex flex-col gap-1">
                    <span class="text-[9px]">Update all<br />status</span>
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                      @change="(e) => updateTasksCompleted(e.target.checked)"
                    />
                  </label>
                </th>
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
                <th>
                  <label>
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                    />
                  </label>
                </th>
                <td>
                  <div class="flex items-center gap-3">
                    <div>
                      <div class="font-bold">Complete project proposal</div>
                      <div class="text-sm text-base-content/60">
                        Design & Development
                      </div>
                    </div>
                  </div>
                </td>
                <td>Today</td>
                <td><span class="badge badge-warning">Medium</span></td>
                <td>
                  <div class="flex flex-wrap gap-1">
                    <span class="badge badge-outline badge-sm">Work</span>
                    <span class="badge badge-outline badge-sm">Project</span>
                  </div>
                </td>
                <td>
                  <div class="flex gap-2">
                    <button class="btn btn-ghost btn-xs">Edit</button>
                    <button class="btn btn-ghost btn-xs text-error">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr>
                <th>
                  <label>
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                      checked
                    />
                  </label>
                </th>
                <td>
                  <div class="flex items-center gap-3">
                    <div>
                      <div class="font-bold">Team meeting</div>
                      <div class="text-sm text-base-content/60">
                        Weekly sync
                      </div>
                    </div>
                  </div>
                </td>
                <td>Yesterday</td>
                <td><span class="badge badge-success">Low</span></td>
                <td>
                  <div class="flex flex-wrap gap-1">
                    <span class="badge badge-outline badge-sm">Work</span>
                    <span class="badge badge-outline badge-sm">Meeting</span>
                  </div>
                </td>
                <td>
                  <div class="flex gap-2">
                    <button class="btn btn-ghost btn-xs">Edit</button>
                    <button class="btn btn-ghost btn-xs text-error">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
              <tr>
                <th>
                  <label>
                    <input
                      type="checkbox"
                      class="checkbox checkbox-primary checkbox-sm"
                    />
                  </label>
                </th>
                <td>
                  <div class="flex items-center gap-3">
                    <div>
                      <div class="font-bold">Client presentation</div>
                      <div class="text-sm text-base-content/60">
                        Prepare slides
                      </div>
                    </div>
                  </div>
                </td>
                <td>Tomorrow</td>
                <td><span class="badge badge-error">High</span></td>
                <td>
                  <div class="flex flex-wrap gap-1">
                    <span class="badge badge-outline badge-sm">Work</span>
                    <span class="badge badge-outline badge-sm">Urgent</span>
                  </div>
                </td>
                <td>
                  <div class="flex gap-2">
                    <button class="btn btn-ghost btn-xs">Edit</button>
                    <button class="btn btn-ghost btn-xs text-error">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
               -->
              <tr v-for="task in tasks" :key="task.id">
                <th>
                  <label>
                    <input
                      type="checkbox"
                      :checked="task.is_completed"
                      class="checkbox checkbox-primary checkbox-sm"
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
                  </label>
                </th>
                <td>
                  <div class="flex items-center gap-3">
                    <div>
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
                    class="badge"
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
                  <div v-if="task.tags.length" class="flex flex-wrap gap-1">
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
                    <Link
                      :href="`/task/edit/${task.id}`"
                      class="btn btn-ghost btn-xs"
                      >Edit</Link
                    >
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

    <!-- Pagination -->
    <div class="flex justify-center mt-6">
      <div class="join">
        <button
          @click="prevPage"
          v-if="page_obj.pagination.has_previous"
          class="join-item btn btn-sm btn-active"
        >
          <
        </button>

        <Link href="#">
          <button class="join-item btn btn-sm">
            {{ page_obj.pagination.current_page }}
          </button>
        </Link>
        <button
          @click="nextPage"
          v-if="page_obj.pagination.has_next"
          class="join-item btn btn-sm"
        >
          >
        </button>
      </div>
    </div>
  </div>
  <!-- End Tasks Page -->
</template>
