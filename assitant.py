import requests
from bs4 import BeautifulSoup
from google import genai


def fetch_wikipedia(topic):
    formatted_topic = topic.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{formatted_topic}"
    
    # 2. Add a User-Agent header so Wikipedia doesn't block your script
    headers = {'User-Agent': 'MyAIApp/1.0 (myemail@example.com)'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Could not find the topic"

    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Scrape the paragraphs
    paragraphs = soup.find_all("p")

    text = ""
    for paragraph in paragraphs:
        p_text = paragraph.get_text().strip()
        if p_text:
            text += p_text + "\n"
            
            if len(text) > 500: 
                break

    return text if text else "No information found."

def summarize_text(text):
    
    client = genai.Client(api_key="YOUR_API_KEY_HERE")

    prompt = f"Summarize the following text in excalty 3 clear bullet points: \n\n{text}"

    response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
    
    return response.text
    

def main():
     topic = input("Enter your topic (e.g., Python_(programming_language)): ")

     print("Scraping Wikipedia...")
     text = fetch_wikipedia(topic)

     if text == "Could not find the topic" or text == "No information found.":
         print("Failed to get text from Wikipedia.")
         return

     print("Summarizing with AI...")
     summary = summarize_text(text)

     with open('summary.txt', 'w') as f:
         f.write(summary)

     print("\n--- AI SUMMARY ---")
     print(summary)

main()