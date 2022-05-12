from pydantic import BaseModel
from typing import List, Optional


class Ingredient(BaseModel):
    name: str
    amount: str


class Step(BaseModel):
    name: str
    substeps: Optional[List[str]]


class Recipe(BaseModel):
    name: str
    description: str
    ingredients: List[Ingredient]
    steps: Optional[List[Step]]
    produces: str
    source: Optional[str]
