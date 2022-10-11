
Service Locator - вместо создания объектов («сервисов») напрямую с помощью "new", мы будем использовать специальный «фабричный» объект, который будет отвечать за создание, а точнее «нахождение» всех сервисов.

Плюсы:
- позволяет отвязать один компонент от другого

Минусы:
- Локатор - глобальный объект
- В Локатор можно записать всё что угодно и получить не те объекты

Реализация:
- статич. сеттер для записи объектов внутрь локатора
- стат. геттер

```php
class Locator
{
    protected static $services = [];

    public static function setComponent($name, $object)
    {
        self::$services[$name] = $object;
    }

    public static function getComponent($name)
    {
        return self::$services[$name] ?? null;
    }
}
```