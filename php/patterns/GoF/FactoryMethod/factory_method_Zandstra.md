Factory Method (Фабричный метод) - это делегирование создания объектов специальным классам.

- Это порождающий шаблон проектирования.
- Применяется для получения объектов, когда в коде применяются абстрактные типы.


Пример: функционал, реализующий разные варианты кодирования данных. 

```php
abstract class Encoder
{
    abstract function encode();
}
```

```php
class BloggsEncoder extends Encoder
{
    public function encode()
    {
        return 'Данные закодированы в формате BloggsCal';
    }
}

```

```php
class MegaEncoder extends Encoder
{
    public function encode()
    {
        return 'Данные закодированы в формате MegaCai';
    }
}

```

```php
class Manager
{
    public function getEncoder(string $mode): Encoder
    {
        if ('mega' == $mode) {
            return new MegaEncoder();
        }
        return new BloggsEncoder();
    }
}

```

```php
$man = new Manager('mega');
$man->getEncoder();

```
