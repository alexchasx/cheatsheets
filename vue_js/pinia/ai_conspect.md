## Конспект по Pinia (store для Vue.js)

Pinia — это библиотека для управления состоянием (state management) в Vue 3 (и Vue 2 с совместимостью). Она стала официальной рекомендацией Vue вместо Vuex и построена с учётом TypeScript, Composition API и простоты.

---

## Зачем нужна Pinia

- Централизованное хранение данных, которые нужны в разных компонентах.
- Упрощённая типизация (особенно с TypeScript).
- Лучшая модульность: несколько независимых сторов вместо одного большого.
- Более понятный API по сравнению с Vuex.
- Поддержка SSR (Server-Side Rendering) «из коробки».

Учитывая твой стек (Vue 3 + TypeScript + Laravel), Pinia отлично ложится в проект: типизированные сторы упрощают работу с данными от бэкенда, а модульная структура помогает масштабировать приложение.

---

## Базовая архитектура

- **Store** — модуль состояния. В Pinia это функция `defineStore`, которая возвращает объект со свойствами и методами.
- **State** — данные (аналог `state` в Vuex).
- **Getters** — вычисляемые значения на основе state (аналог getters).
- **Actions** — логика (запросы, мутации, бизнес-логика). В Pinia нет отдельных «мутаций»: изменения происходят внутри actions или напрямую.
- **Один стор = один файл** (или одна функция), что удобно для организации кода.

---

## Минимальный пример

```ts
// stores/counter.ts
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)

  function increment() {
    count.value++
  }

  return { count, increment }
})
```

Использование в компоненте (Vue 3 + script setup):

```vue
<script setup lang="ts">
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>

<template>
  <button @click="counter.increment">{{ counter.count }}</button>
</template>
```

---

## State

- Объявляется как реактивные переменные (`ref`, `reactive`).
- В отличие от Vuex, нет необходимости использовать `state: () => ({ ... })` — можно сразу `const`.
- State автоматически становится реактивным благодаря Vue.

Пример с объектом:

```ts
const user = reactive({ id: 0, name: '' })
```

---

## Getters

Getters — это функции, возвращающие вычисляемое значение. Они принимают `state` как первый аргумент.

```ts
export const useUserStore = defineStore('user', () => {
  const user = ref<{ id: number; name: string } | null>(null)

  const isLoggedIn = computed(() => !!user.value)
  const displayName = computed(() => user.value?.name ?? 'Гость')

  // Getter как функция (если нужны аргументы)
  function hasPermission(permission: string) {
    return user.value?.permissions?.includes(permission) ?? false
  }

  return { user, isLoggedIn, displayName, hasPermission }
})
```

В шаблоне: `{{ userStore.isLoggedIn }}`, в JS: `userStore.hasPermission('edit')`.

---

## Actions

Actions — это методы для логики: запросы к API, валидации, сложные изменения состояния.

```ts
function login(email: string, password: string) {
  // можно делать async/await
  const response = await api.login(email, password)
  user.value = response.user
}
```

Особенности:
- Можно быть асинхронными.
- Могут вызывать другие actions.
- Не нужно разделять на «actions» и «mutations»: изменение state делается прямо в action.

---

## Типизация в TypeScript

Pinia хорошо дружит с TypeScript. Есть несколько подходов:

1. **Автоматический вывод типов** (самый простой):

   ```ts
   const store = defineStore('name', () => ({
     count: ref(0),
     increment() { count.value++ }
   }))
   ```

2. **Явная типизация через интерфейсы** (удобно для больших сторов):

   ```ts
   interface CounterState { count: number }
   export const useCounterStore = defineStore<CounterState>('counter', () => ({
     count: ref(0),
     // getters/actions добавляются отдельно
   }))
   ```

3. **Типизация actions/getters отдельно** — часто удобнее, когда стор растёт.

Для твоего стека (Vue 3 + TS) лучше сразу делать сторы с явной типизацией состояния и сигнатурами функций: это поможет при работе с API Laravel и уменьшит ошибки при передаче данных в компоненты.

---

## Composition и переиспользование

Можно выносить логику в отдельные функции и компоновать их в сторе:

```ts
function createAuthMethods() {
  const token = ref<string | null>(null)
  function setToken(t: string) { token.value = t }
  function clearToken() { token.value = null }
  return { token, setToken, clearToken }
}

export const useAuthStore = defineStore('auth', () => {
  const { token, setToken, clearToken } = createAuthMethods()
  // другие методы...
  return { token, setToken, clearToken }
})
```

Это удобно, если логика авторизации или работы с API становится большой.

---

## Несколько сторов и связи между ними

- Каждый домен (auth, cart, user, products) — свой стор.
- Сторы могут импортировать и вызывать друг друга:

  ```ts
  import { useUserStore } from './user'

  function logout() {
    const user = useUserStore()
    user.clear()
    // ...
  }
  ```

Важно: не создавать циклические импорты (A импортирует B, B импортирует A). Если нужно, выноси общую логику в утилиты.

---

## Persistence (сохранение в localStorage / sessionStorage)

Часто нужно сохранять состояние между перезагрузками (например, корзину, авторизацию). Для этого используют плагин `pinia-plugin-persisted-state`:

```bash
npm install pinia-plugin-persisted-state
```

```ts
import { createPinia } from 'pinia'
import persistedState from 'pinia-plugin-persisted-state'

const pinia = createPinia()
pinia.use(persistedState)
```

В сторе:

```ts
defineStore('cart', () => {
  const items = ref<Product[]>([])
  return {
    items,
    persist: {
      storage: window.localStorage,
      key: 'cart_items',
    },
  } as const
})
```

---

## SSR (Server-Side Rendering)

Если используешь Nuxt.js (ты интересовался им ранее) или SSR-режим Vue, Pinia поддерживает SSR:

- Используй `useStore()` в компонентах — он корректно работает на сервере и клиенте.
- На сервере создаётся новый экземпляр стора для каждого запроса.
- Данные сторов можно сериализовать и передавать на клиент (в Nuxt это автоматизировано).

---

## Отличия от Vuex

| Что | Vuex | Pinia |
| --- | --- | --- |
| Мутации | Отдельный слой (`commit`) | Нет: изменения в actions или напрямую |
| Типизация | Сложнее | Проще, нативная поддержка TS |
| Модульность | Модули, но всё в одном сторе | Множество независимых сторов |
| API | Более громоздкий | Лаконичный, Composition API-стиль |
| SSR | Требует дополнительной настройки | Работает «из коробки» |

---

## Практические советы под твой стек

- **Для API Laravel**: делай сторы под сущности (`useProductsStore`, `useOrdersStore`) и выноси HTTP-запросы в actions. Так проще тестировать и поддерживать.
- **Типизируй ответы API**: используй интерфейсы/types для DTO из Laravel и возвращай их из actions.
- **Разделяй логику**: auth, cart, filters — отдельные сторы.
- **Не храни лишнее в сторе**: большие списки лучше кэшировать в сторе, а мелкие данные (фильтры, пагинация) можно держать в сторе или передавать через props/provide.
- **Тестируй actions**: так как это обычные функции, их легко тестировать юнит-тестами.

---

## Частые ошибки

- Пытаться использовать `pinia` без инициализации в `main.ts` (нужно создать `pinia` и передать в `app.use(pinia)`).
- Забывать, что `defineStore` нужно вызывать только один раз: `useSomeStore()` — это хук, который возвращает один и тот же экземпляр.
- Смешивать реактивность: не оборачивать уже реактивные значения в `ref` повторно.
- Игнорировать типизацию в больших проектах: потом сложно поддерживать.