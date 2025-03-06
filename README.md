# Proyecto FastAPI con MongoDB

Este proyecto es una API desarrollada con FastAPI, Yagmail y conectada a una base de datos MongoDB para envio y almacenamiento de los correos.

## Requisitos

Asegúrate de tener instalados los siguientes programas:

- Python 3.8+

- MongoDB

- Pip

## Instalación

1. Clona este repositorio:

git clone https://github.com/Gusttowo/API.git
cd API

2. Crea un entorno virtual y actívalo:

- python -m venv venv
- venv\Scripts\activate

3. Instala las dependencias del proyecto:

- pip install -r requirements.txt

4. Configuración de la Base de Datos

Asegúrate de que MongoDB esté instalado en tu sistema.

Para iniciar MongoDB, simplemente ejecuta el siguiente comando en la terminal:

- mongod

Asegúrate de tener una base de datos creada antes de ejecutar la API.

## Ejecución de la API

Inicia el servidor de FastAPI:

- uvicorn appTwo:app --reload

Accede a la documentación interactiva de la API en:

Swagger UI: http://127.0.0.1:8000/docs

