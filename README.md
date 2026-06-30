# ClientSup-help

ТЕХНИЧЕСКОЕ ЗАДАНИЕ: Административная панель ClientSup

1. Общие сведения

Проект представляет собой PWA-приложение для управления данными лидов, сертификации и настроек телеграм-бота. Система базируется на стеке Supabase (PostgreSQL + PostgREST).

2. Стек технологий

Frontend: HTML5, Tailwind CSS, JavaScript (Vanilla ES6+)

Database: Supabase (PostgreSQL)

API: PostgREST (через Supabase JS Client)

PWA: Стандартная реализация с манифестом для инсталляции

3. Структура БД и API-интеграция

База данных содержит три основные таблицы:

3.1. leads (Лиды)

Назначение: хранение данных пользователей, оставивших заявку.

Поля:

id: int8 (Primary Key)

full_name: text

phone: text

course: text

visit_date: text

created_at: timestamptz (default: now())

3.2. certificates (Сертификаты)

Назначение: учет выданных пользователям сертификатов по результатам теста.

Поля:

id: int8 (Primary Key)

full_name: text

phone: text

score: int4

created_at: timestamptz (default: now())

3.3. settings (Настройки)

Назначение: хранение JSON-конфигурации бота.

Поля:

id: int8 (Primary Key)

data: jsonb (Структура: {botName: string, botToken: string, courses: [], branches: [], questions: []})

4. Функциональные требования

Авторизация: локальная проверка учетных данных (admin/admin) с возможностью сохранения сессии через localStorage.

Интерфейс:

Разделы: Записи, Сертификаты, Настройки.

Поддержка тем: Dark/Light Mode.

PWA: Возможность установки приложения на мобильное устройство через браузер.

Логирование: Вывод статусов подключения таблиц в консоль браузера для диагностики сетевых ошибок (Failed to fetch).

5. Технические параметры доступа

Project URL: https://fgpvruxszhbijvjqpr.supabase.co

Anon Public Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZncHZydXhzenhiaWp2dmpxcHJtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI4NDI0NzMsImV4cCI6MjA5ODQxODQ3M30.paj3mpAANfmPSHhS3FUnJAYpMe8EyDR_-pDExmIkj7Q

Инициализация клиента:
supabase.createClient(SUPABASE_URL, SUPABASE_KEY, { auth: { persistSession: false } })

6. Безопасность

Использование RLS (Row Level Security).

Рекомендуемые политики: SELECT для anon роли, INSERT/UPDATE для authenticated.
