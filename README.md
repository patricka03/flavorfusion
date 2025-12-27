🍲 FlavorFusion AI – Cloud‑Native Recipe API with AI Enhancements

FlavorFusion AI is a lightweight, cloud‑native recipe API that blends traditional recipe management with modern AI‑powered enhancements.
It allows users to store recipes, generate AI‑written summaries, rephrase text in custom tones, and get ingredient substitutions — all through clean, well‑structured FastAPI endpoints.

✨ Features
🔹 AI‑Generated Recipe Summaries
Automatically condense recipe instructions into 2–3 sentence summaries focusing on:
Flavour profile
Cooking style
Key preparation steps

🔹 Ingredient Substitution Suggestions
Ask the API for alternatives to any ingredient and receive exactly 3 AI‑generated substitutes.

🔹 Tone‑Controlled Text Rephrasing
Rephrase any text in a tone of your choice:
Professional
Casual
Humorous
Persuasive
Shakespearean
Pirate‑speak
…or anything else you specify

🔹 Simple, Clean REST API
Built with FastAPI for:
Automatic documentation
Type‑safe request/response models
Async performance

🚀 API Endpoints
Root
GET /  
Returns a welcome message.
List Recipes
GET /recipes  
Returns all stored recipes (in‑memory).
Get Recipe by ID
GET /recipes/{recipe_id}  
Returns a single recipe or an error if not found.
Add Recipe (AI Summary Included)
POST /recipes  
Request body (example):
json
{
  "title": "Beef Stew",
  "ingredients": ["beef", "carrots", "onions"],
  "instructions": "Brown the beef, simmer with vegetables for 2 hours."
}
Response:
json
{
  "message": "Recipe added",
  "id": 0,
  "summary": "AI‑generated 2–3 sentence summary..."
}
Ingredient Alternatives
GET /ingredients/{ingredient}/alternatives  
Returns exactly 3 AI‑generated substitutes.
Rephrase Text
POST /rephrase  
Request body:
json
{
  "text": "This stew is hearty and delicious.",
  "tone": "shakespearean"
}
Response:
json
{
  "original": "...",
  "tone": "shakespearean",
  "rephrased": "AI‑generated 2–3 sentence rephrasing..."
}

🧠 AI Service Logic
FlavorFusion AI uses OpenAI’s API to power three core features:
1. Recipe Summaries
Model: gpt-3.5-turbo (or your updated model)
Output: exactly 2–3 sentences
Focus: flavour, cooking style, key steps
2. Text Rephrasing
Tone is fully user‑defined
Output: 2–3 sentences
Great for creative or professional rewriting
3. Ingredient Alternatives
Returns exactly 3 substitutes
Clean comma‑separated parsing

🛠️ Tech Stack
FastAPI – high‑performance Python API framework
Python 3.10+
OpenAI API – generative AI capabilities
Uvicorn – ASGI server

📦 Installation & Setup
Clone the repo:
bash
git clone <your-repo-url>
cd flavorfusion_api
Install dependencies:
bash
pip install -r requirements.txt
Set your OpenAI API key:
bash
export OPENAI_API_KEY="your-key-here"
Run the server:
bash
uvicorn app.main:app --reload
Open the interactive docs:
Code
http://127.0.0.1:8000/docs

🤝 Contributing
Contributions are welcome — feel free to open issues or submit pull requests.
