# src/auth/descriptions.py

REGISTER_DESCRIPTION = "Регистрация нового пользователя. Возвращает JWT токен и информацию о пользователе."
LOGIN_SMS_DESCRIPTION = "Вход пользователя по SMS-коду. Возвращает JWT токен и информацию о пользователе."
LOGIN_PASSWORD_DESCRIPTION = "Вход пользователя по паролю. Возвращает JWT токен и информацию о пользователе."
FORGOT_PASSWORD_DESCRIPTION = "Запрос на сброс пароля. Отправляет код на email."
RESET_PASSWORD_DESCRIPTION = "Подтверждение сброса пароля и установка нового."
