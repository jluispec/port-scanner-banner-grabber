# Port Scanner + Banner Grabber - JLPEC

Este proyecto contiene un script en Python 3 para escanear puertos de una determinada dirección IP (Entorno Controlado), utilizando la librería Socket.

## Estructura del Proyecto

- `scanner.py`: Archivo Python que contiene el código del script del Port Scanner + Banner Grabber.

## Funcionalidades

- Escaneo de puertos del 1 al 200 de una determinada dirección IP local (127.0.0.1) listando solo los puertos abiertos (Port Scanner).
- Por cada puerto abierto, se lista el mensaje que el servicio envía automáticamente, en caso de no obtener respuesta solo se indica que el Banner no está diponible (Banner Grabber).

## Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Accede a la Terminal o Consola de tu Sistema Operativo
3. Ejecuta `python scanner.py` para iniciar el script.
4. Espera hasta que el script indique que ha concluido con el análisis o escaneo.

## Ejemplo de salida

La IP objetivo a escanear es 127.0.0.1 del puerto 1 al 200...  
********************************************************************************  
Puerto 80: ABIERTO  
   Banner: HTTP/1.1 200 OK  
Puerto 135: ABIERTO  
   Banner: No disponible  
********************************************************************************  
Escaneo de 127.0.0.1 del puerto 1 al 200 completado

