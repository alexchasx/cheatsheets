# Декоратор (Wrapper)
Cтруктурный паттерн.

Назначение:
- Добавляет объекту новую функциональность без наследования.

Реализация:
- общий с целевым объектом интерфейс,
- одноимённые с целевым объектом методы,
- расширяемый объект внедряется в декоратор через конструтор,
- в клиентском коде вместо целевого объекта исполь-ся декоратор.

```php
interface IComponent
{
    public function operation();
}

class ConcreteComponent implements IComponent
{
    public function operation()
    { /* какой-то код */ }
}

class Decorator implements IComponent
{
    public function __construct(
        protected IComponent $component
    ) {}

    public function operation()
    {
        // ... расширенная функциональность
        $this->component->operation();
        // ... расширенная функциональность
    }

}

$decorator = new Decorator( new ConcreteComponent());
$decorator->operation();




// ================= Еще примеры ====================

// Декораторы декораторов

interface IText
{
    public function show();
}

class TextHello implements  IText
{
    protected $object;

    public function __construct(IText $text) {
        $this->object = $text;
    }

    public function show() {
        echo 'Hello';
        $this->object->show();
    }
}

class TextWorld implements IText
{
    public function show() {
        echo ' world';
    }
}

$decorator = new TextHello(new TextWorld());
$decorator->show(); // Hello world

/////////////////////////

abstract class ParentClass
{
	abstract public function getFactor();
}

class Real extends ParentClass
{
	private $factor = 2;

	public function getFactor()
	{
		return $this->factor;
	}
}

abstract class Decorator extends ParentClass
{
	protected $parentClass;

	public function __construct( ParentClass $parentClass)
	{
		$this->parentClass = $parentClass;
	}
}

class FirstDecorator extends Decorator
{
	public function getFactor()
	{
		return $this->parentClass->getFactor() + 2;
	}
}

class SecondDecorator extends Decorator
{
	public function getFactor()
	{
		return $this->parentClass->getFactor() - 4;
	}
}

$parentClass = new Real();
print $parentClass->getFactor(); // 2

$parentClass = new FirstDecorator();
print $parentClass->getFactor(); // 4

$parentClass = new SecondDecorator();
print $parentClass->getFactor(); // 0

```