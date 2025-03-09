# Esquema para definir un solo email
def emailEntity(item) -> dict:
    return {
        "id": str(item["_id"]),  # Convertimos el ObjectId a string
        "sender": item["sender"],
        "recipient": item["recipient"],
        "subject": item["subject"], 
        "body": item["body"]
    }

# Esquema para definir varios emails
def emailsEntity(emails) -> list:
    return [emailEntity(item) for item in emails]  # Convertimos cada documento en un diccionario estructurado