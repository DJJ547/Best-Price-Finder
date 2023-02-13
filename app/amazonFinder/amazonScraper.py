import requests
from glob import glob
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep


class AmazonScraper:

    def __init__(self, keyword):
        self.HEADERS = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/109.0.0.0 Safari/537.36'),
            'Accept-Language': 'en-US, en;q=0.5'
        }
        self.baseURL = 'https://www.amazon.com/s?k='
        self.keyword = keyword

    def get_response(self):
        cheapest_price = float('inf')
        cheapest_item_ref = ''

        title = self.parse_url_string(self.keyword)
        url = self.baseURL + title
        print(url)
        webpage = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        links = soup.find_all('div', attrs={'class': 'a-section a-spacing-base'})

        for link in links:
            ref = link.find('a', {'class': 'a-link-normal s-no-outline'})['href']
            price = float(link.find('span', {'class': 'a-offscreen'}).text.replace('$', ''))
            if price < cheapest_price:
                cheapest_price = price
                cheapest_item_ref = ref
        return cheapest_price, cheapest_item_ref

    def parse_url_string(self, input_str):
        print(input_str.replace(' ', '+'))
        return input_str.replace(' ', '+')
