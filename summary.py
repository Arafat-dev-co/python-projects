from google import genai
import os

client = genai.Client(api_key="YOUR_API_KEY_HERE")

def main():
    print("--- AI TEXT SUMMARIZER ---")
    print("Paste the text you want to summarize below.")
    print("Press Enter twice when you are done")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    user_text = "\n".join(lines)

    if user_text == "":
        print("No text provided. Existing.")
        return

    print("\nSummarizing... (this may take a few seconds)")

    prompt = f"Summarize the following text in excalty 3 bullet points. Make it clear and concise:\n\n{user_text}"

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        summary = response.text

        with open("summary.txt", "w") as f:
            f.write(summary)



        print("\n--- SUMMARY ---")
        print(summary)
        print(f"\n[Saved to summary.txt]")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()