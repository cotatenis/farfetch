from farfetch.spiders.jordan_male import JordanMaleSpider

class NikeXOffWhiteMaleSpider(JordanMaleSpider):
    name = 'farfetch-male-nike-x-off-white'
    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?view=90&scale=285&rootCategory=Men&designer=12264703",

        }[page_number]