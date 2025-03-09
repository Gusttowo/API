from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class Email(BaseModel):
    id: Optional[str] = None
    sender: EmailStr
    recipient: EmailStr
    subject: str
    body: str
    date: Optional[datetime] = None  # Fecha en formato ISO 8601
