import requests
from glob import glob
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import urllib.parse


class EbayScraper:

    def __init__(self, keyword):
        self.baseSearchURL = 'https://www.ebay.com/sch/'
        self.baseURL = 'https://www.ebay.com/'
        self.keyword = keyword

    def get_response(self):
        cheapest_price = float('inf')
        cheapest_item_ref = ''

        url_title = self.parse_url_string(self.keyword)
        url = self.baseSearchURL + url_title
        print(url)
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        links = soup.find_all('div', attrs={'class': 's-item__wrapper clearfix'})

        for link in links:
            ref = link.find('a', {'class': 's-item__link'})['href']
            price = float(
                link.find('div', {'class': 's-item__detail s-item__detail--primary'}).text.replace('$', '').split('to')[
                    0].strip())
            title = link.find('div', {'class': 's-item__title'}).text
            if price < cheapest_price and self.check_similarity_between_keyword_and_title(title):
                cheapest_price = price
                cheapest_item_ref = ref
        return cheapest_price, cheapest_item_ref

    def parse_url_string(self, input_str):
        return urllib.parse.quote_plus(input_str)

    # if the provided keyword is equal or over 90% similar to the title of the search result, return true, else false.
    def check_similarity_between_keyword_and_title(self, title):
        num_match = 0
        list1 = self.keyword.split(' ')
        list2 = title.split(' ')
        for i in list1:
            for j in list2:
                if i == j:
                    num_match += 1
                    list2.remove(j)
        if num_match / len(list1) >= 0.90:
            return True
        return False
