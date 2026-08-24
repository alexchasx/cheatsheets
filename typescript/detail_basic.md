## Конспект по TypeScript

---

## Что такое TypeScript

TypeScript (TS) — это надмножество JavaScript (JS), которое добавляет статическую типизацию и дополнительные возможности для структурирования кода. Он компилируется в обычный JS, поэтому работает везде, где работает JS (браузеры, Node.js, серверы и т.д.).

**Зачем нужен:**
- помогает выявлять ошибки на этапе написания кода, а не в рантайме;
- улучшает читаемость и поддерживаемость больших проектов;
- даёт автодополнение и навигацию в IDE;
- позволяет описывать сложные структуры данных и контракты API.

---

## Установка и базовая настройка

### Установка
```bash
npm install -g typescript
tsc --version  # проверить версию
```

### Инициализация проекта
```bash
mkdir my-ts-project
cd my-ts-project
npm init -y
npm install --save-dev typescript @types/node
npx tsc --init
```
Команда `tsc --init` создаёт файл `tsconfig.json` — главный конфиг компилятора.

### Основные настройки `tsconfig.json`
- `target` — целевая версия JS (например, `"es2020"`).
- `module` — система модулей (`"commonjs"`, `"esnext"` и т.п.).
- `outDir` — папка для скомпилированных файлов (часто `"dist"`).
- `rootDir` — корень исходных TS-файлов.
- `strict` — включает строгие проверки типов (рекомендуется `true`).
- `esModuleInterop` — удобная работа с импортами из CommonJS.
- `skipLibCheck` — ускоряет сборку, пропуская проверки деклараций типов в библиотеках.

Пример минимального `tsconfig.json`:
```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"]
}
```

---

## Типы данных

### Примитивы
- `string`
- `number` (включая целые и дробные, без отдельного типа `int`)
- `boolean`
- `bigint`
- `symbol`
- `undefined`, `null`

### Сложные типы
- `any` — отключает проверку типов; использовать осторожно.
- `unknown` — безопасный аналог `any`: перед использованием нужно сузить тип.
- `void` — отсутствие возвращаемого значения (например, у функции).
- `never` — тип, который никогда не может иметь значения (для функций, которые всегда выбрасывают ошибку или зацикливаются).

### Составные типы
- **Массивы**: `string[]`, `Array<number>`.
- **Кортежи**: `[string, number, boolean]` — фиксированный порядок и типы элементов.
- **Объекты**: `{ name: string; age: number }`.
- **Функции**: `(a: number, b: number) => number`.

---

## Аннотации типов

Типы указываются после имени переменной/параметра через двоеточие:
```ts
let name: string = "Alex";
let age: number = 30;
const isActive: boolean = true;

function add(a: number, b: number): number {
  return a + b;
}
```

TypeScript умеет выводить типы автоматически:
```ts
const x = 10;        // number
const y = "hello";   // string
```
Но явные аннотации полезны для параметров функций, возвращаемых значений, сложных структур.

---

## Интерфейсы и типы

### Интерфейсы (`interface`)
Используются для описания структур объектов:
```ts
interface User {
  id: number;
  name: string;
  email?: string;      // необязательное поле
  roles: string[];
  login: () => void;
}
```
Поддерживают наследование:
```ts
interface Admin extends User {
  permissions: string[];
}
```

### Псевдонимы типов (`type`)
Более гибкие, подходят для объединений, пересечений, сложных выражений:
```ts
type Status = "pending" | "approved" | "rejected";
type Point = { x: number; y: number };
type Coordinates = [number, number];
```
Объединение и пересечение:
```ts
type AorB = A | B;   // значение может быть A или B
type AandB = A & B;   // значение должно соответствовать и A, и B
```

Разница: интерфейсы лучше подходят для описания объектов и наследования, типы — для более сложных комбинаций.

---

## Сужение типов (Type Narrowing)

TypeScript сужает тип внутри блоков условий:
```ts
function printLength(value: string | number) {
  if (typeof value === "string") {
    console.log(value.length);  // здесь value — string
  } else {
    console.log(value.toFixed(2));  // здесь value — number
  }
}
```
Также работают проверки на `instanceof`, `in`, равенство с конкретными значениями.

