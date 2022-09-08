Factory Method (Фабричный метод) - это делегирование создания объектов специальным классам.

- Это порождающий шаблон проектирования.
- Применяется для получения объектов при абстрактных типах.

Пример: функционал, реализующий разные варианты отрисовки формы на сайте. 

```php 
abstract class AbstractForm 
{
	public function render()
	{
		return $this->createCuiKit()
			->buildButton()
			->draw();
	}

	abstract function createCuiKit(): GuiInterface;
}

```

1-й вариант отрисовки формы:
```php 
class BootstrapFactory extends AbstractForm 
{
	public function createCuiKit(): GuiInterface
	{
		return new BootstrapForm();
	}
}

```

2-й вариант отрисовки формы:
```php 
class SemanticFactory extends AbstractForm 
{
	public function createCuiKit(): GuiInterface
	{
		return new SemanticForm();
	}
}

```

Выбор отрисовки формы в контроллере:
```php 
class FormController 
{
	public function renderForm()
	{
		$form = new BootstrapFactory();
		// $form = new SemanticForm();
		$result = $form->render();

		return view('form', compact('result'));
	}
}

```

