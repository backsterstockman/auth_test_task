# 🚀 FastAPI Access-Controlled API

## 📌 Описание

Проект — API на FastAPI с авторизацией через JWT и кастомной системой прав доступа на основе ролей и ресурсов. Все эндпоинты защищены, а доступ регулируется через таблицу `permissions`.

---

## 🛠️ Технологии

- **FastAPI** — высокопроизводительный API-фреймворк
- **PostgreSQL** — реляционная база данных
- **SQLAlchemy** — ORM для взаимодействия с БД


## 🗃️ Структура базы данных

### users

- `id`: UUID
- `email`: str
- `hashed_password`: str
- `role`: str (например, "user", "admin")

### permissions

- `id`: UUID
- `resource`: str (`/users`, `/permissions`, `/resumes`, и т.д.)
- `role`: str
- `is_allowed`: bool

### resumes

- `id`: UUID
- `user_id`: int (id пользователя)
- `about_me`: str
- `job_time`: str
- `salary`: int

---

## ⚙️ Развёртывание

### 1. Клонируй репозиторий

```bash
git clone https://github.com/backsterstockman/auth_test_task
cd auth_test_task
```

### 2. Создай .env

```bash
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=auth
SECRET_KEY=vladislavyaroshuk
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Запусти проект через docker

```bash
docker-compose up --build
```

### 4. Открой проект в браузере по localhost:8000/docs


## Проверка работы

Admin может использовать любые методы приложения.  
User не имеет доступа по точкам с префиксом permissions.


### 1. Авторизация

```
Авторизуйся под данными(админ)
john.doe@example.com
password
```

### 2. Проверь работу методов

### 3. Зарегистрируйся при помощи метод register (пользователь)

### 4. Проверь работу методов

