# 🤖 ast-manager-bot

Телеграм-бот для автоматизации управления заказами, пользователями и расчетами в магазине, использующий данные из Google Sheets и базу данных PostgreSQL.

## 🚀 Возможности

- 📌 Приветственное сообщение и автоматическое добавление пользователя или группы
- 📦 Работа с пользователями: добавление, поиск, просмотр с пагинацией
- 🧮 Расчет стоимости вышивки по типу изделия и времени
- 🔎 Inline-запросы для быстрого получения информации прямо из строки поиска Telegram
- 🗃 Хранилище данных на базе PostgreSQL с миграциями через Alembic
- 🐳 Поддержка запуска в Docker
- ✅ Покрытие тестами с использованием PyTest
- ⚙️ Автоматический деплой через GitHub Actions

## 📁 Структура проекта

- `main.py` — точка входа
- `commands/` — обработчики команд (`/start`, `/users`)
- `button_handlers/` — обработчики кнопок (pagination и др.)
- `inline_query_handlers/` — обработчики inline-запросов (расчет цены)
- `crud/` — доступ к данным пользователей
- `models/` — SQLAlchemy модели (User)
- `services/` — интеграции (БД, Google Sheets)
- `texts/` — текстовые шаблоны
- `utils/` — утилиты (pagination, форматирование и др.)
- `tests/` — unit-тесты
- `migrations/` — миграции Alembic

## 🔧 Настройка переменных окружения
Создайте файл .env по примеру:

```
BOT_TOKEN=токен_бота

GOOGLE_TYPE=service_account
GOOGLE_PROJECT_ID=...
GOOGLE_PRIVATE_KEY_ID=...
GOOGLE_PRIVATE_KEY=...
GOOGLE_CLIENT_EMAIL=...
GOOGLE_CLIENT_ID=...
GOOGLE_AUTH_URI=...
GOOGLE_TOKEN_URI=...
GOOGLE_AUTH_PROVIDER_X509_CERT_URL=...
GOOGLE_CLIENT_X509_CERT_URL=...
GOOGLE_UNIVERSE_DOMAIN=...

GOOGLE_SHEET_KEY=ключ_таблицы
DATABASE_URL=postgresql://user:password@host:port/db
```

## 🧬 CI/CD
Проект включает автоматический деплой через GitHub Actions:
* Проверка кода
* Запуск тестов
* Сборка Docker-образа
* Публикация в DockerHub
* Деплой на сервер через SSH

