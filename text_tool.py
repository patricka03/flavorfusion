import argparse
import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_text(input_file: str = None) -> str:
    """
    Reads text from a file if provided, otherwise returns a default paragraph.
    """
    if input_file:
        with open(input_file, "r") as f:
            return f.read()

    return (
        "Content creators often struggle to condense long-form writing into concise summaries "
        "or rewrite their ideas in different tones. This tool demonstrates how AI can help "
        "automate summarisation and rephrasing tasks."
    )


def summarise_text(text: str) -> str:
    """
    Summarise text in exactly 2–3 sentences.
    """
    prompt = (
        "Summarise the following text in exactly 2–3 sentences. "
        "Do not exceed 3 sentences.\n\n"
        f"Text:\n{text}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=80,
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()


def rephrase_text(text: str, tone: str) -> str:
    """
    Rephrase text in a user-defined tone, limited to 2–3 sentences.
    """
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


def main():
    parser = argparse.ArgumentParser(description="AI-Powered Text Summariser & Enhancer")
    parser.add_argument("--input", type=str, help="Path to input .txt file")
    parser.add_argument("--tone", type=str, default="professional", help="Tone for rephrasing")
    args = parser.parse_args()

    original_text = read_text(args.input)
    summary = summarise_text(original_text)
    rephrased = rephrase_text(original_text, args.tone)

    print("\n--- ORIGINAL TEXT ---\n")
    print(original_text)

    print("\n--- SUMMARY (2–3 sentences) ---\n")
    print(summary)

    print(f"\n--- REPHRASED TEXT ({args.tone} tone, 2–3 sentences) ---\n")
    print(rephrased)


if __name__ == "__main__":
    main()
