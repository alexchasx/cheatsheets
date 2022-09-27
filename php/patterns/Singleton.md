
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
    private array $props = [];
    private static Singleton $instance;     // Обязательно!

    private function __construct() {}       // Обязательно!
    private function __clone() {}
    private function __wakeup() {}

    public static function getInstance(): Singleton // Обязательно!
    {
        if (empty(self::$instance)) {
            self::$instance = new self();
        }
        return self::$instance;
    }

	public function setProperty($key, $value) {
		$this->props[$key] = $value;
	}

	public function getProperty($key) {
		return $this->props[$key];
	}
}

// Использование
$single = Singleton::getInstance();
$single->setProperty('variable', 12);
echo 'From "single" = ' . $single->getProperty('variable');
```