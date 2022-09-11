Адаптер (структурный шаблон) преобразует интерфейс класса в другой интерфейс, ожидаемый клиентом.

Назначение: 
- Обеспечить взаимодействие объектов с разными интерфейсами. Адаптировать, а не переписывать существующий код к требуемому интерфейсу.

Реализация:
- Похожа на реализацию Декоратора, но Адаптер реализует общий интерфейс с одним объектом, а принимает в конструктор - другой. Вместо расширения функционала - переопределение метода.

```php

class Component implements IComponent
{
    public function operation()
    {
        // code
    }
}

class OtherComponent
{
    public function otherOperation()
    {
        // code
    }
}

class Adapter implements IComponent
{
    public function __construct(
        private OtherComponent $component
    ) {}

    public function operation()
    {
        $this->component->otherOperation();
    }
}


$adaptedComponent = new Adapter( new OtherComponent());
$adaptedComponent->operation();
```