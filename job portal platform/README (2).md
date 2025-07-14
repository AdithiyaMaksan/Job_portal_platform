# 🧑‍💼 Job Portal Platform

A full-stack web application built using **Python Django** and **Django REST Framework (DRF)** that enables job seekers to find jobs and apply for them, while allowing companies to post jobs and manage applications.

---

## 📌 Features

- 👤 User registration and login
- 🧑‍💼 Company profile management
- 📄 Job listing and application submission
- 📤 Resume upload
- 🛠️ Admin dashboard for management
- 🔗 REST APIs for all core features (DRF)

---

## ⚙️ Tech Stack

| Technology | Purpose                |
|------------|------------------------|
| Python     | Backend Language       |
| Django     | Web Framework          |
| DRF        | REST API Integration   |
| SQLite     | Default Database       |
| HTML/CSS   | Templating             |
| Bootstrap  | Frontend Styling       |

---

## 📂 Project Structure

```
jobportal/
├── core/                  # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── templates/
├── jobportal/             # Django project config
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## 🔌 REST API Endpoints

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | `/api/jobs/`         | List all jobs            |
| POST   | `/api/jobs/`         | Create new job           |
| GET    | `/api/companies/`    | List all companies       |
| GET    | `/api/applications/` | List all applications    |

> API powered by **Django REST Framework**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jobportal.git
cd jobportal
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Access the site at: `http://127.0.0.1:8000/`

---

## 🛠 Usage

- Register a user or login as a company
- Companies can post jobs
- Users can view and apply to jobs
- Admin can manage users, jobs, and applications

---

## 🔐 Authentication

- Django's built-in user model
- Can be extended for JWT auth (optional)

---

## 📈 Future Enhancements

- ✅ JWT-based login system
- ✅ Role-based access (Jobseeker vs Company)
- ✅ Filtering & search on jobs
- ✅ Resume parsing and job recommendation
- ✅ React.js frontend or mobile app integration

---

## 📄 License

This project is open-source and free to use.

---

## ✉️ Contact

Made with ❤️ by [Your Name] – Open to freelance and full-time opportunities.  
Email: your.email@example.com  
LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)

---