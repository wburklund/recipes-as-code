from pydantic import BaseModel
from typing import List, Optional


class Image(BaseModel):
    alt: str = "Image"
    url: str


class Ingredient(BaseModel):
    name: str
    amount: str
    link: Optional[str]

    @property
    def formatted_name(self):
        if self.link is not None:
            return f"[{self.name}]({self.link})"
        else:
            return self.name


class Step(BaseModel):
    step: str
    substeps: Optional[List[str]]


class Recipe(BaseModel):
    image: Optional[Image]
    name: str
    description: str
    ingredients: List[Ingredient]
    steps: Optional[List[Step]]
    produces: str
    source: Optional[str]
