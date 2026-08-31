Атрибут `setup` в теге `<script>` (на практике почти всегда используют синтаксис `<script setup>`) — это **подсказка компилятору Vue**, которая включает специальный режим обработки кода на основе Composition API. Он делает код компонента лаконичнее и удобнее, особенно в связке с TypeScript, Pinia и твоим стеком в целом.

---

## Два варианта, чтобы не путаться

1. **`<script setup>`** (современный, рекомендуемый) — синтаксический сахар, который используют в 95 % случаев в Vue 3.
2. **`<script>` + `setup()`** (классический Composition API) — более многословный вариант, где ты явно пишешь функцию `setup()` и возвращаешь объект.

Дальше речь про `<script setup>`, потому что именно его обычно имеют в виду под «атрибутом setup».

---

## Что он даёт (главное)

- **Автоматически делает переменные доступными в шаблоне.** Всё, что ты объявишь на верхнем уровне в `<script setup>`, можно сразу использовать в `<template>` без `return`.
- **Упрощает работу с props/emits.** Используются специальные макросы `defineProps` и `defineEmits`.
- **Автоматическая регистрация компонентов.** Если импортируешь компонент, он сразу доступен в шаблоне по имени переменной (без секции `components`).
- **Лучшая типизация с TypeScript.** Интерфейсы и типы для props/emits пишутся прямо в макросах.
- **Меньше шаблонного кода.** Не нужно писать `export default { setup() { ... } }` и вручную возвращать всё, что нужно шаблону.

---

## Пример: классический Composition API vs `<script setup>`

**Классический вариант:**
```vue
<script>
import { ref } from 'vue'
import Child from './Child.vue'

export default {
  components: { Child },
  setup() {
    const count = ref(0)
    function increment() { count.value++ }
    return { count, increment }
  }
}
</script>

<template>
  <Child />
  <button @click="increment">{{ count }}</button>
</template>
```

**Вариант с `<script setup>`:**
```vue
<script setup lang="ts">
import { ref } from 'vue'
import Child from './Child.vue'

const count = ref<number>(0)
function increment() { count.value++ }
</script>

<template>
  <Child />
  <button @click="increment">{{ count }}</button>
</template>
```

Заметь: нет `export default`, нет `components`, нет `return` — и при этом `count`, `increment`, `Child` сразу видны в шаблоне.

---

## Как это работает «под капотом»

Компилятор Vue (в Vite/Webpack) на этапе сборки превращает `<script setup>` в обычный компонент с функцией `setup()`. То есть это **компиляторная фича**, а не новая среда выполнения. Поэтому в браузере или Node.js отдельно такого API нет — оно работает только в однофайловых компонентах (`.vue`) при сборке.

---

## Важные возможности именно в `<script setup>`

- **`defineProps`** — объявление входных параметров:
  ```ts
  const props = defineProps<{
    title: string
    count?: number
  }>()
  ```
- **`defineEmits`** — объявление событий:
  ```ts
  const emit = defineEmits<{
    (e: 'save', data: { title: string }): void
  }>()
  function onSave() { emit('save', { title: 'My Title' }) }
  ```
- **Автоматическая доступность импортированных компонентов** — никакой регистрации в `components`.
- **Поддержка TypeScript «из коробки»**: `lang="ts"` + интерфейсы дают точную типизацию props/emits и реактивных переменных.

---

## Связь с твоим стеком (Vue 3 + TypeScript + Laravel + Pinia)

- **TypeScript.** В `<script setup>` типизация props/emits максимально чистая: интерфейсы пишутся прямо в `defineProps/defineEmits`, а типы для `ref/reactive` — рядом с объявлением.
- **Pinia.** Использование сторов выглядит естественно:
  ```ts
  <script setup lang="ts">
  import { useUserStore } from '@/stores/user'
  const userStore = useUserStore()
  </script>
  ```
- **Laravel API.** Удобно типизировать ответы от бэкенда и сразу использовать их в шаблоне без лишних обёрток.
- **Composables.** Логику (запросы к API, валидацию, пагинацию) выносят в отдельные функции и импортируют в `<script setup>`.

---

## Частые ошибки и нюансы

- **Нельзя использовать `this`.** В Composition API (и в `<script setup>`) нет экземпляра компонента, поэтому `this.someProp` не работает.
- **Не смешивай Options API и `<script setup>` в одном компоненте.** Выбирай один стиль на компонент.
- **Макросы только в `<script setup>`.** `defineProps`, `defineEmits`, `defineModel` работают только внутри этого блока.
- **Асинхронность.** В самом `<script setup>` нельзя делать `await` на верхнем уровне (если не используешь экспериментальный `top-level await` или `<Suspense>`). Для загрузки данных обычно используют `onMounted` + `async/await` либо выносят логику в composable/Pinia action.

---

## Когда можно не использовать `<script setup>`

Редко, но бывает:
- Если нужен доступ к экземпляру компонента через `getCurrentInstance()` для продвинутых плагинов.
- В некоторых edge‑case с SSR, где требуется особый контроль над созданием экземпляра.
- При миграции старого кода, где уже много логики в Options API.

Для новых проектов и твоего стека **`<script setup>` — стандарт де‑факто**.

Если скажешь, какой кейс хочешь реализовать (например, форма с валидацией, таблица с пагинацией, интеграция с Laravel API), могу показать пример компонента на `<script setup>` с типизацией и Pinia.