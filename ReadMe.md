# TaskFlow - Personal Task Manager

TaskFlow is a modern, full-stack personal task manager designed to help you organize tasks, boost productivity, and manage your day-to-day activities with ease. Built with Django, Vue.js, TailwindCSS, and DaisyUI.

## Features

- 📝 **Easy Task Creation:** Create, edit, and delete tasks with a simple, intuitive interface.
- 📅 **Calendar View:** Visualize your tasks and deadlines in a beautiful calendar layout.
- 🏷️ **Tag & Categorize:** Organize tasks with custom tags and categories for easy filtering.
- 🔒 **Secure Authentication:** Register, login, and manage your profile securely.
- ⚡ **Fast & Responsive UI:** Built with Vue.js, TailwindCSS, and DaisyUI for a seamless experience.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Vue.js (Vite)
- **Styling:** TailwindCSS & DaisyUI
- **Database:** SQLite (default, easily swappable)

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js & pnpm (or npm/yarn)

### Backend Setup

1. Install Python dependencies:
	```sh
	pip install -r requirements.txt
	```
2. Run migrations:
	```sh
	python manage.py migrate
	```
3. Start the Django server:
	```sh
	python manage.py runserver
	```

### Frontend Setup

1. Navigate to `task_frontend`:
	```sh
	cd task_frontend
	```
2. Install dependencies:
	```sh
	pnpm install
	# or npm install
	```
3. Start the Vite dev server:
	```sh
	pnpm run dev
	# or npm run dev
	```

## Usage

- Access the app at `http://localhost:8000` (Django backend)
- Frontend runs at `http://localhost:5173` during development
- Register, login, and start managing your tasks!

## Folder Structure

- `authentication/` - User authentication (login, register, profile)
- `task/` - Task management (CRUD, calendar, tags)
- `task_frontend/` - Vue.js frontend
- `templates/` - Django HTML templates
- `static/` - Static files (built frontend)

## Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.

## License

MIT License

---
Made with ❤️ by TaskFlow contributors.
