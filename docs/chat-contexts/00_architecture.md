# Контекст проекта Losk Space

## Что за проект
Аналитический сервис по новостройкам Москвы. Помогает покупателям
выбирать квартиры через персональный коэффициент комфорта и расчёт
финансовых стратегий. Проект портфолио / стартап, разрабатывается
одним человеком (студент 1 курса МИФИ, Python/Docker/Git/CI-CD).

## Стек (зафиксирован, не обсуждаем)
- Backend: FastAPI + SQLAlchemy + Alembic + PostgreSQL + PostGIS
- Фоновые задачи: Celery + Redis
- Frontend: Next.js (React, TypeScript)
- Инфраструктура: Docker Compose, GitHub Actions
- ML (этап 4, далеко): scikit-learn / CatBoost

## Структура репозитория
losk-space/
├── backend/
│   ├── app/
│   │   ├── api/v1/          # эндпоинты
│   │   ├── models/          # SQLAlchemy модели
│   │   ├── schemas/         # Pydantic схемы
│   │   ├── services/        # бизнес-логика
│   │   └── tasks/           # Celery задачи
│   ├── alembic/
│   └── main.py
├── frontend/
├── ml/
├── docs/
│   ├── architecture.md
│   ├── known-risks.md
│   └── chat-contexts/
└── docker-compose.yml

## API (зафиксировано)
/api/v1/properties/              GET  — список с фильтрами
/api/v1/properties/{id}/         GET  — карточка
/api/v1/properties/{id}/history/ GET  — история цен
/api/v1/calculator/mortgage/     POST — ипотека
/api/v1/calculator/installment/  POST — рассрочка
/api/v1/comfort/score/           POST — коэффициент комфорта
/api/v1/strategies/              POST — ML стратегии (этап 4)

## Этапы (roadmap)
1. Фундамент: Docker, БД, модели, парсинг тестового XML — СЕЙЧАС
2. Калькулятор ипотеки/рассрочки + базовый UI
3. Подключение реальных XML-фидов застройщиков
4. Коэффициент комфорта (PostGIS, расстояния)
5. ML-стратегии погашения

## Ключевые решения (не пересматриваем)
- История цен — отдельная таблица PriceHistory, не JSONB
- Идентификатор квартиры — (корпус + этаж + номер + площадь), не внешний id
- Celery задачи идемпотентны (повторный запуск = безопасно)
- Версионирование API с /v1/ с самого начала
- Django Admin не используем — только FastAPI

## Известные риски (см. docs/known-risks.md)
- XML-фиды у каждого застройщика свой формат
- PostGIS: расстояние по прямой ≠ пешком, явно указываем в UI
- Коэффициент комфорта — инструмент исследования, не рекомендация

## Задача в этом чате
[ОПИШИ СЮДА конкретную задачу — модуль, вопрос, код]