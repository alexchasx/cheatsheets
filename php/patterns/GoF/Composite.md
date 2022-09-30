# Шаблон проектирования Composite (Компоновщик) на php.
Структурный шаблон проектирования.

Назначение:
- Позволяет одинаково работать с составными и отдельными объектами.

Реализация:
- общий интерфейс у составных и атомарных объектов,
- составные объекты имеют методы для добавления, удаления и манипуляций с атомарными или другими составными объектами.

```php
interface IComponent 
{
    public function display();
}

class Composite implements IComponent
{        
    public function __construct(
        public string $name,
        protected array $children = [],
    ) {}

    public function add(IComponent $item)
    {
        $this->children[$item->name] = $item;
    }

    public function remove(IComponent $item)
    {
        unset($this->children[$item->name]);
    }

    public function display()
    {
        $this->displaySelf();
        foreach ($this->children as $child) {
            $child->display();
        }
    }
}

class Leaf implements IComponent
{        
    public function __construct(
        public string $name
    ) {}

    public function display()
    {
        print $this->name.'<br>'.PHP_EOL;
    }
}

$root = new Composite("root");

$root->add(new Leaf("Leaf A"));
$root->add(new Leaf("Leaf B"));

$comp = new Composite("Composite X");
$comp->add(new Leaf("Leaf XA"));
$comp->add(new Leaf("Leaf XB"));

$root->add($comp);
$root->add(new Leaf("Leaf C"));

$leaf = new Leaf("Leaf D");
$root->add($leaf);
$root->remove($leaf);

$root->display();


// ===============================
abstract class Unit
{
    /**
     * выполняется принцип шаблона
     * Composite, который заключается в том, что у элементарных классов ("листьев") та­
     * кой же интерфейс, как у композитов.
     * Метод не всем нужен, поэтому генерирует исключение
     */
    public function addUnit(Unit $unit)
    {
        throw new UnitException(get_class($this) . " относится к ' неделимому объекту' ");
    }

    /**
     * Метод не всем нужен, поэтому генерирует исключение
     */
    public function removeUnit(Unit $unit)
    {
        throw new UnitException(get_class($this) . " относится к 'неделимому объекту'");
    }

    abstract public function power();

}

class UnitException extends Exception
{ }

/**
 * Несостаные объекты
 */
class Archer extends Unit
{
    public function power()
    {
        return 4;
    }
}

/**
 * Составные объекты
 */
class Army extends Unit
{
    private $units = [];

    /**
     * Добавить юнита
     */
    public function addUnit(Unit $unit)
    {
        if ( in_array($unit, $this->units, true) ) {
            return;
        }
        $this->units [] = $unit;
    }

    /**
     * Удаление юнитов
     * Анонимная функция обратного вызова предназначена для проверки элементов массива,
     * содержащихся в свойстве $units, на эквивалентность (вернет TRUE или FALSE)
     * @param object $unit
     */
    public function removeUnit(Unit $unit)
    {
        $this->units = array_udiff($this->units, array($unit),
            function($а, $b) {
                return ($а === $b) ? 0 : 1;
            });
    }

    /**
     * Вычисляет общую ударную силу
     */
    public function power()
    {
        $ret = 0;
        foreach ($this->units as $unit) {
            $ret += $unit->power();
        }
        return $ret;
    }

}


// Создадим армию
$main_army = new Army();
// Добавим боевую единицу
$main_army->addUnit( new Archer() );

// Создадим еще одну армию
$sub_army = new Army();
// Добавим несколько боевых единиц
$sub_army->addUnit( new Archer() );
$sub_army->addUnit( new Archer() );
$sub_army->addUnit( new Archer() );

// Добавим вторую армию к первой
$main_army->addUnit($sub_army);
// Все вычисления выполняются за кулисами
print "Атакующая сила : { $main_army->power() } \n";

```