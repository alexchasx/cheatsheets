Factory Method (Фабричный метод) - это порождающий шаблон проектирования. 
Он делегирует логику создания объектов дочерним классам.

- Применяется, когда неизвестно какой из объектов нужно создать.

Пример: функционал, реализующий отрисовку формы на сайте. 

```php 
abstract class AbstractForm 
{
	public function render()
	{
		$guiKit = $this->createCuiKit();

		return $guiKit->buildButton()->draw();
	}

	abstract function createCuiKit(): GuiInterface;
}

```
