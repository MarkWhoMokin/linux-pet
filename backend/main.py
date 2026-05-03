from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Магия CORS: разрешаем браузеру делать запросы к API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешаем всем (для пет-проекта ок)
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv() # Загружает данные из файла .env

DB_PARAMS = {
    "host": "localhost",
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS")
}

@app.get("/tasks")
def get_tasks():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM tasks;")
        tasks = cur.fetchall()
        cur.close()
        conn.close()
        return tasks
    except Exception as e:
        return {"error": str(e)}
