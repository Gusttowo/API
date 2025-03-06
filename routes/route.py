import os
from dotenv import load_dotenv
from fastapi import APIRouter, Response, status
from config.db import client
from schemas.route import emailEntity, emailsEntity
from models.models import Email
from passlib.hash import sha256_crypt #Encriptar datos
from bson import ObjectId #Para convertir un id a un ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from yagmail import SMTP

route = APIRouter()
load_dotenv()

@route.get('/')
def welcome():
    return "Hola, Bienvenido a mi API"


@route.get('/api/emails', response_model= list[Email], tags=["CRUD EMAIL"])
def get_all_emails():
    return emailsEntity(client.API.emails.find())

#Guardar email
@route.post('/api/emails', response_model=Email, tags=["CRUD EMAIL"])
def send_email(email: Email):
    new_email = dict(email)
    #new_email["password"] = sha256_crypt.encrypt(new_email["password"]) #para encryptar la contraseña
    del new_email["id"] #Eliminamos el id para que no se dupliquen

    Id = client.API.emails.insert_one(new_email).inserted_id
    email_found = client.API.emails.find_one({"_id": Id})
    print(new_email)

    #Enviar email
    with SMTP(os.getenv('email'), os.getenv('contrasena')) as yag:
        yag.send(new_email["recipient"], new_email["subject"], new_email["body"])

    return emailEntity(email_found)


#Buscar email por id
@route.get('/api/emails/{id}', response_model=Email, tags=["CRUD EMAIL"])
def get_one_emails(id: str):
    print(id)
    return emailEntity(client.API.emails.find_one({"_id": ObjectId(id)}))


#Eliminar email
@route.delete('/api/emails/{id}', response_model=Email, tags=["CRUD EMAIL"])
def delete_email(id: str):
    emailEntity(client.API.emails.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

#Actualizar email
@route.put('/api/emails/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["CRUD EMAIL"])
def update_email(id: str, email: Email):
    client.API.emails.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(email)})
    return emailEntity(client.API.emails.find_one({"_id": ObjectId(id)}))