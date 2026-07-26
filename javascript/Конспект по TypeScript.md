
# Конспект по синтаксису TypeScript

## 1. Базовые типы данных

* `number` — числовые значения (целые и дробные):
  ```typescript
  let age: number = 25;
  let price: number = 9.99;
  ```
* `string` — строковые значения:
  ```typescript
  let name: string = "Alice";
  let message: string = `Hello, ${name}!`;
  ```
* `boolean` — логические значения:
  ```typescript
  let isActive: boolean = true;
  let hasPermission: boolean = false;
  ```
* `any` — любой тип (отключает проверку типов):
  ```typescript
  let unknownValue: any = "может быть строкой";
  unknownValue = 42; // допустимо
  ```
* `void` — отсутствие значения (обычно для функций):
  ```typescript
  function logMessage(): void {
    console.log("Сообщение");
  }
  ```
* `null` и `undefined` — специальные значения:
  ```typescript
  let empty: null = null;
  let notDefined: undefined = undefined;
  ```

## 2. Составные типы

* **Массивы:**
  ```typescript
  let numbers: number[] = [1, 2, 3];
  let names: Array<string> = ["Alice", "Bob"];
  ```
* **Кортежи (Tuples)** — массивы с фиксированной длиной и типами:
  ```typescript
  let person: [string, number] = ["Alice", 25];
  ```
* **Объединения (Union)** — переменная может иметь один из нескольких типов:
  ```typescript
  let id: string | number = "123";
  id = 123; // тоже допустимо
  ```
* **Пересечения (Intersection)** — объединение нескольких типов:
  ```typescript
  type A = { a: string };
  type B = { b: number };
  let combined: A & B = { a: "text", b: 42 };
  ```

## 3. Интерфейсы и типы

* **Интерфейсы:**
  ```typescript
  interface User {
    id: number;
    name: string;
    email?: string; // опциональное поле
  }

  let user: User = { id: 1, name: "Alice" };
  ```
* **Типы (Type Aliases):**
  ```typescript
  type Point = {
    x: number;
    y: number;
  };

  let point: Point = { x: 10, y: 20 };
  ```

## 4. Функции

* **Типизация параметров и возвращаемого значения:**
  ```typescript
  function add(a: number, b: number): number {
    return a + b;
  }
  ```
* **Опциональные параметры:**
  ```typescript
  function greet(name: string, greeting?: string): string {
    return `${greeting || 'Hello'}, ${name}!`;
  }
  ```
* **Параметры по умолчанию:**
  ```typescript
  function multiply(a: number, b: number = 1): number {
    return a * b;
  }
  ```
* **Функции как типы:**
  ```typescript
  type MathOperation = (a: number, b: number) => number;

  const add: MathOperation = (x, y) => x + y;
  ```

## 5. Классы

```typescript
class Person {
  // Поля класса
  name: string;
  private age: number; // приватное поле

  // Конструктор
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  // Методы
  getInfo(): string {
    return `${this.name}, ${this.age} лет`;
  }
}

// Наследование
class Student extends Person {
  studentId: string;

  constructor(name: string, age: number, studentId: string) {
    super(name, age);
    this.studentId = studentId;
  }
}
```

## 6. Модификаторы доступа

* `public` — доступен везде (по умолчанию);
* `private` — только внутри класса;
* `protected` — внутри класса и его наследников.

## 7. Дженерики (Generics)

Позволяют создавать переиспользуемые компоненты с типами:
```typescript
function identity<T>(arg: T): T {
  return arg;
}

let output1 = identity<string>("hello");
let output2 = identity<number>(42);
```

## 8. Декораторы

Специальные функции, которые добавляют метапрограммирование:
```typescript
@Component({
  selector: 'app-root',
  template: `<h1>Hello World</h1>`
})
class AppComponent {}
```

## 9. Пространства имён (Namespaces)

Группировка связанных типов:
```typescript
namespace MathUtils {
  export function add(a: number, b: number): number {
    return a + b;
  }

  export function multiply(a: number, b: number): number {
    return a * b;
  }
}

// Использование
let result = MathUtils.add(5, 3);
```

## 10. Асинхронные операции

* **Promises:**
  ```typescript
  function fetchData(): Promise<string> {
    return new Promise((resolve) => {
      setTimeout(() => resolve("Данные получены"), 1000);
    });
  }
  ```
* **Async/await:**
  ```typescript
  async function getData(): Promise<void> {
    const data = await fetchData();
    console.log(data);
  }
  ```

## 11. Утилитарные типы (Utility Types)

Встроенные типы для трансформации:
* `Partial<T>` — все поля опциональные;
* `Readonly<T>` — все поля только для чтения;
* `Pick<T, K>` — выбор определённых полей;
* `Omit<T, K>` — исключение определённых полей.

Пример:
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

type PartialUser = Partial<User>; // все поля опциональны
type UserNameOnly = Pick<User, 'name'>; // только поле name
```

## 12. Опциональная цепочка (Optional Chaining)

Безопасный доступ к вложенным свойствам:
```typescript
const user = {
  profile: {
    address: {
      city: "Moscow"
    }
  }
};

// Безопасный доступ
const city = user?.profile?.address?.city;
```

## 13. Оператор нулевого слияния (Nullish Coalescing)

Предоставляет значение по умолчанию только для `null` или `undefined`:
```typescript
let name = user.name ?? "Anonymous";
```

---

## Краткий итог

TypeScript расширяет JavaScript следующими возможностями:
* статическая типизация;
* интерфейсы и типы;
* классы с модификаторами доступа;
* дженерики;
* декораторы;
* улучшенная поддержка асинхронного кода;
* утилитарные типы и современные синтаксические конструкции.
```