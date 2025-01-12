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


print(soup)