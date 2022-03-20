from farfetch.spiders.jordan_male import JordanMaleSpider

class AdidasMaleSpider(JordanMaleSpider):
    name = 'farfetch-male-adidas'
    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?view=90&scale=285&rootCategory=Men&designer=214504",
            '2' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=2&view=90&scale=285&rootCategory=Men&designer=214504",
            '3' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=3&view=90&scale=285&rootCategory=Men&designer=214504",
            '4' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=4&view=90&scale=285&rootCategory=Men&designer=214504",
            '5' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=5&view=90&scale=285&rootCategory=Men&designer=214504",
            '6' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=6&view=90&scale=285&rootCategory=Men&designer=214504",
            '7' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=7&view=90&scale=285&rootCategory=Men&designer=214504",
            '8' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=8&view=90&scale=285&rootCategory=Men&designer=214504",
            '9' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=9&view=90&scale=285&rootCategory=Men&designer=214504",
            '10' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=10&view=90&scale=285&rootCategory=Men&designer=214504",
            '11' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=11&view=90&scale=285&rootCategory=Men&designer=214504",
            '12' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=12&view=90&scale=285&rootCategory=Men&designer=214504",
            '13' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=13&view=90&scale=285&rootCategory=Men&designer=214504",
            '14' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=14&view=90&scale=285&rootCategory=Men&designer=214504",

        }[page_number]