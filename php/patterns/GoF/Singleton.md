
# Шаблон проектирования Одиночка (Singleton) в PHP.

`Singleton` - Порождающий паттерн.

Назначение: гарантировать единственный экземпляр класса и глобальную точку доступа к нему.

Примеры: 
- класс-логгер, 
- класс подключения к БД.

Проблема:
Нам не нужно, чтобы одни объекты устанавливали значения в каком-то объекте, а
другие - читали данные из совершенно иного объекта.

Недостатки: 
- мешает тестированию, 
- повышает связанность кода (`coupling`).

Реализация: 
- приватный конструктор, 
- приватное статич. свойство, принимающее объект текущего класса,
- публичный статич. метод, создающий объект или возвращающий на него ссылку,
- приватные методы `__clone` и `__wakeup`.


```php
class Singleton
{
    private static Singleton $instance;

    private function __construct() {}
    private function __clone() {}
    private function __wakeup() {}

    public static function getInstance(): Singleton
    {
        if (empty(self::$instance)) {
            self::$instance = new self();
        }
        return self::$instance;
    }

}

$single = Singleton::getInstance();
```