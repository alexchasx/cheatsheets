
# Шаблон проектирования Наблюдатель (Observer) в PHP (конспект)

Тип: Поведенческий

Определяет отношение «один-ко-многим» между объектами. Когда состояние одного объекта изменяется, все зависимые объекты получают оповещения об этом.

Рализация:
- Субъект (Издатель) содержит список оповещаемых, методы добавления, удаления и оповещения наблюдателей.
- Наблюдатели имеет метод для обновления информации об субъекте.

```php
class Newspaper implements \SplSubject
{
    private array $observers = [];
    private string $content;
   
    public function __construct(private string $name)
    {}

    public function attach(\SplObserver $observer): void
    {
        $this->observers[] = $observer;
    }
   
    public function detach(\SplObserver $observer) 
    {       
        $key = array_search($observer, $this->observers, true);
        if(false !== $key) {
            unset($this->observers[$key]);
        }
    }

    public function notify(): void
    {
        foreach ($this->observers as $value) {
            $value->update($this);
        }
    }
   
    public function breakOutNews(string $content): void
    {
        $this->content = $content;
        $this->notify();
    }
   
    public function getContent(): string
    {
        return $this->content . " ({$this->name})";
    }
   
}

class Reader implements SplObserver
{   
    public function __construct(private string $name) 
    {}
   
    public function update(\SplSubject $subject): void
    {
        echo $this->name.' is reading breakout news <b>'.$subject->getContent().'</b><br>';
    }
}

$newspaper = new Newspaper('Newyork Times');

$allen = new Reader('Allen');
$jim = new Reader('Jim');
$linda = new Reader('Linda');

//add reader
$newspaper->attach($allen);
$newspaper->attach($jim);
$newspaper->attach($linda);

//remove reader
$newspaper->detach($linda);

//set break outs
$newspaper->breakOutNews('USA break down!');d
```