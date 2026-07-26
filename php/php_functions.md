# PHP: функция `array_map`

`array_map` — применяет callback-функцию ко всем элементам одного или нескольких массивов.

## Базовый синтаксис

```php
array_map(?callable $callback, array $array, array ...$arrays): array
```

- `$callback` — функция, применяемая к каждому элементу. Если `null`, массивы объединяются.
- `$array` — исходный массив.
- `$arrays` — дополнительные массивы (если переданы, callback получает элемент из каждого).

---

## Пример 1: Анонимная функция (замыкание)

Удвоение каждого числа:

```php
$numbers = [1, 2, 3, 4, 5];

$doubled = array_map(function(int $n): int {
    return $n * 2;
}, $numbers);

// Результат: [2, 4, 6, 8, 10]
print_r($doubled);
```

---

## Пример 2: Именованная функция

Приведение строк к верхнему регистру:

```php
$words = ['hello', 'world', 'php'];

$uppercased = array_map('strtoupper', $words);

// Результат: ['HELLO', 'WORLD', 'PHP']
print_r($uppercased);
```

---

## Пример 3: Несколько массивов

Сложение элементов двух массивов поэлементно:

```php
$a = [1, 2, 3];
$b = [10, 20, 30];

$sum = array_map(function(int $x, int $y): int {
    return $x + $y;
}, $a, $b);

// Результат: [11, 22, 33]
print_r($sum);
```

> **Важно:** Если массивы разной длины, `array_map` дополнит короткий массив пустыми значениями (`null`).

---

## Пример 4: `null` в качестве callback (объединение массивов)

Создание массива из элементов нескольких массивов:

```php
$names = ['Alice', 'Bob', 'Charlie'];
$ages  = [25, 30, 35];

$combined = array_map(null, $names, $ages);

// Результат:
// [
//   ['Alice', 25],
//   ['Bob',   30],
//   ['Charlie', 35]
// ]
print_r($combined);
```

---

## Пример 5: Стрелочная функция (PHP 7.4+)

Фильтрация и преобразование в одну строку (лаконичный синтаксис):

```php
$prices = [100, 250, 500, 1000];

$withTax = array_map(
    fn(int $price) => $price * 1.2,
    $prices
);

// Результат: [120, 300, 600, 1200]
print_r($withTax);
```

---

## Пример 6: Обработка ассоциативного массива

Извлечение значений по ключам и форматирование:

```php
$users = [
    ['name' => 'Alice', 'age' => 25],
    ['name' => 'Bob',   'age' => 30],
    ['name' => 'Charlie', 'age' => 35],
];

$formatted = array_map(
    fn(array $user): string => sprintf('%s (%d years)', $user['name'], $user['age']),
    $users
);

// Результат: ['Alice (25 years)', 'Bob (30 years)', 'Charlie (35 years)']
print_r($formatted);
```

---

## Пример 7: Сохранение ключей ассоциативного массива

`array_map` не сохраняет строковые ключи. Чтобы обойти это — используйте `array_combine` + `array_keys`:

```php
$data = ['a' => 1, 'b' => 2, 'c' => 3];

$mapped = array_combine(
    array_keys($data),
    array_map(fn(int $v) => $v * 10, $data)
);

// Результат: ['a' => 10, 'b' => 20, 'c' => 30]
print_r($mapped);
```

---

## Сводка

| Сценарий | Callback | Результат |
|----------|----------|-----------|
| Один массив | `fn($v) => ...` | Новый массив той же длины |
| Несколько массивов | `fn($v1, $v2) => ...` | Поэлементная обработка |
| Объединение | `null` | Массив массивов (как `zip`) |
| Сохранение ключей | Любая | `array_combine` + `array_keys` |