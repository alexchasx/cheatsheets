

```php
// Ссылки по теме:
https://carbon.nesbot.com/
https://github.com/briannesbitt/Carbon/blob/master/src/Carbon/Carbon.php
https://github.com/briannesbitt/Carbon/blob/master/src/Carbon/CarbonImmutable.php?ysclid=lq96dswt23396971726


$immutable = Carbon::now()->toImmutable();

$carbon = new Carbon();     // объект текущ. даты + время
$carbon = Carbon::today();  // сегодня
$carbon = Carbon::tomorrow();  // завтра
$carbon = Carbon::yesterday();  // вчера

$carbon = new Carbon('first day of next month'); // создать объект даты из произволной строки

$carbon = Carbon::create(2018, 12, 1, 2, 10, 30);   // 2018-12-01 02:10:30
$carbon = Carbon::createSafe(2018, 12, 1, 2, 10, 30);  // с проверкой каждого параметра на соответствие
$carbon = Carbon::createFromDate(2018, 12, 1);      // + текущ. время
$carbon = Carbon::createFromTime(2, 10, 30);        // текущ. дата + 02:10:30
$carbon = Carbon::createFromTimestamp(12151111215);  //
$carbon = Carbon::createFromTimeString('02:10:30'); // текущ. дата + 02:10:30
$carbon = Carbon::createFromFormat('Ymd', '20180523');  // строка парсится в соответствии с шаблоном
$carbon = Carbon::parse('2015-5-4 21:23:11.152456'); // попытается распарсить дату из произвольной строки

$cp = $carbon->copy();

echo $carbon->format('Y-m-d');          // вывод в нужном формате
echo $carbon->toDateTimeString();       // преобразовать к строке всю дату + время
echo $carbon->toDateString();           // без времени
echo $carbon->toTimeString();           // только время (без даты)
echo $carbon->toFormattedDateString();  // Nov 25, 1973
echo $carbon->toDayDateTimeString();    // Mon, Nov 25, 1973 3:34 AM

echo $carbon->dayOfWeek;   // 1 (день недели)
echo $carbon->year;    // 1973
echo $carbon->month;   // 11
// и так далее


// Локализация

Carbon::setLocale('ru_Ru'); // Прописать в AppServiceProvider::boot()
$carbon->traslatedFormat('F'); // Вывести месяц словом

// или
setlocale(LC_TIME, 'Russian');
echo $carbon->formatLocalized('%A %d %B %Y');  // но в кодировке windows-1251
echo iconv('windows-1251', 'utf-8', $carbon->formatLocalized('%A %d %B %Y')); // преобразование в кодировку utf-8


// Сравнение дат

$carbon2 = Carbon::parse('2015-5-4 21:23:11.152456');
$check = $carbon->eq($carbon2);      // $carbon === $carbon2
$check = $carbon->gt($carbon2);      // $carbon > $carbon2
$check = $carbon->gte($carbon2);     // $carbon >= $carbon2
$check = $carbon->lt($carbon2);      // $carbon < $carbon2
$check = $carbon->lte($carbon2);     // $carbon <= $carbon2

echo Carbon::now()->closest($carbon, $carbon2); // ближайщая к текущей из переданных дат
echo Carbon::now()->farthest($carbon, $carbon2); // дальняя к текущей из переданных дат

var_dump($carbon->isToday());       // сегодня?
var_dump($carbon->isMonday());      // понедельник?
var_dump($carbon->isTuesday());     // вторник?
// и так далее

// Арифметические операции над датами

$carbon->addYears(10);      // добавить 10 лет к дате
$carbon->subYears(10);      // минус 10 лет от даты
$carbon->addCentury();      // добавить век (по умолчанию 1)
// и так далее

$carbon->add(1, 'day');

echo $carbon->diffForHumans($carbon2);  // разница в человекопонятном виде, например: "6 years after"
echo $carbon->diffInHourse($carbon2);   // разница в часах
echo $carbon->diffInDays($carbon2);     // разница в днях
// и так далее

// Формат

$mutable->isoFormat('dddd D');             // string(9) "Sunday 10"
```
