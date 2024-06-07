# Используем официальный образ Python
FROM python:3.10

# Устанавливаем зависимости
RUN apt-get update \
    && apt-get install -y postgresql-client \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Открываем порт для сервера
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hope_project.wsgi:application"]
