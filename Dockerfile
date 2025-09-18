FROM python:3.12-slim

# рабочая директория
WORKDIR /app

# Устанавливаем системные зависимости (для psycopg2 и других пакетов)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# зависимости
COPY requirements/base.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# копируем весь проект
COPY . .

# команда запуска (если точка входа main.py в src)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
