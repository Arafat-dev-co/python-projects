import requests
from bs4 import BeautifulSoup
import csv



url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

filename = "scraper.csv"
field = ["Text", "Author"]

with open(filename, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        
        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text
            print(text, "|", author)
    

    

            writer.writerow({"Text": text, "Author": author})
            print(f"Saved: {text[:20]}... by {author}")

        print("Scraping complete")



