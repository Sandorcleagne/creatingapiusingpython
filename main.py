from concurrent.futures import ProcessPoolExecutor
from itertools import product
import json
from lib2to3.pytree import Base
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Products(BaseModel):
    id: Optional[int] =None
    title: str
    description: str
    price: int
    discountPercentage : float
    rating : float
    stock:int
    brand : str
    category: str
    thumbnail: str
    images: str

with open("demo.json", "r") as f:
    product = json.load(f)["products"]
print(product)