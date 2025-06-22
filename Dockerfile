FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Якщо є залежності, розкоментуй цей рядок
# RUN pip install -r requirements.txt

# Папку storage ти вже створюєш в коді, тому можна цей рядок прибрати або залишити
RUN mkdir -p /app/storage

EXPOSE 3000
EXPOSE 6000

CMD ["python3", "main.py"]
