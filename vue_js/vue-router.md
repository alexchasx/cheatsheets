## Конспект по Vue Router для Vue 3

Учитывая твой стек (Vue 3, TypeScript, Pinia, Laravel), Vue Router — это стандартный роутер, который даёт декларативную навигацию, динамическую подгрузку страниц и удобную работу с URL. Ниже — структурированный конспект: от установки до продвинутых кейсов.

---

## Установка и базовая настройка

```bash
npm install vue-router@4
```

**Точка входа (`main.ts`):**
```ts
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import routes from './router/routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // history mode (без #)
  routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')
```

`routes` — это массив объектов, где каждый маршрут описывает путь и компонент.

---

## Описание маршрутов (routes)

Пример `src/router/routes.ts`:
```ts
import type { RouteRecordRaw } from 'vue-router'
import Home from '@/views/Home.vue'
import Products from '@/views/Products.vue'
import ProductDetail from '@/views/ProductDetail.vue'

export const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/products',
    name: 'products',
    component: Products,
  },
  {
    path: '/products/:id', // динамический параметр
    name: 'product-detail',
    component: ProductDetail,
    props: true, // передавать :id как пропс
  },
]
```

**Ключевые поля:**
- `path` — URL-путь.
- `name` — имя маршрута (удобно для `router.push({ name: '...' })`).
- `component` — компонент страницы.
- `props` — если `true`, динамические сегменты передаются как пропсы в компонент.
- `meta` — произвольные данные (например, `{ requiresAuth: true }`).

---

## Навигация в шаблоне: `<router-link>`

```vue
<template>
  <nav>
    <router-link to="/">Главная</router-link>
    <router-link :to="{ name: 'products' }">Каталог</router-link>
    <router-link :to="{ name: 'product-detail', params: { id: 123 } }">
      Товар 123
    </router-link>
  </nav>
</template>
```

**Пропсы для подсветки активной ссылки:**
- `active-class` — класс при префиксном совпадении.
- `exact-active-class` + `exact` — только при точном совпадении (важно для `/`).

---

## Программная навигация: `router` instance

В компоненте:
```ts
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

function goBack() {
  router.back()
}

function goToProduct(id: number) {
  router.push({ name: 'product-detail', params: { id } })
}

function replaceHome() {
  router.replace({ name: 'home' }) // без истории (replace вместо push)
}
</script>
```

**Методы:**
- `push` — добавить в историю.
- `replace` — заменить текущую запись.
- `back/forward` — как в браузере.
- `go(n)` — на n шагов вперёд/назад.

---

## Динамические параметры и query-параметры

- **Params:** `/products/:id` → `route.params.id`.
- **Query:** `/search?q=vue` → `route.query.q`.

Пример в компоненте:
```ts
const id = Number(route.params.id)
const q = route.query.q as string | undefined
```

Если в `routes` указано `props: true`, то `:id` приходит как обычный пропс, и в шаблоне можно использовать `{{ id }}`.

---

## Вложенные маршруты (Nested Routes)

Используются для макетов (sidebar + content) или вложенных страниц.

```ts
{
  path: '/dashboard',
  component: DashboardLayout,
  children: [
    {
      path: '',
      name: 'dashboard-overview',
      component: Overview,
    },
    {
      path: 'settings',
      name: 'dashboard-settings',
      component: Settings,
    },
  ],
}
```

В `DashboardLayout.vue` обязательно должен быть `<router-view />`, куда рендерятся дети.

---

## Защита маршрутов (Route Guards)

### Глобальные guards
```ts
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

### Per-route guards (в объекте route)
```ts
{
  path: '/profile',
  component: Profile,
  beforeEnter: (to, from, next) => { /* логика */ },
}
```

### Внутри компонента (in-component guards)
```ts
export default {
  beforeRouteEnter(to, from, next) { /* ... */ },
  beforeRouteUpdate(to, from, next) { /* ... */ },
  beforeRouteLeave(to, from, next) { /* ... */ },
}
```
В Vue 3 Composition API эти хуки **не работают** в `<script setup>`. Вместо них используют `router.beforeEach` или логику в сторе/composable.

---

## Ленивая загрузка (Lazy Loading)

Для производительности компоненты загружают по требованию:

```ts
const routes: RouteRecordRaw[] = [
  {
    path: '/admin',
    name: 'admin',
    component: () => import('@/views/Admin.vue'),
  },
]
```
Vite/Webpack автоматически создаст отдельный чанк. Это особенно полезно для админ-панелей на Laravel + Vue.

---

## Работа с историей и mode

- `createWebHistory()` — обычные URL без `#` (рекомендуется).
- `createWebHashHistory()` — URL с `#` (проще для статических хостингов без настройки сервера).

На сервере (Nginx/Apache) при `WebHistory` нужно настроить редирект всех неизвестных путей на `index.html`, иначе при обновлении страницы будет 404.

---

## Типизация в TypeScript

- Типы: `RouteRecordRaw`, `useRouter`, `useRoute`.
- Для типизации `meta`:
  ```ts
  declare module 'vue-router' {
    interface RouteMeta {
      requiresAuth?: boolean
      role?: 'admin' | 'user'
    }
  }
  ```
Тогда `route.meta.requiresAuth` будет строго типизирован.

---

## Интеграция с Pinia и твоим стеком

Часто проверку авторизации выносят в стор:

```ts
// stores/auth.ts
export const useAuthStore = defineStore('auth', () => {
  const isLoggedIn = ref(false)
  function login() { /* ... */ }
  return { isLoggedIn, login }
})
```

Guard:
```ts
router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    next('/login')
  } else {
    next()
  }
})
```

Это удобно, потому что стор уже типизирован и переиспользуется в формах, API-запросах и т. д.

---

## Продвинутые возможности

- **Named views** — несколько `<router-view name="...">` на одной странице (редко, но бывает для сложных макетов).
- **Dynamic routing** — добавление маршрутов на лету через `router.addRoute()` (полезно для динамических админок).
- **Scroll behavior** — настройка прокрутки при переходе:
  ```ts
  const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
      if (savedPosition) return savedPosition
      return { top: 0 }
    },
  })
  ```

---

## Частые ошибки и нюансы

- **404 при обновлении страницы** в режиме `WebHistory` — нужно настроить сервер на редирект на `index.html`.
- **Не передавать `params` при использовании `name`** — ошибка вида `router.push({ name: 'product-detail' })` без `params: { id }`.
- **Смешивание guards** — не дублируй одну и ту же логику в `beforeEach` и `beforeEnter`.
- **Типизация `route.params`** — всегда приводи к нужному типу (`Number(route.params.id)` и т. п.).
- **Отсутствие `<router-view>`** в layout-компоненте — маршруты не рендерятся.

---

## Практические советы под твой стек

- **Для Laravel + Vue:** роутинг часто делят на публичные и защищённые зоны. Публичные — лендинги, каталог; защищённые — админка/профиль. Используй `meta: { requiresAuth: true }`.
- **Lazy loading** — обязательно для админки и больших разделов.
- **Имена маршрутов** (`name`) — используй везде: это упрощает рефакторинг и тесты.
- **Типизируй `meta`** — это поможет избежать ошибок в guards и UI.
- **Интегрируй с Pinia** — логика авторизации и прав доступа в одном месте.