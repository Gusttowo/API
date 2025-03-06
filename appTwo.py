from fastapi import FastAPI, HTTPException
from routes.route import route


app = FastAPI(title="REST API with FastAPI, Yagmail and MongoDB",
              description="Esta es una API Rest que envia correos y los almacena en Mongo",
              version="0.0.1")

#Agregamos las rutas a la app
app.include_router(route)
