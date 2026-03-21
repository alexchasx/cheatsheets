# Конспект по Python из книг:
#   "Простой Python. Современный стиль программирования" Билл Любанович
#   "Изучаем Python" [2020] Эрик Мэтиз

## ТИПЫ ДАННЫХ ============================
""" 
1. Числовые
В Python есть три основных числовых типа: 
- Целые числа (int)
- Числа с плавающей точкой (float)
- Комплексные числа (complex), например: 3+4j, 2-1j.

2. Строки (тип str) - неизменяемый тип данных 
3. Логические (bool): True, False
4. Структуры
- Списки (list) — упорядоченные, изменяемые коллекции элементов.
- Кортежи (tuple) — упорядоченные, неизменяемые коллекции элементов.
- Множества (set) — неупорядоченные коллекции уникальных элементов.
- Фиксированное множество (frozenset)
- Словари (dict) — коллекции пар ключ-значение.
- Байты (bytes)
- Массив байтов (bytearray)
"""
x = type(y)         # верн тип данных
num = int(x);       # приведение к int

# // - оператор целочисленного деления
x = 7 // 2          # -> 3
#  3 ** 4           # 3 в 4-й степени

# продлеваем строки с помощью символа "\":
sum = 1 + \
    2 + \
    3

# к False приравниваются следующие значения:
#  None;
#  целое число 0;
#  число с плавающей точкой 0.0;
#  пустая строка ('');
#  пустой список ([]);
#  пустой кортеж (());
#  пустой словарь ({});
#  пустое множество (set()).
                    

## СТРОКИ ============================

string_1 = 'string 1'
string_2 = "string 1"
s1 = string_1.title()       # делает первые буквы каждого слова большими
s2 = string_1.upper()       #
s2 = string_1.lower()       #
string = str(98)            # ->'98' приведение к строке
string_3 = string_1 + string_2      # конкатенация строк с использованием "+"
str = 'ываыва' * 4          # строки можно размножать с помощью символа "*"
# можно извлекать подстроки с помощью [начало:конец]
str1 = 'sdfxcv sdfsdfsd sdf sdfsdfsd'
substr1 = str1[2:5]         # ->'fxcv'
substr2 = str1[-3:]         # ->'fsd' последние 3
list1 = str1.split(' ');    # разбивает строку в список
s3 = s3.rstrip()    # удаляет пробелы в конце строки
s3 = s3.lstrip()    # удаляет пробелы в начале строки
s3 = s3.strip()     # удаляет пробелы в начале и в конце строки

# Есть еще ф-ии 
#   join(), replace(), startswith(), endswith(), find(), rfind(), index(), rindex(), capitalize(), 
#   swapcase() - меняет регистр на противополож.
#   center(30) - отцентрирует строку в промежутке из 30 пробелов
#   ljust(30) - выравнивание по левому краю
#   rjust(30) - вырав-е по правому краю

s3 = f"{s1} {s2}"           # f-строка (с подстановкой переменных). Появились в версии Python 3.6
# для версии Python менее 3.6 используйте метод "format"
s3 = "{} {}".format(s1, s2)

if x == True:
    # ...
elif x == False:
    # ...
else:
    # ...


## СПИСКИ (массивы) ============================

x = [3, 6]

for i in x:
    x[i] +=3
    continue
    break
else:           # срабатывает после любых циклов: while, for, и др.
    # ...

y = range(5)            # создаст список со значениями от 1 до 5
y = range(5, 10, 3)     # создаст список со значениями от 5 до 10 c интервалом 3
y = len(x)              # length x
y.append(x)             # добавляет в конец
y.insert(index, value)  # добавляет значение по индексу
z = y.count(value)      # верн кол-во указанных значений
y.sort()
sorted_list = sorted(y) # создает новый отсортированный список
y.reverse() 
z = y.pop(index)        # удаление по индексу
del y[index]            # удаление по индексу
y.remove(value)         # удаление по значению
y.clear()               # очистка всего списка
y.extend([2,3])         # сливание списков
z = y.copy()

b = n[start:end:step]   # срез списка
b = n[0::2]             # срез всего списка через одного, начиная с первого элемента
b = n[0:2]              # от первого элемента до 3-го
b = n[:]                # копирование списка
last = x[-1]            #
sd = x[-3:]             # вернёт 3 последних элемента

x = list(y)             # преобраз-е в список

squares = [value**2 for value in range(1,11)]       # генератор списка. **2 - возведение в квадрат


## КОРТЕЖ (tuple) ============================

# Кортеж — это упорядоченная и НЕИЗМЕНЯЕМАЯ коллекция элементов, которые могут быть разных типов. 
#Меньше занимают памяти по сравнению со списками

# Создание кортежа
x = (9, 8, 7)
a = (9,)
y = 9, 8, 7
z = tuple([9, 8, 7])    # преобраз-е в кортеж

r = 3
d = 5
r, d = d, r     # свап 

x = z.count(value)
x = z.index(value)

z += (3, 5)     # кортежи можно объединять
z = s           # кортежи клонируются, а НЕ создаются ссылки


import os       # импорт модуля для работы с ОС

path = 'C:\\Users\...'
files = os.walk(path)               # рекурсивно обходит дерево каталогов и возр КОРТЕЖ
string = os.path.join(val1, val2)   # объедин строки с подстановкой правильных слэшев для путей ОС

if '.txt' in full_path:             # если в full_path содержится строка '.txt'
    spisok.append(z)

if i not in x: # если i НЕТ в списке x


import time     # модуль для работы с временем

time_1 = time.time()                # вернет текущий таймстамп
t2 = os.path.getctime(file_path)    # верн таймстамп создания файла


