from fastapi import *
from pydantic import BaseModel

api = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

@api.get("/")
async def homepage():
    return {"status": "success"}

@api.get("/product")
async def getdata(item: Item = Depends()):
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price
    }