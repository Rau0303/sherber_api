# 🔐 Sheber API (Test Project)

Тестовое/демо-приложение для демонстрации работы с **FastAPI**, **PostgreSQL**, **JWT-авторизацией** и **Docker**.

---

## 🚀 Стек

- **Backend:** FastAPI + Uvicorn  
- **База данных:** PostgreSQL + SQLAlchemy (асинхронный)  
- **Миграции:** Alembic  
- **Валидация/схемы:** Pydantic  
- **Контейнеризация:** Docker + docker-compose  

---

## ⚙️ Запуск проекта

### Локально

```bash
pip install -r requirements/base.txt
cp .env.example .env
uvicorn src.main:app --reload
```

**Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)  

### Через Docker

```bash
docker-compose up --build
```

**Приложение:** [http://localhost:8000/docs](http://localhost:8000/docs)  

---

## 🔑 Эндпоинты Auth

### Общий пример `client`

```json
{
  "platform": "ios",
  "os_version": "iOS 17.2",
  "app_version": "1.0.5",
  "app_build_version": "102",
  "locale": "ru-RU"
}
```

---

### 1️⃣ Регистрация пользователя

**POST** `/auth/register`  

- **Описание:** Создаёт пользователя и ClientInfo, возвращает JWT токен.  

**Request Body (`RegisterSchema`):**

```json
{
  "phone": "77011234567",
  "password": "My$ecureP@ssw0rd",
  "email": "user@example.com",
  "client": {
    "platform": "ios",
    "os_version": "iOS 17.2",
    "app_version": "1.0.5",
    "app_build_version": "102",
    "locale": "ru-RU"
  }
}
```

**Response (`AuthResponseSchema`):**

```json
{
  "status": "success",
  "data": {
    "user": {
      "id": 123,
      "phone": "77011234567",
      "email": "user@example.com"
    },
    "access_token": "jwt_token",
    "token_type": "bearer"
  }
}
```

---

### 2️⃣ Логин по SMS

**POST** `/auth/login/sms/verify`  

- **Описание:** Подтверждает SMS-код и возвращает JWT токен.  

**Request Body (`LoginWithSms`):**

```json
{
  "phone": "77777777777",
  "sms_code": "2002",
  "client": {
    "platform": "ios",
    "os_version": "iOS 17.2",
    "app_version": "1.0.5",
    "app_build_version": "102",
    "locale": "ru-RU"
  }
}
```

- **Response:** аналогично регистрации.

---

### 3️⃣ Отправка SMS для входа

**POST** `/auth/login/send/sms`  

- **Описание:** Отправляет SMS-код пользователю.  

**Request Body (`SendSms`):**

```json
{
  "phone": "77011234567",
  "client": {
    "platform": "ios",
    "os_version": "iOS 17.2",
    "app_version": "1.0.5",
    "app_build_version": "102",
    "locale": "ru-RU"
  }
}
```

**Response (`SendSmsResponseSchema`):**

```json
{
  "status": "success",
  "message": "SMS-код успешно отправлен"
}
```

---

### 4️⃣ Логин по паролю

**POST** `/auth/login/password`  

- **Описание:** Логин пользователя по телефону и паролю, возвращает JWT токен.  

**Request Body (`LoginWithPassword`):**

```json
{
  "phone": "77011234567",
  "password": "My$ecureP@ssw0rd",
  "client": {
    "platform": "ios",
    "os_version": "iOS 17.2",
    "app_version": "1.0.5",
    "app_build_version": "102",
    "locale": "ru-RU"
  }
}
```

- **Response:** аналогично регистрации.

---

## ⚠️ Возможные ошибки

| Исключение                    | HTTP статус | Сообщение                                        |
| ----------------------------- | ----------- | ------------------------------------------------ |
| `InvalidPhoneFormatException` | 422         | Номер телефона должен быть в формате 7XXXXXXXXXX |
| `InvalidSmsCodeException`     | 401         | Введён неверный или просроченный SMS-код         |
| `InvalidCredentialsException` | 401         | Неверный номер телефона или пароль               |
| `EmailAlreadyExistsException` | 409         | Эта электронная почта уже зарегистрирована       |
| `PhoneAlreadyExistsException` | 409         | Этот номер телефона уже зарегистрирован          |
| `InternalServerError`         | 500         | Любые непредвиденные ошибки сервера              |

> Все эндпоинты `/auth/*` используют эти исключения для информирования клиента о проблемах при регистрации и логине.
