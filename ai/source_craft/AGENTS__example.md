# Правила проекта для AI-агента

## Стек
- Backend: Laravel 11, PHP 8.3
- Frontend: Vue 3 (Composition API + `<script setup>`), TypeScript, Vue Router 4
- Стили: Tailwind CSS

## Соглашения по коду
- Vue-компоненты: PascalCase имена файлов и компонентов (Button.vue, UserProfile.vue)
- Props: camelCase (userProfile, isActive)
- TypeScript: использовать интерфейсы/типы в папке types/, избегать any
- Laravel: контроллеры в app/Http/Controllers/, ресурсы API в app/Http/Resources/

## Что нельзя делать
- Не добавлять новые зависимости без согласования
- Не менять формат миграции БД без отдельной задачи
- Не удалять тесты без замены

## Команды для агента
- Запуск: `docker compose up -d` или `php artisan serve` + `npm run dev`
- Тесты: `php artisan test` и `npm run test`
