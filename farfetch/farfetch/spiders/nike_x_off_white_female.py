from farfetch.spiders.jordan_male import JordanMaleSpider

class NikeXOffWhiteFemaleSpider(JordanMaleSpider):
    name = 'farfetch-female-nike-x-off-white'
    start_urls = ['https://www.farfetch.com/br/shopping/women/items.aspx']

    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?view=90&scale=276&rootCategory=Women&designer=12264703",
        }[page_number]