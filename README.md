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
├── logo.png
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
}

Технології
Python 3

HTTPServer + socketserver

HTML + CSS (Bootstrap)