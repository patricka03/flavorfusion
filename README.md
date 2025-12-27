# flavorfusion
🚀 AI‑Powered Text Summarizer & Enhancer




A lightweight, AI‑driven Python tool that summarises long‑form text and rephrases it in custom tones.
Perfect for content creators, writers, and anyone who wants fast, consistent text transformations.
✨ Features
🔹 Smart Summarisation
Condenses long paragraphs into 2–3 crisp sentences
Preserves meaning while improving clarity
🔹 Tone‑Controlled Rephrasing
Rewrites the original text in any tone you choose:
Professional
Casual
Humorous
Persuasive
Shakespearean
Pirate‑speak
…and anything else you can imagine
🔹 Flexible Input
Provide a .txt file
Or let the script use its built‑in default text
🔹 Clean CLI Interface
Simple command‑line usage powered by argparse.
🧠 How It Works
The script (text_tool.py) performs three steps:
Load text  
Reads from a file or uses a default paragraph.
Summarise  
Sends the text to the OpenAI API with a strict 2–3 sentence constraint.
Rephrase  
Rewrites the original text in a user‑defined tone.
All results print cleanly to the console.
🛠️ Installation
Clone the repo:
bash
git clone <your-private-repo-url>
cd <repo>
Install dependencies:
bash
pip install -r requirements.txt
Set your OpenAI API key:
bash
export OPENAI_API_KEY="your-key-here"
▶️ Usage
Run with a text file:
bash
python3 text_tool.py --input sample.txt --tone "shakespearean"
Run with default text:
bash
python3 text_tool.py --tone "professional"
📁 Project Structure
Code
.
├── text_tool.py
├── requirements.txt
├── sample.txt
└── AI-Powered Text Tool - Technical Approach & AI Utilisation Report.md
📦 Dependencies
Code
openai>=1.0.0
python-dotenv
🧩 Notes
This repository is intentionally simple to demonstrate AI integration and prompt engineering.
The FastAPI app in the /app directory is optional and not required for the challenge, but it showcases additional engineering capability.
🤝 Contributing
Contributions are welcome — feel free to open issues or submit pull requests.
📜 License
MIT License.
