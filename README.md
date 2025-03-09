# Proyecto FastAPI con MongoDB

Este proyecto es una API desarrollada con FastAPI, Yagmail y conectada a una base de datos MongoDB para envio y almacenamiento de los correos.

## Requisitos

Asegúrate de tener instalados los siguientes programas:

- Python 3.8+

- MongoDB

- Pip

## Instalación

1. Clona este repositorio:

```
git clone https://github.com/Gusttowo/API.git
cd API
```

2. Crea un entorno virtual y actívalo:

```
python -m venv venv
venv\Scripts\activate
```

3. Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

4. Configura la variables de entorno

- Crear un archivo llamado `.env`

- Agrega las variables `MONGO_URI`, `EMAIL_USER` y `EMAIL_PASSWORD`

1. Configuración de la Base de Datos

Para esta api se usa un servicio en MongoDB Atlas. Por lo que se configura la siguiente variable:


```
MONGO_URI = mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<db-name>?retryWrites=true&w=majority
```

Si lo vas a ejecutar en local, asegurate de tener intalado MongoDB y cambia la variable por:

```
MONGO_URI = mongodb://localhost/
```

Asegúrate de tener una base de datos llamada **API** y una coleccion **emails** antes de ejecutar la API.

## Ejecución de la API

Inicia el servidor de FastAPI:

```
uvicorn main:app --reload
```

Accede a la documentación interactiva de la API en:

Swagger UI: http://127.0.0.1:8000/docs