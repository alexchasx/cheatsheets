Декоратор (Wrapper) - структурный паттерн.
Декоратор динамически добавляет объекту новую функциональность без наследования.

Реализация:
- Декоратор(Д) и Целевой Объект(ЦО) реализуют общий интерфейс.
- В свойство Д через конструтор забрасывается ЦО.
- Д расширяет общие с ЦО методы.
- В клиентском коде создаётся объект Д, и в него помещается ЦО. 
Далее вызываются методы Д.

```php
interface IComponent
{
    public function operation();
}

class ConcreteComponent implements IComponent
{
    public function operation()
    {
        // какой-то код
    }
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

$decoratedComponent = new Decorator( new ConcreteComponent());
$decoratedComponent->operation();


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