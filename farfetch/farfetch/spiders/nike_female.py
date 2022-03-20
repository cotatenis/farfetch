from farfetch.spiders.jordan_male import JordanMaleSpider

class NikeFemaleSpider(JordanMaleSpider):
    name = 'farfetch-female-nike'
    start_urls = ['https://www.farfetch.com/br/shopping/women/items.aspx']

    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?view=90&scale=276&rootCategory=Women&designer=1664",
            '2' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=2&view=90&scale=276&rootCategory=Women&designer=1664",
            "3" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=3&view=90&scale=276&rootCategory=Women&designer=1664",
            "4" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=4&view=90&scale=276&rootCategory=Women&designer=1664",
            "5" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=5&view=90&scale=276&rootCategory=Women&designer=1664",
            "6" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=6&view=90&scale=276&rootCategory=Women&designer=1664",
            "7" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=7&view=90&scale=276&rootCategory=Women&designer=1664",
            "8" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=8&view=90&scale=276&rootCategory=Women&designer=1664",
            "9" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=9&view=90&scale=276&rootCategory=Women&designer=1664",
            "10" : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=10&view=90&scale=276&rootCategory=Women&designer=1664",
        }[page_number]