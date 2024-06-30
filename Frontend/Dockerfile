# Dockerfile-frontend
# Используем официальный образ Node.js
FROM node:18

# Устанавливаем рабочую директорию в контейнере
WORKDIR /frontend

# Копируем файлы проекта в рабочую директорию
COPY . .

# Устанавливаем зависимости
RUN npm install

# Запускаем сервер
CMD ["npm", "run", "serve"]