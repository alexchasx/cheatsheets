
# Наблюдатель (Observer)
Определяет отношение «один-ко-многим» между объектами. Когда состояние одного объекта изменяется, все зависимые объекты получают оповещения.

Рализация:
- Субъект (Издатель) содержит список оповещаемых, методы добавления, удаления и оповещения наблюдателей.
- Наблюдатели имеет метод для обновления информации.

```php
class Newspaper implements \SplSubject{
    private $name;
    private $observers = array();
    private $content;
   
    public function __construct($name) {
        $this->name = $name;
    }

    public function attach(\SplObserver $observer) {
        $this->observers[] = $observer;
    }
   
    public function detach(\SplObserver $observer) {
       
        $key = array_search($observer,$this->observers, true);
        if(false !== $key){
            unset($this->observers[$key]);
        }
    }
   
    public function breakOutNews($content) {
        $this->content = $content;
        $this->notify();
    }
   
    public function getContent() {
        return $this->content." ({$this->name})";
    }
   
    public function notify() {
        foreach ($this->observers as $value) {
            $value->update($this);
        }
    }
}

class Reader implements SplObserver{
    private $name;
   
    public function __construct($name) {
        $this->name = $name;
    }
   
    public function update(\SplSubject $subject) {
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