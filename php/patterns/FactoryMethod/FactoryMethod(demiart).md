Фабричный метод — создание объектов на основе заданного параметра.

Это абстрагирование создания объектов.

Вариант на основе строчных парамметров:
```php
class CarEngineFactory implements ICarEngineFactory
{
    public function make(string $carBrand): IEngine
    {
       switch ($carBrand) {
           case "mercedes":
              return new MercedesEngine();
           case "bmw":
               return new BmwEngine();
           default: 
                throw new CarEngineNotAvailableException();          
       }
    }
}
```

Улучшенный вариант:
```php
class CarEngineFactory implements ICarEngineFactory
{
    protected static $availableEngines = [
        Mercedes::class => MercedesEngine::class,
        Bmw::class => BmwEngine::class,
    ];

    public function make(ICar $car): IEngine
    {
        $carClass = get_class($car);

        if (!array_key_exists(get_class($car), self::$availableEngines)) {
            throw new CarEngineNotAvailableException();
        }

        $engineClass = self::$availableEngines[$carClass];

        return (new $engineClass());
    }
}
```