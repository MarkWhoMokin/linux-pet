# 📝 To-Do Pet Project

> Учебный проект по администрированию Linux, настройке веб-серверов и разработке REST API.
> Простой менеджер задач на основе клиент-серверной архитектуры.

---

## 🏗️ Архитектура

| Слой | Технология |
|------|-----------|
| **Frontend** | HTML + Vanilla JS |
| **Backend** | Python · FastAPI · Uvicorn |
| **Database** | PostgreSQL |
| **Web Server** | Nginx (статика + Reverse Proxy) |

---

## 🚀 Быстрый старт

### Подготовка системы

```bash
sudo apt update
sudo apt install python3-venv python3-pip postgresql nginx -y
```

---

## 1. 🗄️ База данных (PostgreSQL)

Войдите в консоль PostgreSQL:

```bash
sudo -u postgres psql
```

Создайте БД, пользователя и таблицу:

```sql
-- Создание базы данных и пользователя
CREATE DATABASE todo_db;
CREATE USER todo_user WITH PASSWORD 'ваш_пароль';
GRANT ALL PRIVILEGES ON DATABASE todo_db TO todo_user;

-- Создание таблицы задач
CREATE TABLE tasks (
    id        SERIAL PRIMARY KEY,
    title     VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
```

---

## 2. ⚙️ Бэкенд (FastAPI)

Перейдите в папку бэкенда, создайте и активируйте виртуальное окружение:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> 💡 **Совет:** не забудьте сгенерировать `requirements.txt` перед первым коммитом:
> ```bash
> pip freeze > requirements.txt
> ```

**Запуск сервера:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 3. 🌐 Фронтенд (Nginx)

Разместите статику и настройте доступ:

```bash
# Удалить стандартную страницу Nginx
sudo rm /var/www/html/index.nginx-debian.html

# Скопировать фронтенд
sudo cp ~/linux-pet/frontend/index.html /var/www/html/index.html

# Выставить права
sudo chmod 644 /var/www/html/index.html

# Открыть порты в фаерволе
sudo ufw allow 'Nginx Full'
```

---

## ✅ Использование

1. Убедитесь, что бэкенд запущен (`uvicorn`).
2. Откройте браузер и перейдите по IP-адресу сервера:

```
http://<IP-адрес-сервера>
```

---

## 📁 Структура проекта

```
linux-pet/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── venv/
├── frontend/
│   └── index.html
└── README.md
```

