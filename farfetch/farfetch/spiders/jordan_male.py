from scrapy.http.request import Request
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.utils.project import get_project_settings
from typing import  Dict
from parsel import Selector
import undetected_chromedriver as uc
from scrapy import signals
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from price_parser import Price
from urllib.parse import urljoin
from pyvirtualdisplay import Display
from typing import Optional
from farfetch.items import FarfetchItem
class JordanMaleSpider(Spider):
    name = 'farfetch-male-jordan'
    allowed_domains = ['farfetch.com']
    start_urls = ['https://www.farfetch.com/br/shopping/men/items.aspx']
    settings = get_project_settings()
    version = settings.get("VERSION")
    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?view=90&scale=285&rootCategory=Men&category=135968",
            '2' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=2&view=90&scale=285&rootCategory=Men&category=135968",
            '3' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=3&view=90&scale=285&rootCategory=Men&category=135968",
            '4' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=4&view=90&scale=285&rootCategory=Men&category=135968",
            '5' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=5&view=90&scale=285&rootCategory=Men&category=135968",
            '6' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=6&view=90&scale=285&rootCategory=Men&category=135968",
            '7' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=7&view=90&scale=285&rootCategory=Men&category=135968",
            '8' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=8&view=90&scale=285&rootCategory=Men&category=135968",
            '9' : "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?page=9&view=90&scale=285&rootCategory=Men&category=135968",
        }[page_number]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(JordanMaleSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider
    
    def spider_opened(self, spider):
        display = Display(visible=True, size=(800, 600), backend="xvfb")
        display.start()
        options = uc.ChromeOptions()
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        #self.browser = uc.Chrome(executable_path="/usr/local/bin/chromedriver",options=options)
        self.browser = uc.Chrome(options=options)
        self.wdw = WebDriverWait(self.browser, 5)
        #we only use this on to interate over rows inside a product page
        self.wdw_ior = WebDriverWait(self.browser, 3)
    def spider_closed(self, spider):
        self.browser.close()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)
    
    def parse(self, response):
        self.browser.get(self.target_page)
        self.scroll_to_the_endpage(1)
        product_details_elements = self.browser.find_elements(By.XPATH, "//div[@data-testid='productArea']//a[@data-component='ProductCardLink']")
        product_details = [urljoin("https://www.farfetch.com", el.get_attribute("href")) for el in product_details_elements]
        product_images_elements = self.browser.find_elements(By.XPATH, "//div[@data-testid='productArea']//div[@data-component='ProductCardImageContainer']/img")
        product_images = [el.get_attribute("src") for el in product_images_elements]
        for link, image in zip(product_details, product_images):
            sneaker_data = self.process_product_details(image=image, url=link)
            if sneaker_data:
                yield sneaker_data

    def process_product_details(self, image, url) -> Optional[Dict[str, str]]:
        self.browser.get(url)
        selector = Selector(text=self.browser.page_source)
        # stock and prices information
        container_sizes = []
        # product name
        product_name = selector.xpath("//span[@data-tstid='cardInfo-description']/text()").get()
        # brand 
        brand = selector.xpath("//a[@data-tstid='cardInfo-title']/span/text()").get()
        if brand:
            brand = brand.strip()
        # product images
        product_images = selector.xpath("//meta[@property='og:image']/@content").getall()
        # description
        description = selector.xpath("//p[@data-tstid='fullDescription']/text()").get()
        # sku
        sku = selector.xpath("//p[@data-tstid='designerStyleId']/span/text()").get()
        if sku:
            if len(sku) == 9:
                sku = sku[:-3]+"-"+sku[-3:]
            else:
                if sku == 'CD7071001A':
                    sku = sku[:9]
                    sku = sku[:-3]+"-"+sku[-3:]
        else:
            self.logger.warning(f"Não foi encontrado SKU: {url}")
            self.browser.refresh()
            selector = Selector(text=self.browser.page_source)
            # product name
            product_name = selector.xpath("//span[@data-tstid='cardInfo-description']/text()").get()
            # brand 
            brand = selector.xpath("//a[@data-tstid='cardInfo-title']/span/text()").get()
            if brand:
                brand = brand.strip()
            product_images = selector.xpath("//meta[@property='og:image']/@content").getall()
            # description
            description = selector.xpath("//p[@data-tstid='fullDescription']/text()").get()
            # sku
            sku = selector.xpath("//p[@data-tstid='designerStyleId']/span/text()").get()
        # out of stock information
        out_of_stock_locator = By.XPATH, "//td[@data-tstid='outOfStockRow']"
        # in stock price
        in_stock_price_locator = By.XPATH, "//td[@data-tstid='addToBagRow']//span[1]"
        #conversion table
        try:
            tabela_locator = By.XPATH, "//button[@data-tstid='sizeGuideButton']"
            tabela_conversao = self.wdw.until(EC.presence_of_element_located(tabela_locator))
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            self.logger.warning(f"Não foi possível coletar: {url}")
            return None
        else:
            try:
                tabela_conversao.click()
            except ElementClickInterceptedException:
                tabela_conversao = self.browser.find_element(By.XPATH, "//button[@data-tstid='sizeGuideButton']")
                self.browser.execute_script("arguments[0].click();", tabela_conversao)
            finally:
                linhas_locator = By.XPATH, "//table[@data-tstid='charttable']/tbody//tr"
                try:
                    _ = self.wdw.until(EC.presence_of_element_located(linhas_locator))
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    self.logger.warning(f"Não foi possível coletar: {url}")
                    return None
                else:                    
                    linhas = self.browser.find_elements(By.XPATH, "//table[@data-tstid='charttable']/tbody//tr")
                    for linha in linhas:
                        size = linha.text.split(" ")[1]
                        if size == '-':
                            continue
                        element_stock_and_sizes = {'size' : "", 'in_stock' : "", "price": "", "currency" : ""}
                        linha.click()
                        sleep(.5)
                        try:
                            self.wdw_ior.until(EC.presence_of_element_located(out_of_stock_locator))
                        except (NoSuchElementException, TimeoutException):
                            try:
                                get_price = self.wdw.until(EC.presence_of_element_located(in_stock_price_locator))
                            except (NoSuchElementException, TimeoutException):
                                element_stock_and_sizes['size'] = size
                                element_stock_and_sizes['price'] = None
                                element_stock_and_sizes['in_stock'] = False
                                element_stock_and_sizes['currency'] = None
                            else:
                                if get_price:
                                    raw_price = Price.fromstring(get_price.text)
                                    element_stock_and_sizes['size'] = size
                                    element_stock_and_sizes['price'] = raw_price.amount_float
                                    element_stock_and_sizes['in_stock'] = True
                                    element_stock_and_sizes['currency'] = raw_price.currency

                                else:
                                    self.logger.debug("Entrei aqui: sem dado de preço 2")
                                    element_stock_and_sizes['size'] = size
                                    element_stock_and_sizes['price'] = None
                                    element_stock_and_sizes['in_stock'] = False
                                    element_stock_and_sizes['currency'] = None
                        else:
                            element_stock_and_sizes['size'] = size
                            element_stock_and_sizes['price'] = None
                            element_stock_and_sizes['in_stock'] = False
                            element_stock_and_sizes['currency'] = None
                        container_sizes.append(element_stock_and_sizes)
                    #close the popup
                    close_popup_locator = By.XPATH, "//button[@data-tstid='btnCloseSizeGuide']"
                    try:
                        close_popup = self.wdw.until(EC.presence_of_element_located(close_popup_locator))
                    except (NoSuchElementException, TimeoutException):
                        self.logger.warning(f"Não foi possível coletar: {url}")
                        return None
                    else:
                        close_popup.click()
        if sku == '555088':
            sku = '555088-118'
        elif sku == 'CD7070':
            sku = 'CD7070-100'
        elif sku == 'CZ6433':
            sku = 'CZ6433-100'
        elif sku == 'AT3375':
            sku = 'AT3375-200'
        elif sku == '554724':
            sku = '554724-125'
        images_uri = []
        if len(product_images) > 0:
            images_uri = [
                f"{self.settings.get('IMAGES_STORE')}{sku}_{filename.split('/')[-1]}"
                for filename in product_images
            ]
        payload = {
                'brand' : brand,
                'product' : product_name,
                'sku' : sku,
                'url' : url,
                'img_search_page' : f"{self.settings.get('IMAGES_STORE')}{sku}_{image.split('/')[-1]}",
                'image_urls' : product_images,
                'image_uris' : images_uri,
                'description' : description,
                'stock_and_prices' : container_sizes,
                'spider' : self.name,
                'spider_version' : self.version
            }
        return FarfetchItem(**payload)
    
    def scroll_to_the_endpage(self, scroll_pause_time):
        screen_height = self.browser.execute_script(
            "return window.screen.height;"
        )  # get the screen height of the web
        screen_height -= 50
        i = 1
        while True:
            # scroll one screen height each time
            self.browser.execute_script(
                "window.scrollTo(0, {screen_height}*{i});".format(
                    screen_height=screen_height, i=i
                )
            )
            i += 1
            sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = self.browser.execute_script(
                "return document.body.scrollHeight;"
            )
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break