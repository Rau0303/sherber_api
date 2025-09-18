🔐 Sheber API (Test Project)

Этот проект создан как тестовое/демо-приложение, чтобы показать работу с FastAPI, PostgreSQL, JWT-авторизацией и Docker.

🚀 Стек

FastAPI + Uvicorn

PostgreSQL + SQLAlchemy (async)

Alembic (миграции)

Pydantic

Docker + docker-compose

⚙️ Запуск
Локально
pip install -r requirements/base.txt
cp .env.example .env
uvicorn src.main:app --reload


Swagger: http://localhost:8000/docs

Через Docker
docker-compose up --build


Приложение: http://localhost:8000/docs

🔑 Эндпоинты Auth
Общий пример client:
{
  "platform": "ios",
  "os_version": "iOS 17.2",
  "app_version": "1.0.5",
  "app_build_version": "102",
  "locale": "ru-RU"
}

1. Регистрация пользователя

POST /auth/register
Описание: Создаёт пользователя и ClientInfo, возвращает JWT токен.

Request Body (RegisterSchema):

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


Response (AuthResponseSchema):

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

2. Логин по SMS

POST /auth/login/sms/verify
Описание: Подтверждает SMS-код и возвращает JWT токен.

Request Body (LoginWithSms):

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


Response (AuthResponseSchema):
Схема ответа аналогична регистрации.

3. Отправка SMS для входа

POST /auth/login/send/sms
Описание: Отправляет SMS-код пользователю.

Request Body (SendSms):

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


Response (SendSmsResponseSchema):

{
  "status": "success",
  "message": "SMS-код успешно отправлен"
}

4. Логин по паролю

POST /auth/login/password
Описание: Логин пользователя по телефону и паролю, возвращает JWT токен.

Request Body (LoginWithPassword):

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


Response (AuthResponseSchema):
Схема ответа аналогична регистрации.

⚠️ Возможные ошибки и статусы ответов
Исключение	HTTP статус	Сообщение
InvalidPhoneFormatException	422 Unprocessable Entity	Номер телефона должен быть в формате 7XXXXXXXXXX (11 цифр, без +).
InvalidSmsCodeException	401 Unauthorized	Введён неверный или просроченный SMS-код.
InvalidCredentialsException	401 Unauthorized	Неверный номер телефона или пароль.
EmailAlreadyExistsException	409 Conflict	Эта электронная почта уже зарегистрирована.
PhoneAlreadyExistsException	409 Conflict	Этот номер телефона уже зарегистрирован.
InternalServerError	500 Internal Server Error	Любые непредвиденные ошибки сервера.

Все эндпоинты /auth/* используют эти исключения для информирования клиента о проблемах при регистрации и логине.

