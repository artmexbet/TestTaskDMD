# Тестовое задание
## Запуск
### Без Docker
#### Запуск сервера
1. Убедиться, что у Вас запущен PostgreSQL
2. Установить зависимости
```bash
cd backend
pip install -r requirements.txt
```
3. Изменить настройки подключения к БД в файле `backend/settings.py`
4. Применить миграции
```bash
python manage.py migrate
```
5. Запустить сервер
```bash
python manage.py runserver
```
#### Запуск клиента
1. Установить зависимости
```bash
cd frontend
npm install
```
2. Запустить клиент
```bash
npm run build
npm start
```
### С Docker
1. Изменить настройки подключения к БД в файле `backend/settings.py`
   (нужно изменить `HOST` на `database`)
2. Запустить docker-compose
```bash
docker-compose up -d
```