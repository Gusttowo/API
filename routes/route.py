import os
from dotenv import load_dotenv
from fastapi import APIRouter, Response, status, HTTPException
from config.db import client
from schemas.route import emailEntity, emailsEntity
from models.models import Email
from passlib.hash import sha256_crypt  # Encriptar datos
from bson import ObjectId  # Para convertir un id a un ObjectId
from yagmail import SMTP  # Para enviar correos

route = APIRouter()
load_dotenv()

@route.get("/")
def welcome():
    return "Hola, Bienvenido a mi API"

# Obtener todos los emails
@route.get("/api/emails", response_model=list[Email], tags=["CRUD EMAIL"])
def get_all_emails():
    return emailsEntity(client.API.emails.find())

# Guardar y enviar un email
@route.post("/api/emails", response_model=Email, tags=["CRUD EMAIL"])
def send_email(email: Email):
    if not email.recipient or not email.subject:
        raise HTTPException(status_code=400, detail="El destinatario y el asunto son obligatorios")

    new_email = dict(email)
    del new_email["id"]  # Eliminamos el id para evitar duplicados

    Id = client.API.emails.insert_one(new_email).inserted_id
    email_found = client.API.emails.find_one({"_id": Id})

    try:
        with SMTP(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD')) as yag:
            yag.send(new_email["recipient"], new_email["subject"], new_email["body"])
    except Exception:
        raise HTTPException(status_code=500, detail="Error al enviar el correo")

    return emailEntity(email_found)

# Obtener un email por ID
@route.get("/api/emails/{id}", response_model=Email, tags=["CRUD EMAIL"])
def get_one_email(id: str):
    try:
        email = client.API.emails.find_one({"_id": ObjectId(id)})
        if not email:
            raise HTTPException(status_code=404, detail="Email no encontrado")
        return emailEntity(email)
    except Exception:
        raise HTTPException(status_code=400, detail="ID inválido")

# Eliminar un email
@route.delete("/api/emails/{id}", response_model=Email, tags=["CRUD EMAIL"])
def delete_email(id: str):
    email = client.API.emails.find_one({"_id": ObjectId(id)})
    if not email:
        raise HTTPException(status_code=404, detail="Email no encontrado")

    client.API.emails.find_one_and_delete({"_id": ObjectId(id)})
    return emailEntity(email)

# Actualizar un email
@route.put("/api/emails/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["CRUD EMAIL"])
def update_email(id: str, email: Email):
    existing_email = client.API.emails.find_one({"_id": ObjectId(id)})
    if not existing_email:
        raise HTTPException(status_code=404, detail="Email no encontrado")

    update_data = {k: v for k, v in dict(email).items() if v is not None}
    client.API.emails.find_one_and_update({"_id": ObjectId(id)}, {"$set": update_data})

    return emailEntity(client.API.emails.find_one({"_id": ObjectId(id)}))
