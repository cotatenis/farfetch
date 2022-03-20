from farfetch.spiders.jordan_male import JordanMaleSpider

class JordanFemaleSpider(JordanMaleSpider):
    name = 'farfetch-female-jordan'
    start_urls = ['https://www.farfetch.com/br/shopping/women/items.aspx']

    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?view=90&scale=276&rootCategory=Women&designer=6687111",
            '2' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=2&view=90&scale=276&rootCategory=Women&designer=6687111",
            '3' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=3&view=90&scale=276&rootCategory=Women&designer=6687111",
            '4' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=4&view=90&scale=276&rootCategory=Women&designer=6687111",
        }[page_number]