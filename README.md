# Performance Testing con locust

Este proyecto realiza pruebas de performance sobre la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts) utilizando Locust.

## Objetivo
Simular 100 usuarios concurrentes accediendo al endpoint `GET /posts`.
Medir:
 Tiempo de respuesta promedio.
 Porcentaje de errores (en caso de que haya).
 Máximo tiempo de respuesta.

## Requisitos previos
Antes de ejecutar las pruebas se debe tener instalado lo siguiente:
- Python 3.10 o superior
- Locust
- python-dotenv

Instalar dependencias:
```bash
pip install -r requirements.txt
```
## Configuracion
Crear un archivo .env en la raíz del proyecto con la siguiente variable
TARGET_HOST=https://jsonplaceholder.typicode.com

## Ejecucion
Para correr la prueba en modo headless (sin interfaz web) con 100 usuarios y una tasa de arranque de 10 usuarios por segundo durante 1 minuto:
```
locust -f locustfile.py --headless -u 100 -r 10 -t 1m --csv=reports/results --html=reports/reporte.html
```
Locust genera reportes en formato CSV en la carpeta reports/. Estos archivos contienen métricas detalladas de la prueba, incluyendo tiempos de respuesta y porcentaje de errores.
Sin embargo en la linea de comandos anterior se agrega un reporte HTML que tambien se almacena en la carpeta  reports/. Para visualizarlo solo abrelo en tu navegador una vez terminen las pruebas

## Logs
Durante la ejecucion vas a ver varios logs en consola, puedes configurarlo como desees en el archivo tasks/get_posts_task.py el cual posee la logica principal de la prueba.

 Autor
Luis Mosquera – QA Engineer 
