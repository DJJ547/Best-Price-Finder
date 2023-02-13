from amazonFinder.amazonScraper import AmazonScraper


def main():
    keyword = 'tamiya model kit'
    az_scraper = AmazonScraper(keyword)
    ref_and_price = az_scraper.get_response()
    price = ref_and_price[0]
    ref = ref_and_price[1]
    print(price)
    print(ref)

if __name__ == '__main__':
    main()
