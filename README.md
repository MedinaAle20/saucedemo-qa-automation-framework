# SauceDemo QA Automation Framework

[![Automation Tests](https://github.com/MedinaAle20/saucedemo-qa-automation-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/MedinaAle20/saucedemo-qa-automation-framework/actions/workflows/tests.yml)

Autor: Alejandro Medina

## Proposito del proyecto

Framework de automatizacion QA para validar flujos web de SauceDemo y endpoints publicos de JSONPlaceholder.

La parte UI prueba flujos principales de SauceDemo: login, catalogo, carrito, checkout y logout. La parte API usa JSONPlaceholder para validar requests GET, POST y DELETE.

El proyecto esta organizado con Page Object Model para que los tests queden simples y la logica de Selenium quede separada en clases de pagina.

Sitio web demo: https://www.saucedemo.com/

API publica: https://jsonplaceholder.typicode.com/

## Tecnologias utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- Page Object Model
- Git y GitHub

## Estructura del proyecto

```text
.
|-- conftest.py
|-- data/
|   `-- users.json
|-- pages/
|   |-- base_page.py
|   |-- cart_page.py
|   |-- checkout_page.py
|   |-- inventory_page.py
|   |-- login_page.py
|   `-- menu_page.py
|-- reports/
|   |-- logs/
|   |   `-- ejecucion.log
|   `-- screenshots/
|-- requirements.txt
|-- tests/
|   |-- api/
|   |   `-- test_jsonplaceholder_api.py
|   `-- ui/
|       `-- test_saucedemo_ui.py
`-- utils/
    `-- helpers.py
```

## Instalacion de dependencias

Desde la carpeta raiz del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecucion de pruebas

Ejecutar todos los tests:

```bash
pytest
```

Ejecutar solo pruebas UI:

```bash
pytest tests/ui
```

Ejecutar solo pruebas API:

```bash
pytest tests/api
```

Ejecutar pruebas UI sin abrir la ventana del navegador:

```bash
pytest tests/ui --headless
```

## Reporte HTML

Generar el reporte HTML:

```bash
pytest --html=reports/reporte.html --self-contained-html
```

El reporte queda disponible en:

```text
reports/reporte.html
```

El reporte muestra que tests se ejecutaron, si pasaron o fallaron y cuanto tardaron. Si una prueba UI falla, se guarda una captura y se agrega al reporte cuando Pytest HTML esta disponible.

## GitHub Actions

El proyecto incluye un workflow de integracion continua en:

```text
.github/workflows/tests.yml
```

Este workflow se ejecuta en cada push o pull request hacia `master` o `main`. Instala dependencias, corre las pruebas en modo headless y deja el reporte HTML como artefacto.

## Logs y screenshots

El log de ejecucion se guarda en:

```text
reports/logs/ejecucion.log
```

Los screenshots automaticos por fallo se guardan en:

```text
reports/screenshots/
```

El nombre de cada captura incluye el nombre del test y la fecha/hora, por ejemplo:

```text
test_login_invalido_20260705_153000.png
```

## Datos de prueba

Los datos externos se encuentran en:

```text
data/users.json
```

Incluye usuario valido, usuarios invalidos, datos de checkout y productos esperados del catalogo.

## Pruebas UI incluidas

- Login exitoso con usuario valido.
- Login invalido con datos incorrectos y usuario bloqueado.
- Validacion del catalogo de productos.
- Agregado de productos al carrito.
- Checkout completo.
- Validacion del menu lateral y logout.

## Pruebas API incluidas

- GET de lista de usuarios.
- POST de creacion de usuario.
- DELETE de usuario.

## Buenas practicas aplicadas

- Page Object Model para separar la interaccion con la pagina de la logica de los tests.
- Tests independientes entre si.
- Uso de waits explicitos en Selenium.
- Datos de prueba externos en JSON.
- Logging centralizado.
- Screenshots automaticos ante fallos.
- Separacion clara entre pruebas UI y API.
