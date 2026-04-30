# Proyecto de Automatización Urban Grocers

Este proyecto contiene pruebas automatizadas para la API de Urban Grocers, específicamente para la creación de kits de productos.

## Tecnologías utilizadas
* Python 3.14
* Pytest
* Requests (Librería para solicitudes HTTP)

## Estructura del proyecto
* **configuration.py**: Contiene la URL base y las rutas de los endpoints.
* **data.py**: Contiene los diccionarios de datos y encabezados.
* **sender_stand_request.py**: Contiene las funciones para enviar solicitudes POST.
* **create_kit_name_kit_test.py**: Contiene los casos de prueba automatizados.

## Instrucciones para ejecutar las pruebas
1. Asegúrate de que el servidor de Urban Grocers esté activo.
2. Actualiza la `URL_SERVICE` en el archivo `configuration.py` si es necesario.
3. Ejecuta el siguiente comando en la terminal de PyCharm:
   ```bash
   pytest create_kit_name_kit_test.py