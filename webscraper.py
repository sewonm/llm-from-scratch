from bs4 import BeautifulSoup 
import requests 

url = "https://en.wikipedia.org/wiki/Persona_5"
headers = {"User-Agent": "Mozilla/5.0 (compatible; LLM-dataset-scraper/1.0)"}
response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.text, 'html.parser') 
content = soup.select("div.mw-parser-output  p")
paragraphs = [p.get_text(strip=True) for p in content if p.get_text(strip=True)]

for p in paragraphs[:100]:
    print(p)