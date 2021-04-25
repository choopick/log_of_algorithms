import requests
from bs4 import BeautifulSoup
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0


url = "https://workey.codeit.kr/ratings/index"
response = requests.get(url)
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
# program_title_tags = soup.select('td.program')
td_tags = soup.select('td')[:4]

for tag in td_tags:
    print(tag.get_text())