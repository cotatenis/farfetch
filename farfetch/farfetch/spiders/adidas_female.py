from farfetch.spiders.jordan_male import JordanMaleSpider

class AdidasFemaleSpider(JordanMaleSpider):
    name = 'farfetch-female-adidas'
    start_urls = ['https://www.farfetch.com/br/shopping/women/items.aspx']

    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?view=90&scale=276&rootCategory=Women&designer=214504",
            '2' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=2&view=90&scale=276&rootCategory=Women&designer=214504",
            '3' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=3&view=90&scale=276&rootCategory=Women&designer=214504",
            '4' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=4&view=90&scale=276&rootCategory=Women&designer=214504",
            '5' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=5&view=90&scale=276&rootCategory=Women&designer=214504"
        }[page_number]