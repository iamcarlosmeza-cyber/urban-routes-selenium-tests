# qa-project-Urban-Routes-es

## Descripción del proyecto

Proyecto de automatización de pruebas para la aplicación web Urban Routes, una plataforma de solicitud de taxis. Las pruebas cubren el flujo completo de pedido de un taxi, desde la configuración de la ruta hasta la confirmación del modal de búsqueda de conductor.

## Tecnologías y técnicas utilizadas

- **Python 3** — lenguaje de programación principal
- **Selenium WebDriver** — automatización del navegador
- **pytest** — framework de ejecución de pruebas
- **Chrome WebDriver** — navegador utilizado para las pruebas
- **Page Object Model (POM)** — patrón de diseño utilizado para organizar los localizadores y métodos de la página en la clase `UrbanRoutesPage`, separando la lógica de las pruebas
- **WebDriverWait / Expected Conditions** — esperas explícitas para manejar elementos dinámicos
- **Chrome DevTools Protocol (CDP)** — utilizado para interceptar el código de confirmación del teléfono

## Descripción de las pruebas

Las pruebas están definidas en la clase `TestUrbanRoutes` dentro del archivo `test_main.py` y cubren las siguientes acciones:

1. `test_set_route` — Configurar la dirección de origen y destino
2. `test_select_comfort_tariff` — Seleccionar la tarifa Comfort
3. `test_fill_phone_number` — Rellenar el número de teléfono y confirmar con código SMS
4. `test_add_credit_card` — Agregar una tarjeta de crédito
5. `test_write_driver_message` — Escribir un mensaje para el conductor
6. `test_request_blanket_and_tissues` — Solicitar manta y pañuelos
7. `test_order_2_ice_creams` — Pedir 2 helados
8. `test_taxi_search_modal_appears` — Verificar que aparece el modal de búsqueda de taxi

## Instrucciones para ejecutar las pruebas

### Requisitos previos

- Python 3 instalado
- Google Chrome instalado
- ChromeDriver compatible con la versión de Chrome instalada

### Instalación de dependencias

```bash
pip install selenium pytest
```

### Configuración

En el archivo `data.py`, asegúrate de que la URL del servidor esté actualizada:

```python
urban_routes_url = 'https://<tu-url-del-servidor>?lng=es'
```

### Ejecución

Desde la carpeta raíz del proyecto, ejecuta:

```bash
pytest test_main.py -v
```
