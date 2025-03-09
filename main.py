import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.route import route
from config.settings import settings

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API para enviar correos y almacenarlos en MongoDB"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza con dominios específicos en producción
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Restringir métodos permitidos
    allow_headers=["Authorization", "Content-Type"],  # Evitar permitir todos los headers
)

# Registrar las rutas de la API
app.include_router(route)

# Punto de entrada para desarrollo y producción
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
