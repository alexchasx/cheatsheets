## Конспект по Vue.js 3 Composition API

Учитывая твой стек (Vue 3, TypeScript, Laravel, Pinia), Composition API — это основной способ писать компоненты в современных Vue‑проектах. Он даёт лучшую переиспользуемость логики, понятную типизацию и удобство работы с реактивностью.

---

## Что такое Composition API и зачем он нужен

Composition API — альтернатива Options API (где логика разбросана по `data`, `methods`, `computed` и т. д.). Вместо этого ты пишешь логику как набор функций и реактивных переменных, а потом «составляешь» их в компоненте.

**Главные плюсы:**
* **Переиспользование логики** через composables (хуки).
* **Лучшая организация кода**: связанные по смыслу куски логики лежат рядом.
* **Удобная типизация в TypeScript**: легче описывать типы для реактивных значений.
* **Меньше «магических» свойств**: нет привязки к `this`, всё — обычные переменные и функции.

---

## Базовые реактивные примитивы

### `ref`
Для примитивов и любых значений, где нужна реактивность через `.value`.

```ts
import { ref } from 'vue'

const count = ref<number>(0)
count.value++
```

В шаблоне: `{{ count }}` (Vue автоматически разворачивает `.value`).

### `reactive`
Для объектов. Возвращает прокси, менять свойства можно напрямую.

```ts
import { reactive } from 'vue'

const user = reactive<{ id: number; name: string }>({
  id: 1,
  name: 'Alice'
})
user.name = 'Bob'
```

**Когда что выбирать:**
* `ref` — для чисел, строк, булевых, массивов (если удобно работать через `.value`), а также когда нужно переназначить переменную целиком.
* `reactive` — для сложных объектов, чтобы не писать `.value` на каждом поле.

---

## Жизненный цикл в Composition API

Вместо хуков `mounted`, `beforeDestroy` и т. п. используются `onMounted`, `onUnmounted` и другие:

```ts
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  // аналог mounted
})

onUnmounted(() => {
  // аналог beforeDestroy / destroyed
})
```

Полный список: `onBeforeMount`, `onMounted`, `onBeforeUpdate`, `onUpdated`, `onBeforeUnmount`, `onUnmounted`, а также `onErrorCaptured`.

---

## Вычисляемые значения и эффекты

### `computed`
Создаёт реактивное производное значение.

```ts
import { computed, ref } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)
```

Можно делать и writable computed (с геттером и сеттером).

### `watch` и `watchEffect`

`watch` — следит за конкретными источниками:

```ts
import { watch, ref } from 'vue'

const search = ref('')
watch(search, (newVal) => {
  fetchData(newVal)
})
```

`watchEffect` — автоматически отслеживает все реактивные зависимости внутри себя:

```ts
import { watchEffect, ref } from 'vue'

const query = ref('')
const page = ref(1)

watchEffect(() => {
  fetch(`/api/items?q=${query.value}&page=${page.value}`)
})
```

---

## Передача данных между компонентами

### Props

```ts
// child.vue
import { defineProps } from 'vue'

const props = defineProps<{
  title: string
  count?: number
}>()
```

TypeScript позволяет описывать типы прямо в `defineProps`.

### Emit

```ts
import { defineEmits } from 'vue'

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
  (e: 'save', data: { title: string }): void
}>()

function save() {
  emit('save', { title: 'My Title' })
}
```

### Provide / Inject

Позволяют передавать данные «сквозь» уровни компонентов:

```ts
// родитель
import { provide } from 'vue'
const theme = ref('dark')
provide('theme', theme)

// потомок
import { inject } from 'vue'
const theme = inject<'light' | 'dark'>('theme')!
```

---

## Работа с шаблоном и реактивностью в `<script setup>`

Конструкция `<script setup>` — синтаксический сахар, который делает Composition API максимально лаконичным:

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'
import { useCounter } from '@/composables/useCounter'

const count = ref(0)
const doubled = computed(() => count.value * 2)

