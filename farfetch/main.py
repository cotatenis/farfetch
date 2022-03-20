from scrapy.utils.project import get_project_settings
import os
from scrapy.crawler import CrawlerRunner
from farfetch.spiders import (
    JordanMaleSpider,
    JordanFemaleSpider,
    YeezyFemaleSpider,
    YeezyMaleSpider,
    AdidasStellaFemaleSpider,
    AdidasStellaMaleSpider,
    AdidasFemaleSpider,
    AdidasMaleSpider,
    NikeXOffWhiteFemaleSpider,
    NikeFemaleSpider,
    AdidasPWMaleSpider,
    NikeMaleSpider,
    NikeXOffWhiteMaleSpider
)
from scrapy.utils.log import configure_logging
from config import settings
from typer import Typer
from twisted.internet import reactor
import os

app = Typer()

@app.command()
def start_crawl(brand: str = "", page_number: str = ""):
    if brand not in settings.get("store.brands"):
        raise ValueError(f"{brand} is not a valid store.")
    spider = {
        'farfetch-male-jordan' : JordanMaleSpider,
        'farfetch-female-jordan' : JordanFemaleSpider,
        'farfetch-female-yeezy' : YeezyFemaleSpider,
        'farfetch-male-yeezy' : YeezyMaleSpider,
        'farfetch-female-stella' : AdidasStellaFemaleSpider,
        'farfetch-male-stella' : AdidasStellaMaleSpider,
        'farfetch-female-adidas' : AdidasFemaleSpider,
        'farfetch-male-adidas' : AdidasMaleSpider,
        'farfetch-female-nike-x-off-white' : NikeXOffWhiteFemaleSpider,
        'farfetch-male-nike-x-off-white' : NikeXOffWhiteMaleSpider,
        'farfetch-female-nike' : NikeFemaleSpider,
        'farfetch-male-adidas-pw' : AdidasPWMaleSpider,
        'farfetch-male-nike' : NikeMaleSpider,
    }
    crawl_settings = get_project_settings()
    settings_module_path = os.environ.get("SCRAPY_ENV", "farfetch.settings")
    crawl_settings.setmodule(settings_module_path)
    configure_logging(crawl_settings)
    runner = CrawlerRunner(crawl_settings)
    d = runner.crawl(spider[brand], page_number=page_number)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() 


if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings.get("store.GOOGLE_APPLICATION_CREDENTIALS", "./credentials/credentials.json")
    app()
