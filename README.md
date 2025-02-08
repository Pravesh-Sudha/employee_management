# Employee Management System (Django)

## Overview
This is a **Django-based Employee Management System** that provides **CRUD operations** (Create, Read, Update, Delete) for employee records. The application includes a web UI for managing employee data and is containerized using **Docker**.

## Features
- List all employees in a well-styled table.
- Add new employees.
- Delete employees.
- Integrated with **MySQL (AWS RDS)** for persistent data storage.
- Containerized using **Docker** for easy deployment.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: MySQL (AWS RDS or Local MySQL)
- **Containerization**: Docker

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/django-employee-management.git
cd django-employee-management
```

### 2. Set Up a Virtual Environment
```sh
python -m venv django-env
source django-env/bin/activate  # On macOS/Linux
# or
django-env\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Database (MySQL)
Update the `DATABASES` settings in `employee_management/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee-db',
        'USER': 'admin',
        'PASSWORD': 'your-password',
        'HOST': 'database-1.XXXXXXXX.eu-north-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server
```sh
python manage.py runserver
```
Go to **[http://127.0.0.1:8000](http://127.0.0.1:8000)** to access the app.

---

## Running with Docker

### 1. Build the Docker Image
```sh
docker build -t employee_management .
```

### 2. Run the Docker Container
```sh
docker run -p 8000:8000 employee_management
```

### 3. Open in Browser
Visit **[http://localhost:8000](http://localhost:8000)**

---

## Running with Docker Compose
If using **AWS RDS**, create a `docker-compose.yml` file:
```yaml
version: '3.8'

services:
  django_app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DB_NAME=employee-db
      - DB_USER=admin
      - DB_PASSWORD=your-password
      - DB_HOST=database-1.xxxxxx.rds.amazonaws.com
      - DB_PORT=3306
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
```
Run with:
```sh
docker-compose up --build
```

---

## License
This project is licensed under the MIT License.

