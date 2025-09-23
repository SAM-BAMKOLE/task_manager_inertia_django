<script setup>
import { useForm, Head } from "@inertiajs/vue3";
import { ref } from "vue";
import { addTagToSelected, removeTagFromSelected } from "../../utils/helpers";
const selectedTags = ref([]);
const curTypedTag = ref("");
const form = useForm({
  title: "",
  due_date: "",
  priority: "MEDIUM",
  tags: selectedTags.value,
  description: "",
});

defineProps({
  title: String,
  description: String,
  errors: Object,
});

function removeTag(key) {
  removeTagFromSelected(key, selectedTags);
}
function addTag() {
  addTagToSelected(curTypedTag, selectedTags);
}

const onSubmit = () => {
  form.tags = [...selectedTags.value];
  form.post("/task/create/", { forceFormData: true });
};
</script>
<template>
  <!-- Task Create Page -->
  <Head>
    <title>{{ title }}</title>
    <meta name="description" :content="description" />
  </Head>

  <div id="task-create-page">
    <div class="mb-6">
      <h2 class="text-2xl font-bold">Create New Task</h2>
      <p class="text-base-content/60">Add a new task to your list</p>
    </div>

    <div class="card bg-base-100 shadow-md">
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl">
            <div class="form-control flex flex-col gap-1">
              <label class="label">
                <span class="label-text">Task Title</span>
              </label>
              <input
                type="text"
                placeholder="Enter task title"
                class="input input-bordered w-full"
                v-model="form.title"
                required
              />
              <ul
                class="list-inside text-xs text-red-500 font-medium list-disc"
                v-if="form.errors?.title?.length"
              >
                <li
                  class=""
                  v-for="(error, key) in form.errors.title"
                  :key="key"
                >
                  {{ error }}
                </li>
              </ul>
            </div>
            <div class="form-control flex flex-col gap-1">
              <label class="label">
                <span class="label-text">Due Date</span>
              </label>
              <input
                type="date"
                class="input input-bordered w-full"
                v-model="form.due_date"
              />
              <ul
                class="list-inside text-xs text-red-500 font-medium list-disc"
                v-if="form.errors?.due_date?.length"
              >
                <li
                  class=""
                  v-for="(error, key) in form.errors.due_date"
                  :key="key"
                >
                  {{ error }}
                </li>
              </ul>
            </div>
            <div class="form-control flex flex-col gap-1">
              <label class="label">
                <span class="label-text">Priority</span>
              </label>
              <select
                class="select select-bordered w-full"
                v-model="form.priority"
              >
                <option value="LOW">Low</option>
                <option value="MEDIUM" selected>Medium</option>
                <option value="HIGH">High</option>
              </select>
              <ul
                class="list-inside text-xs text-red-500 font-medium list-disc"
                v-if="form.errors?.priority?.length"
              >
                <li
                  class=""
                  v-for="(error, key) in form.errors.priority"
                  :key="key"
                >
                  {{ error }}
                </li>
              </ul>
            </div>
            <div class="form-control flex flex-col gap-1">
              <label class="label">
                <span class="label-text">Tags</span>
              </label>

              <div class="space-y-1 flex items-center gap-3">
                <div
                  v-if="selectedTags.length"
                  class="flex flex-wrap w-full items-center text-xs gap-1"
                >
                  <div
                    v-for="(tag, key) in selectedTags"
                    :key="key"
                    class="badge badge-soft rounded"
                  >
                    <span>{{ tag }}</span>
                    <button
                      type="button"
                      class="font-semibold cursor-pointer"
                      @click="removeTag(key)"
                    >
                      x
                    </button>
                  </div>
                </div>
                <div
                  class="input input-bordered flex flex-1 items-center justify-between"
                >
                  <input
                    type="text"
                    class="w-full"
                    v-model="curTypedTag"
                    placeholder="You can add at most 4 tags"
                  />
                  <button type="button" class="cursor-pointer" @click="addTag">
                    ✔️
                  </button>
                </div>
              </div>
              <ul
                class="list-inside text-xs text-red-500 font-medium list-disc"
                v-if="form.errors?.tags?.length"
              >
                <li
                  class=""
                  v-for="(error, key) in form.errors.tags"
                  :key="key"
                >
                  {{ error }}
                </li>
              </ul>
            </div>
            <div class="form-control flex flex-col gap-1 md:col-span-2">
              <label class="label">
                <span class="label-text">Description</span>
              </label>
              <textarea
                class="textarea textarea-bordered w-full h-24"
                v-model="form.description"
                placeholder="Task description"
              ></textarea>
              <ul
                class="list-inside text-xs text-red-500 font-medium list-disc"
                v-if="form.errors?.description?.length"
              >
                <li
                  class=""
                  v-for="(error, key) in form.errors.description"
                  :key="key"
                >
                  {{ error }}
                </li>
              </ul>
            </div>
          </div>
          <div class="form-control mt-6">
            <button
              :disabled="form.processing"
              type="submit"
              class="btn btn-primary"
            >
              Create Task
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!-- End Task Create Page -->
</template>

<!-- 
<select
                class="select select-bordered w-full"
                v-model="form.tags"
                multiple
              >
                <option>Work</option>
                <option>Personal</option>
                <option>Urgent</option>
                <option>Project</option>
              </select>
-->
