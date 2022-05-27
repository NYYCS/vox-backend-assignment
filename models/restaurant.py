from sqlmodel import SQLModel, Field

class RestaurantBase(SQLModel):
    name: str
    hooli_number: str

class Restaurant(RestaurantBase, table=True):
    id: str = Field(default=None, primary_key=True)
    contact_phone: str

class RestaurantUpdate(RestaurantBase):
    pass