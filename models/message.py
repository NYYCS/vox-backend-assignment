from pydantic import BaseModel, Field
# Using pydantic there isn't any CRUD involved for messages

class MessageGet(BaseModel):
    sender: str
    receiver: str
    text: str

class Message(BaseModel ):
    msg: str = Field(alias='text')

    class Config:
        allow_population_by_field_name = True