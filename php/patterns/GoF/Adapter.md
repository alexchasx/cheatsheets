
# Шаблон проектирования Адаптер в PHP

Тип: структурный.

Назначение: 
- адаптирует один интерфейс к другому (обеспечивает взаимодействие объектов с разными интерфейсами).

Реализация:
- Похожа на реализацию Декоратора, но Адаптер реализует общий интерфейс с одним объектом, а принимает в конструктор - другой. Вместо расширения функционала - переопределение метода.

Задача для примера:
- в клиентский код нужно внедрить функционал класса OtherComponent, но старый интерфейс нельзя переписать:

```php
// нельзя переписать
interface IComponent
{
    public function operation();
}


// нельзя переписать
class OtherComponent
{
    public function otherOperation()
    {
        // code
    }
}

// -----------------------------------

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

// -----------------------------------

// Клиентский код
$adaptedComponent = new Adapter( new OtherComponent());
$adaptedComponent->operation();
```