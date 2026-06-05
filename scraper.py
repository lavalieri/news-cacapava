import requests
from bs4 import BeautifulSoup
import json

def scrape_vale360():
    url = "https://www.vale360news.com.br/tag/cacapava/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    noticias = [h.get_text().strip() for h in soup.find_all("h3", class_="entry-title")][:5]

    return noticias

if __name__ == "__main__":
    noticias = scrape_vale360()
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump({"noticias": noticias}, f, ensure_ascii=False, indent=2)
