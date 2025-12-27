from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    instructions: str
    summary: Optional[str] = None

class RecipeResponse(BaseModel):
    message: str
    id: int
    summary: str

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Recipe added",
                "id": 0,
                "summary": "A warm, hearty stew with tender beef and rich flavours."
            }
        }

class RephraseRequest(BaseModel):
    text: str
    tone: Optional[str] = "professional"

class RephraseResponse(BaseModel):
    original: str
    tone: str
    rephrased: str
