from typing import Optional
from pydantic import BaseModel



class Email(BaseModel):
    id: Optional[str]
    sender: str
    recipient: str
    subject: str
    body:str
    #date: Optional[str]