const { increment, reset } = useCounter()
</script>

<template>
  <button @click="increment">{{ count }}</button>
  <p>{{ doubled }}</p>
</template>
```

Все переменные и функции из `setup` автоматически доступны в шаблоне.

---

## Composables (переиспользуемая логика)

Composable — это обычная функция, которая использует реактивные API и возвращает нужные значения.

Пример простого composable:

```ts
// composables/useCounter.ts
import { ref, computed } from 'vue'

export function useCounter(initial = 0) {
  const count = ref(initial)
  const doubled = computed(() => count.value * 2)

  function increment() { count.value++ }
  function reset() { count.value = initial }

  return { count, doubled, increment, reset }
}
```

Использование:

```ts
const { count, increment } = useCounter(10)
```

Это идеально ложится на твой стек: можно вынести в composables логику работы с API Laravel, валидацию форм, пагинацию, фильтры и т. д.

---

## Типизация в Composition API + TypeScript

Ключевые моменты:
* `defineProps` и `defineEmits` поддерживают интерфейсы и типы.
* Для `ref` и `reactive` явно указывай типы: `ref<number>`, `reactive<User>`.
* Composables можно типизировать через возвращаемые интерфейсы.

Пример типизированного composable:

```ts
interface CounterReturn {
  count: Ref<number>
  increment: () => void
}

export function useCounter(): CounterReturn {
  const count = ref<number>(0)
  function increment() { count.value++ }
  return { count, increment }
}
```

---

## Интеграция с Pinia

Pinia построена на Composition API, поэтому использование сторов очень естественное:

```ts
<script setup lang="ts">
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

function logout() {
  userStore.logout()
}
</script>
```

Ты можешь комбинировать сторы и composables: например, в composable вынести логику форм, а данные брать из стора.

---

## Асинхронность и загрузка данных

В Composition API нет отдельного хука `async setup`, но можно использовать `onMounted` + `async/await`:

```ts
import { onMounted, ref } from 'vue'

const items = ref<Product[]>([])

onMounted(async () => {
  const res = await fetch('/api/products')
  items.value = await res.json()
})
```

Для более сложной логики удобно выносить запросы в composables или actions Pinia.

---

## Ключевые отличия от Options API

| Что | Options API | Composition API |
| --- | --- | --- |
| Реактивность | `data()` возвращает объект, свойства доступны напрямую | `ref`, `reactive`, явный `.value` у `ref` |
| Логика | Разбросана по полям (`data`, `methods`, `computed`) | Сгруппирована в функции и composables |
| Переиспользование | Mixins (проблемные) или HOC | Composables |
| Типизация | Сложнее, много магии | Проще, обычные типы TS |
| Контекст `this` | Есть | Нет (используются переменные) |

---

## Практические советы под твой стек

* **Для форм и валидации**: делай composables для полей, ошибок и отправки формы. Так легче тестировать и переиспользовать.
* **Для API Laravel**: выноси запросы в отдельные composables или Pinia actions, возвращай типизированные DTO.
* **Не смешивай «всё в одном»**: разделяй логику по смыслу — отдельные composables для фильтров, пагинации, сортировки.
* **Используй TypeScript на максимум**: типизируй props, emits, ref/reactive, возвращаемые типы composables.
* **Интегрируй с Pinia**: сторы — для глобального состояния, composables — для логики компонентов.

---

## Частые ошибки

* Пытаться использовать `.value` в шаблоне: пиши `{{ count }}`, а не `{{ count.value }}`.
* Забывать, что `reactive` не делает реактивными новые свойства: если нужно добавить поле, используй `Object.assign` или пересоздай объект, либо используй `ref`.
* Делать `watch` без указания источника или неправильно использовать `watchEffect`.
* Смешивать Options API и Composition API в одном компоненте — лучше выбрать один стиль.
* Не типизировать сложные объекты в `reactive`: это усложняет работу с данными от Laravel API.