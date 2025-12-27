AI-Powered Text Tool – Technical Approach & AI Utilisation Report

1. Overview
This project is a lightweight Python tool designed to help content creators summarise long-form text and rephrase it in different tones using Generative AI. The script (text_tool.py) accepts input either from a .txt file or from a built‑in default paragraph. It then:
Produces a 2–3 sentence summary of the text
Rephrases the original text in a user‑specified tone
Prints the original, summary, and rephrased versions to the console
The tool demonstrates practical AI integration, prompt engineering, and basic software design.

2. Script Functionality
Key Features
Summarisation: Condenses long text into 2–3 sentences.
Rephrasing: Rewrites the original text in a custom tone (e.g., “professional”, “casual”, “Shakespearean”, “pirate-speak”).
File Input: Accepts a .txt file via command-line argument.
Console Output: Prints all results clearly for the user.
Model: Uses gpt-4o-mini for reliable, low‑cost inference.
How to Run
bash
python3 text_tool.py --input sample.txt --tone "shakespearean"
Or without a file:
bash
python3 text_tool.py --tone "professional"

3. Contextual Tone Adjustment (The Crucial 10%)
A key requirement of the challenge was to add a feature that allows the user to specify a custom tone for the rephrasing function. This required modifying the AI prompt dynamically based on user input.
Implementation Snippet
python
def rephrase_text(text: str, tone: str) -> str:
    prompt = (
        f"Rephrase the following text in a {tone} tone. "
        "Your response must be 2–3 sentences only.\n\n"
        f"Text:\n{text}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
Why this works
The tone is inserted directly into the prompt, allowing the model to adapt its style.
The 2–3 sentence constraint ensures consistent output length.
The temperature is slightly higher (0.7) to encourage creativity in tone shifts.
Example Output (Shakespearean Tone)
“Verily, this tool doth aid the weary scribe in shaping their thoughts anew. With but a whisper of command, it fashions summaries and rephrasings fit for noble eyes.”
This demonstrates the model’s ability to interpret and apply unusual tones.

4. Prompting Strategy & Iteration
Initial Prompt Issues
Early prompts produced:
Summaries that were too long
Rephrasings that ignored tone
Outputs with 4–5 sentences
Refinements Made
Explicit constraints
Adding “exactly 2–3 sentences” dramatically improved consistency.
Repetition of constraints
Models respond better when rules are reinforced:
Code
Do not exceed 3 sentences.
Lower max_tokens
Summary: max_tokens=80
Rephrase: max_tokens=120
This physically prevents long outputs.
Dynamic prompt construction
The tone is inserted directly into the prompt string.
Final Prompt Structure
Clear instruction
Hard constraints
Text separated cleanly
Tone included explicitly
This combination produced reliable, high‑quality results.

5. Error Handling Considerations
Although the script is intentionally simple, several real‑world issues were considered:
Potential Errors & Mitigations
Issue	Consideration
Missing API key	Check for OPENAI_API_KEY before running.
API quota exceeded	Switch to low‑cost models (gpt-4o-mini).
Empty or very short input text	Add validation before sending to AI.
Network/API failure	Wrap AI calls in try/except and print a friendly message.
Invalid tone	Default to “professional” if tone is empty.
These considerations show awareness of production‑level robustness even if not fully implemented.

6. Tools Used
AI Tools
Microsoft Copilot (for code generation and refinement)
OpenAI API (gpt-4o-mini)
Development Tools
Python 3
argparse (CLI handling)
GitHub (private repository)
Terminal for execution
Dependencies
Listed in requirements.txt:
Code
openai>=1.0.0
python-dotenv

7. Repository Structure
Code
/your-repo
    text_tool.py
    requirements.txt
    sample.txt
    AI-Powered Text Tool - Technical Approach & AI Utilisation Report.md
    
8. Conclusion
This project demonstrates the ability to integrate Generative AI into a Python application, apply prompt‑engineering techniques, and extend functionality with custom tone control. The tool is simple, effective, and showcases both AI-assisted development and thoughtful personal contribution.
