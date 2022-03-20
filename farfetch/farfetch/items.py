from scrapy import Field
from scrapy.item import Item


class FarfetchItem(Item):
    brand = Field()
    url = Field()
    product = Field()
    sku = Field()
    img_search_page = Field()
    image_urls = Field()
    image_uris = Field()
    spider = Field()
    spider_version = Field()
    timestamp = Field()
    stock_and_prices = Field()
    description = Field()