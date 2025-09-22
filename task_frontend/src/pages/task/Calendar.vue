<script setup></script>
<template>
  <!-- Calendar Page -->
  <div id="calendar-page">
    <div class="mb-6">
      <h2 class="text-2xl font-bold">Calendar</h2>
      <p class="text-base-content/60">View your tasks by due date</p>
    </div>

    <div class="card bg-base-100 shadow-md">
      <div class="card-body">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-lg font-semibold">December 2023</h3>
          <div class="flex gap-2">
            <button class="btn btn-sm btn-ghost">
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
                  d="M15 19l-7-7 7-7"
                />
              </svg>
            </button>
            <button class="btn btn-sm btn-ghost">
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
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

        <div class="overflow-x-auto">
          <table class="table table-bordered text-center">
            <thead>
              <tr>
                <th class="py-3">Sun</th>
                <th class="py-3">Mon</th>
                <th class="py-3">Tue</th>
                <th class="py-3">Wed</th>
                <th class="py-3">Thu</th>
                <th class="py-3">Fri</th>
                <th class="py-3">Sat</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="py-4 text-base-content/30">26</td>
                <td class="py-4 text-base-content/30">27</td>
                <td class="py-4 text-base-content/30">28</td>
                <td class="py-4 text-base-content/30">29</td>
                <td class="py-4 text-base-content/30">30</td>
                <td class="py-4">1</td>
                <td class="py-4">2</td>
              </tr>
              <tr>
                <td class="py-4">3</td>
                <td class="py-4">4</td>
                <td class="py-4">5</td>
                <td class="py-4">6</td>
                <td class="py-4">7</td>
                <td class="py-4">8</td>
                <td class="py-4">9</td>
              </tr>
              <tr>
                <td class="py-4">10</td>
                <td class="py-4">11</td>
                <td class="py-4">12</td>
                <td class="py-4">13</td>
                <td class="py-4">14</td>
                <td class="py-4 bg-primary/10 relative">
                  <div>15</div>
                  <div
                    class="absolute bottom-1 left-0 right-0 flex justify-center"
                  >
                    <div class="badge badge-primary badge-xs"></div>
                  </div>
                </td>
                <td class="py-4">16</td>
              </tr>
              <tr>
                <td class="py-4">17</td>
                <td class="py-4">18</td>
                <td class="py-4">19</td>
                <td class="py-4">20</td>
                <td class="py-4">21</td>
                <td class="py-4">22</td>
                <td class="py-4">23</td>
              </tr>
              <tr>
                <td class="py-4">24</td>
                <td class="py-4 bg-secondary/10 relative">
                  <div>25</div>
                  <div
                    class="absolute bottom-1 left-0 right-0 flex justify-center"
                  >
                    <div class="badge badge-secondary badge-xs"></div>
                  </div>
                </td>
                <td class="py-4">26</td>
                <td class="py-4">27</td>
                <td class="py-4">28</td>
                <td class="py-4">29</td>
                <td class="py-4">30</td>
              </tr>
              <tr>
                <td class="py-4">31</td>
                <td class="py-4 text-base-content/30">1</td>
                <td class="py-4 text-base-content/30">2</td>
                <td class="py-4 text-base-content/30">3</td>
                <td class="py-4 text-base-content/30">4</td>
                <td class="py-4 text-base-content/30">5</td>
                <td class="py-4 text-base-content/30">6</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="mt-6">
          <h4 class="font-semibold mb-3">Tasks for Selected Date</h4>
          <div class="space-y-2">
            <div
              class="flex items-center justify-between p-2 bg-base-200 rounded"
            >
              <div>Complete project proposal</div>
              <div class="badge badge-warning badge-sm">Medium</div>
            </div>
            <div
              class="flex items-center justify-between p-2 bg-base-200 rounded"
            >
              <div>Team meeting</div>
              <div class="badge badge-success badge-sm">Low</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Calendar Page -->
</template>
