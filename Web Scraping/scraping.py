import requests
from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()
file = open('Web Scraping\Sources.txt', 'r')
sites = file.readlines()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
url = sites[0].strip()
infos = scraper.get(url)
soup = BeautifulSoup(infos.content, 'html.parser')

imoveis = soup.find_all("a", {"class": "property-card__content-link js-card-title"}, href = True)

link_to_imoveis = [imovel['href'] for imovel in imoveis]

for imovel in link_to_imoveis:
    print(f'Link para o imovel: {imovel}')
