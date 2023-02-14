from amazonFinder.amazonScraper import AmazonScraper


def main():
    keyword = 'Tamiya 35346 1/35 US Medium Tank M4A3E8 Sherman Plastic Model Kit'
    az_scraper = AmazonScraper(keyword)
    ref_and_price = az_scraper.get_response()
    price = ref_and_price[0]
    ref = ref_and_price[1]
    print(price)
    print(ref)


if __name__ == '__main__':
    main()
