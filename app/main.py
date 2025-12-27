from fastapi import FastAPI
from app.ai_service import generate_summary, suggest_alternatives, rephrase_text
from app.schemas import Recipe, RecipeResponse, RephraseRequest, RephraseResponse


app = FastAPI(
    title="FlavorFusion AI",
    description="Cloud-native recipe sharing API with AI-powered enhancements",
    version="0.1.0"
)

# Temporary in-memory storage
recipes = []


@app.get("/")
def root():
    return {"message": "Welcome to FlavorFusion AI!"}


@app.get("/recipes")
def list_recipes():
    return recipes


@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    if recipe_id < 0 or recipe_id >= len(recipes):
        return {"error": "Recipe not found"}
    return recipes[recipe_id]


@app.post("/recipes", response_model=RecipeResponse)
async def add_recipe(recipe: Recipe):
    summary = await generate_summary(recipe.ingredients, recipe.instructions)
    recipe.summary = summary
    recipes.append(recipe.dict())

    return {
        "message": "Recipe added",
        "id": len(recipes) - 1,
        "summary": summary
    }



@app.get("/ingredients/{ingredient}/alternatives")
async def ingredient_alternatives(ingredient: str):
    alternatives = await suggest_alternatives(ingredient)
    return {
        "ingredient": ingredient,
        "alternatives": alternatives
    }

@app.post("/rephrase", response_model=RephraseResponse)
async def rephrase_endpoint(payload: RephraseRequest):
    result = await rephrase_text(payload.text, payload.tone)
    return {
        "original": payload.text,
        "tone": payload.tone,
        "rephrased": result
    }