## СЛОВАРИ ============================

# похожи на объекты в JavaScript
alien_0 = {'color': 'green', 'points': 5}
# получить значение. Если ключа нет, то будет сообщение об ошибке
x = alien_0['color']
# чтобы не было ошибки при обращении к несущ ключу, использ-ся get
x = alien_0.ge('color', 'default')      # 'default' - значение по умолчанию

# добавление пары ключ-значение
alien_0['x_position'] = 0

# создание пустого словаря 
alien_0 = {}

# удаление пары ключ-значение
del alien_0['points']

# Перебор словаря
for key, value in alien_0.items():
    print("{key} {value}")
    
# перебо ключей
for name in alien_0.keys():
    print(name.title())

# перебо значенией
for name in alien_0.values():
    print(name.title())


## Ввод данных и циклы while ============================

# предложение юзеру ввести текст
message = input("Tell me something, and I will repeat it back to you: ")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

pets = [1, 2]
while 'cat' in pets:
    pets.remove('cat')


## Функции ================================

def my_function():          # объявление функции
    x = 7
    return x

def func(*a):       # *a - любое кол-во аргументов
    print(a)        # выведет КОРТЕЖ из всех аргументов

def func(h, *args, key):
    print(h)
    print(args)

func(1, 2, 3, key = 10)     # h -> 1; args -> (2, 3); key -> 10 (ключевой параметр после *args - обязательно именованый)

# **args - СЛОВАРЬ аргументов 
# *argsa - кортеж
def func(h, **args): 
    print(args)


## Области видимости ============================

x = 5
def fun1():
    y = 10
    print(x)    # x - видна внутри функции (как в JS)

print(y)        # y - НЕ сущест в глоб обл видим-ти

def func_2():
    global x    # чтобы иметь возможность перезаписать глобальную переменную
    x = 10


## ИМПОРТ ============================

# Импортирование всего модуля
import pizza

# Импортирование конкретных функций
from имя_модуля import функция_0, функция_1, функция_2

# Назначение псевдонима для функции
from имя_модуля import имя_функции as псевдоним

# Назначение псевдонима для модуля
import имя_модуля as псевдоним

# Импортирование всех функций модуля (не рекомендуется)
from pizza import *


## Классы ============================

class Car():
    def __init__(self, model, year):
        """Инициализирует атрибуты"""
        self.model = model
        self.year = year
        self.odometer_reading = 0   # значение по умолчанию

    def move(self):
        print(f"{self.model} is now moving.")


my_car = Car('audi', 2019)
my_car.move()


## Наследование ======================

class ElectricCar(Car):
    def __init__(self, model, year):
        super().__init__(model, year)


## Импорт классов ======================

# импорт классов из файла car.py
from car import Car, ElectricCar

# импорт всего модуля 
import car

# импорт всех классов из модуля (не рекомендуется)
from имя_модуля import *

# Использование псевдонимов
from electric_car import ElectricCar as EC


## Стандартная библиотека "random" ========================

from random import randint, choice
# вернет случайное число от 1 до 6
randint(1, 6)      

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# вернет случайной элемент списка или кортежа
first_up = choice(players)


## Файлы ======================

# чтение файла 'pi_digits.txt'
# open возвращает объект, представляющий файл
# Конструкция с with закрывает файл после того, как надобность в нем отпадет
with open('pi_digits.txt') as file_object:
    contents = file_object.read()       # read() читает содержимое и сохраняет его в строке
print(contents)

# Файлы можно открывать и закрывать явными вызовами open() и close(); 
# но если из-за ошибки в программе команда close() останется невыполненной, то файл не будет закрыт

# чтение по строкам (исп-ся for-in)
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines() # последовательно читает каждую строку из файла и сохраняет ее в списке
pi_string = ''
for line in lines:                  # lines вынесли за пределы with
    pi_string += line.strip()

# запись в файл (перезапись)
with open('programming.txt', 'w') as file_object:
    file_object.write("I love programming.")

# запись в файл (добавление в конец)
with open('programming.txt', 'a') as file_object:
    file_object.write("I love programming.")


## Исключения ===========================

try:
    print(5/0)
except ZeroDivisionError:       # ZeroDivisionError - определенное исключение
    print("You can't divide by zero!")
else:               # выполнится только при успешном срабатывании кода внтури try
    print('asdasd')


filename = 'alice.txt'
try:
    # encoding - если кодировка файла не совпадает с кодир-ой системы
    with open(filename, encoding='utf-8') as f:  
        contents = f.read()
except FileNotFoundError:       # FileNotFoundError - для отсутствия файла
    print(f"Sorry, the file {filename} does not exist.")


try:
    print(5/0)
except FileNotFoundError:
    pass            # pass - спец команда для пропуска ошибок
else:
    ...


numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# сохранение JSON в файл
import json
with open(filename, 'w') as f:
    json.dump(numbers, f)   


# чтение JSON из файла
with open(filename) as f:
    numbers = json.load(f)
print(numbers)


## Тестирование ===========================

import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
# Любой метод, имя которого начинается с test_, будет выполняться автоматически при запуске скрипта
# Если файл импортируется тестовым сценарием, то переменная __name__ будет содержать
# значение '__main__', и этот блок выполняться не будет

# assertEqual(a, b)             Проверяет, что a == b
# assertNotEqual(a, b)          Проверяет, что a != b
# assertTrue(x)                 Проверяет, что значение x истинно
# assertFalse(x)                Проверяет, что значение x ложно
# assertIn(элемент, список)     Проверяет, что элемент входит в список
# assertNotIn(элемент, список)  Проверяет, что элемент не входит в список



##  ===========================