---

## Классы и ООП

Классы в TypeScript поддерживают модификаторы доступа: `public`, `private`, `protected`.

```ts
class User {
  private id: number;
  public name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  getId(): number {
    return this.id;
  }
}
```

Наследование:
```ts
class Admin extends User {
  role: "admin" = "admin";
}
```

Интерфейсы можно реализовывать в классах:
```ts
interface Drawable {
  draw(): void;
}

class Circle implements Drawable {
  radius: number;
  constructor(radius: number) { this.radius = radius; }
  draw() { console.log(`Circle with radius ${this.radius}`); }
}
```

---

## Дженерики (Generics)

Позволяют писать функции и типы, работающие с разными типами, сохраняя типобезопасность:
```ts
function identity<T>(arg: T): T {
  return arg;
}

const str = identity<string>("hello");
const num = identity<number>(42);
```

Дженерики в интерфейсах и классах:
```ts
interface Box<T> {
  content: T;
}

class Stack<T> {
  private items: T[] = [];
  push(item: T) { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
}
```

---

## Перечисления (Enums)

Удобны для фиксированных наборов значений:
```ts
enum Color { Red, Green, Blue }
// по умолчанию: Red=0, Green=1, Blue=2

enum Status {
  Pending = "PENDING",
  Approved = "APPROVED",
  Rejected = "REJECTED"
}
```

---

## Работа с модулями

ES-модули в TypeScript работают так же, как в JS:
```ts
// math.ts
export function add(a: number, b: number): number {
  return a + b;
}
export const PI = 3.14;

// main.ts
import { add, PI } from "./math";
```

CommonJS (для Node.js без ESM):
```ts
import fs = require("fs");
```
При включённом `esModuleInterop` чаще используют стандартный `import`.

---

## Ошибки типизации и как их читать

Типичные сообщения:
- `Type 'string' is not assignable to type 'number'` — несовпадение типов.
- `Property 'x' does not exist on type 'Y'` — обращение к несуществующему полю.
- `Argument of type '...' is not assignable to parameter of type '...'` — аргумент не подходит по типу.

Подход к исправлению:
1. Посмотреть, какой тип ожидается и какой передаётся.
2. Проверить, не забыли ли вы сузить тип (через `typeof`, `instanceof` и т.п.).
3. Проверить аннотации типов и возвращаемые значения.

---

## Практические советы и паттерны

- Включайте `"strict": true` в `tsconfig.json`.
- Избегайте `any`, используйте `unknown` и сужайте тип.
- Для объектов, где ключи — строки, а значения — одного типа, используйте индексные сигнатуры:
  ```ts
  interface Dictionary {
    [key: string]: string;
  }
  ```
- Используйте `readonly` для полей, которые не должны изменяться.
- Для конфигураций и сложных структур удобно описывать интерфейсы, а не писать типы «на лету».

---

## Интеграция с популярными стеками (с учётом твоих прошлых интересов)

- **Vue.js**: Vue 3 и Composition API отлично работают с TS; компоненты можно описывать с типизацией props, emits, refs.
- **Laravel + JS**: фронтенд на Vue/React с TypeScript, бэкенд на PHP не меняется, но API-контракт удобно описывать через TS-типы.
- **Node.js**: TS компилируется в JS и запускается через `node dist/index.js` или с `ts-node` для разработки.
- **Базы данных**: типы можно сопоставлять с таблицами/моделями (ORM, DTO), чтобы уменьшить ошибки при работе с данными.

---

## Частые вопросы и типичные проблемы

- **«Почему TS не видит типы для библиотек?»** — нужно установить `@types/...` (например, `npm install --save-dev @types/node @types/express`).
- **«Как работать с JSON?»** — JSON всегда приходит как `unknown`; нужно сужать тип вручную или через валидацию (Zod, Yup и т.п.).
- **«Можно ли смешивать TS и JS?»** — да, но лучше постепенно переводить файлы и не оставлять слишком много `any`.

---
