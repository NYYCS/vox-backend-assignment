from sqlmodel import SQLModel, Field

class Customer(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    hooli_number: str = Field(default=None, index=True)
    name: str
    delivery_address: str