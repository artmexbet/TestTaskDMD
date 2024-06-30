# Dockerfile-backend
# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /backend

# Копируем файлы проекта в рабочую директорию
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]