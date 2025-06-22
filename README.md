# Python Web Form Project

## 📄 Опис
Цей проєкт — простий веб-сервер на Python, який дозволяє користувачеві надіслати повідомлення через HTML-форму. Повідомлення зберігаються у форматі JSON.

## 📁 Структура
project/
├── main.py
├── index.html
├── message.html
├── error.html
├── style.css
├── Dockerfile
├── requirements.txt
└── storage/
└── data.json

## ▶️ Як запустити
1. Встановіть Python 3.10+.
2. Запустіть програму:
   ```bash
   python3 main.py
3. Відкрийте браузер і перейдіть на:

http://localhost:3000
4. Надсилання повідомлень
Перейдіть на "Send message"

Заповніть форму

Повідомлення збережеться в storage/data.json у форматі:
{
  "2025-06-22 10:37:24.498405": {
    "username": "@Natka",
    "message": "hi!"
  }
  "2025-06-22 11:43:24.190424": {
    "username": "@Natka",
    "message": "Hello, Docker!"
  },
  "2025-06-22 11:48:26.130001": {
    "username": "@Natka",
    "message": "Good bay!"
  }
 },

Технології
Python 3

HTTPServer + socketserver

HTML + CSS (Bootstrap)

# Simple UDP + HTTP Server with Docker

Цей проєкт містить простий HTTP-сервер та UDP socket-сервер на Python.  
HTTP-сервер приймає повідомлення через форму, UDP-сервер зберігає їх у JSON-файл з таймстампом.

---

## Особливості

- HTTP-сервер слухає на порту 3000
- UDP-сервер слухає на порту 6000 (порт можна змінити)
- Дані зберігаються у `storage/data.json`
- Збереження даних через Docker volume — щоб зберегти дані поза контейнером

---
## Як запускати локально

1. Створити папку `storage` поруч з `main.py`
2. Запустити скрипт:
   ```bash
   python3 main.py