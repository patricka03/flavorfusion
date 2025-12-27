import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def generate_summary(ingredients: list, instructions: str) -> str:
    """
    Generate a short recipe summary in exactly 2–3 sentences.
    """

    prompt = (
        "Summarize the following recipe in **exactly 2–3 sentences**. "
        "Do not exceed 3 sentences. Focus on flavour, cooking style, and key steps.\n\n"
        f"Ingredients: {ingredients}\n"
        f"Instructions: {instructions}\n"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=80,
        temperature=0.6,
    )

    return response.choices[0].message.content.strip()


async def rephrase_text(text: str, tone: str = "professional") -> str:
    """
    Rephrase text in a user-defined tone, limited to 2–3 sentences.
    """

    prompt = (
        f"Rephrase the following text in a {tone} tone. "
        "Your response must be 2–3 sentences only. "
        "Do not exceed 3 sentences.\n\n"
        f"Text:\n{text}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()


async def suggest_alternatives(ingredient: str) -> list:
    """
    Use AI to suggest 3 alternative ingredients for a given ingredient.
    """
    prompt = (
        f"Suggest exactly 3 alternative ingredients for '{ingredient}'. "
        "Return them as a simple comma-separated list with no explanation."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=30,
        temperature=0.7,
    )

    raw = response.choices[0].message.content.strip()
    return [item.strip() for item in raw.split(",")][:3]
