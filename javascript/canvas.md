Canvas API предоставляет средства для рисования графики с помощью HTML-элемента <canvas>.

```html
<canvas id="canvas"></canvas>
```

```js
// получает ссылку на HTML-элемент <canvas>
const canvas = document.getElementById("canvas");
// получает контекст этого элемента — объект, на котором будет отображаться рисунок
const ctx = canvas.getContext("2d");
// размеры полотна:
canvas.width = 500; // пикселей
canvas.height = 500; // пикселей

ctx.fillStyle = "green";                // устанавливаем цвет заполнения фигуры
ctx.fillRect(10, 10, 150, 100);         // Заполненный прямоуголник: x, y, width, height
context.strokeStyle = "#22a6b3";      // устанавливаем цвет контура фигуры
context.strokeRect(10, 10, 100, 100);   // Пустой пряумоугольник
context.clearRect(10, 10, 50, 50);      // Очищает область в виде прямоугодника

ctx.lineWidth = 2;  // задаёт толщину линий
ctx.moveTo(0, 20);  // перемещает «курсор» в заданные координаты без создания линии
ctx.lineTo(50, 100);// соединяет последнюю точку подпути с указанными координатами (x, y). Сам метод не отображает линию — для этого нужно вызвать методы stroke() или fill()
ctx.stroke();       // используется для обводки (обрисовки) текущего или заданного контура цветом, заданным свойством strokeStyle

// Рисование фигур составленных из линий выполняется последовательно в несколько шагов
ctx.beginPath() //  «начать» серию действий описывающих отрисовку фигуры
ctx.closePath() // пытается завершить рисование проведя линию от текущей позиции к позиции с которой начали рисовать
ctx.fill() //  заливает фигуру сплошным цветом

ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise) // рисование дуги, где x и y центр окружности, далее начальный и конечный угол, последний параметр указывает направление

// две функции, для построения кубической кривой Бизье и квадратичной, соотвестствено
ctx.quadraticCurveTo(Px, Py, x, y) 
ctx.bezierCurveTo(P1x, P1y, P2x, P2y, x, y)

// Пример:
ctx.beginPath();
ctx.moveTo(10, 15);
ctx.bezierCurveTo(75, 55, 175, 20, 250, 15);
ctx.moveTo(10, 15);
ctx.quadraticCurveTo(100, 100, 250, 15);
ctx.stroke();

// Добавление текста
ctx.font = "24px Arial";
ctx.textAlign = "center";
let txt = "Hi canvas!";
ctx.fillText(txt, 10, 35);


ctx.fillStyle = color   // определяет цвет заливки 
ctx.strokeStyle = color // цвет линий цвет задается точно так же как и css, на примере все четыре способа задания цвета

// отрисовка изображения
var img = new Image();
img.src = 'myImage.png';    // Путь к изображению
// или
// let myImage = document.getElementById("flower");
img.onload = function() { // Событие которое будет исполнено в момент когда изображение будет загружено
    ctx.drawImage(image, x, y) // Где x и y это координаты левого верхнего угла изображения, а первый параметр это изображение
}

ctx.drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
// Первый параметр указывает на изображение
// sx, sy, sWidth, sHeight указывают параметры фрагмента на изображение-источнике
// dx, dy, dWidth, dHeight ответственны за координаты отрисовки фрагмента на холсте

// еще пример работы с изображением
let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
let imgLoader = document.getElementById("imgLoader");
imgLoader.addEventListener("change", upImage, false);
function upImage() {
    let fr = new FileReader(); // позволяет асинхронно читать содержимое файлов (или буферов сырых данных)
    fr.readAsDataURL(event.target.files[0]);
    fr.onload = function (e) {
        let img = new Image();
        img.src = event.target.result;
        img.onload = function () {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);
        };
        console.log(fr);
    };
}

// Добавление анимации в элемент canvas
window.onload = init;
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
canvas.height = 500;
canvas.width = 500;
var pos = {
    x: 0,
    y: 50,
};
function init() {
    draw();
}
function draw() {
    pos.x = pos.x + 5;
    if (pos.x > canvas.width) {
        pos.x = 0;
    }
    if (pos.y > canvas.height) {
        pos.y = 0;
    }
    ctx.fillRect(pos.x, pos.y, 100, 100);
    window.setTimeout(draw, 50);
}

// Чтобы очистить весь элемент canvas, следует написать:
ctx.clearRect(0, 0, canvas.width, canvas.height);
```