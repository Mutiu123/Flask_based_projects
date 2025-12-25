# Flask Masterclass: Full-Stack Web Applications & APIs

This repository features a suite of Flask applications, from core basics and Jinja2 templates to Flask-SQLAlchemy databases. It includes a Food Tracker, Q&A App, Weather App, and Dashboard. It also demonstrates backend proficiency through Registration and Member APIs, covering authentication, CRUD, and RESTful design.

## 🚀 Projects Overview

| Project | Key Features | Tech Stack |
| :--- | :--- | :--- |
| **Food Tracker** | Macro tracking, daily logs, date-based filtering | Flask, SQLAlchemy |
| **Weather App** | Real-time weather data via OpenWeatherMap API | Flask, Requests API |
| **Q&A App** | User roles (User/Expert) and question submission | Auth, Relationships |
| **Registration API** | Token-based authentication and user management | Flask-RESTful, JSON |
| **Dashboard App** | User metrics, protected routes, and sessions | Flask-Login |
| **Store App** | Product listings and shopping cart logic | Jinja2, CRUD |

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask
* **Database:** Flask-SQLAlchemy (SQLite)
* **Templating:** Jinja2, HTML5, CSS3
* **APIs:** RESTful Architecture, JSON, Requests library

---

## ⚙️ Installation & Setup

Follow these steps to run the projects locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME  

### 2. Create and Activate a Virtual Environment

**Windows (Command Prompt):**
```cmd
python -m venv flaskvenv
flaskvenv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv flaskvenv
.\flaskvenv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv flaskvenv
source flaskvenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install flask flask-sqlalchemy flask-login requests flask-restful
```

### 4. Run the Projects
Navigate to a specific project directory and run the application:

```bash
python app.py
```

## 📁 Directory Structure
```
├── Food_Tracker_App/
├── Weather_App/
├── QA_App/
├── Registration_API/
├── Dashboard_App/
├── static/          # Shared CSS, Images, JS
└── templates/       # Shared Jinja2 HTML files
```