#Esquema para definir un solo email
def emailEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "sender": item["sender"],
        "recipient": item["recipient"],
        "subject": item["subject"], 
        "body": item["body"]
    }


#Esquema para definir varios emails
def emailsEntity(emails) -> list:
    return [emailEntity(item) for item in emails] #Vamos a recorrer una lista, a cada item de la lista le vamos a dar el esquena de un solo item