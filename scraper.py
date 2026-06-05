import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO)

def scrape_vale360():
    url = "https://www.vale360news.com.br/tag/cacapava/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # Captura títulos dentro de h3.entry-title > a
    noticias = [h.get_text().strip() for h in soup.find_all("h3", class_="entry-title")][:5]

    logging.info(f"Capturadas {len(noticias)} notícias: {noticias}")
    return noticias

if __name__ == "__main__":
    noticias = scrape_vale360()
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump({"noticias": noticias}, f, ensure_ascii=False, indent=2)
    logging.info("Arquivo data/news.json atualizado com sucesso.")
