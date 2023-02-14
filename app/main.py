from amazonFinder.amazonScraper import AmazonScraper
from ebayFinder.ebayScraper import EbayScraper


def main():
    keyword = 'Tamiya 35346 1/35 US Medium Tank M4A3E8 Sherman Plastic Model Kit'
    az_scraper = AmazonScraper(keyword)
    az_ref_and_price = az_scraper.get_response()
    az_price = az_ref_and_price[0]
    az_ref = az_ref_and_price[1]

    eb_scraper = EbayScraper(keyword)
    eb_ref_and_price = eb_scraper.get_response()
    eb_price = eb_ref_and_price[0]
    eb_ref = eb_ref_and_price[1]

    if az_price < eb_price:
        print(f"This item is cheaper on Amazon with price: {az_price}, and here's the link: {az_ref}")
    elif az_price == eb_price:
        print("same price on both site, you can buy it on any one of them.")
    else:
        print(f"This item is cheaper on Ebay with price: {eb_price}, and here's the link: {eb_ref}")


if __name__ == '__main__':
    main()
