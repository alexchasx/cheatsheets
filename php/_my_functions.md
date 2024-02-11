```php

    /**
     * Задаёт порядок сортировки в зависимости от указанного расположения элементов
     * Использование: 
     *  usort($images, $this->build_sorter($order));
     */
    private function build_sorter($order)
    {
        return function ($a, $b) use ($order) {
            $a_url = $a['url'] ?? $a['image'];
            $b_url = $b['url'] ?? $b['image'];

            $array_a = explode('/', $a_url);
            $string_end_a = array_pop($array_a);
            $pos_a = array_search($string_end_a, $order);

            $array_b = explode('/', $b_url);
            $string_end_b = array_pop($array_b);
            $pos_b = array_search($string_end_b, $order);

            return $pos_a - $pos_b;
        };
    }
```
