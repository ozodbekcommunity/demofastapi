from fastapi import *
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.get("/")
async def homepage():
    return {"status": "success"}

@app.get("/product")
async def getdata(item: Item = Depends()):
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price

    }
