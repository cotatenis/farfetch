from farfetch.spiders.jordan_male import JordanMaleSpider

class NikeMaleSpider(JordanMaleSpider):
    name = 'farfetch-male-nike'
    def __init__(self, page_number, **kwargs):
        super().__init__(page_number=page_number, **kwargs)
        self.target_page = {
            '1' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?view=90&scale=285&rootCategory=Men&designer=1664",
            '2' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=2&view=90&scale=285&rootCategory=Men&designer=1664",
            '3' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=3&view=90&scale=285&rootCategory=Men&designer=1664",
            '4' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=4&view=90&scale=285&rootCategory=Men&designer=1664",  
            '5' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=5&view=90&scale=285&rootCategory=Men&designer=1664", 
            '6' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=6&view=90&scale=285&rootCategory=Men&designer=1664", 
            '7' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=7&view=90&scale=285&rootCategory=Men&designer=1664", 
            '8' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=8&view=90&scale=285&rootCategory=Men&designer=1664", 
            '9' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=9&view=90&scale=285&rootCategory=Men&designer=1664", 
            '10' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=10&view=90&scale=285&rootCategory=Men&designer=1664", 
            '11' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=11&view=90&scale=285&rootCategory=Men&designer=1664", 
            '12' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=12&view=90&scale=285&rootCategory=Men&designer=1664", 
            '13' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=13&view=90&scale=285&rootCategory=Men&designer=1664", 
            '14' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=14&view=90&scale=285&rootCategory=Men&designer=1664",
            '15' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=15&view=90&scale=285&rootCategory=Men&designer=1664",
            '16' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=16&view=90&scale=285&rootCategory=Men&designer=1664",
            '17' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=17&view=90&scale=285&rootCategory=Men&designer=1664",
            '18' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=18&view=90&scale=285&rootCategory=Men&designer=1664",
            '19' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=19&view=90&scale=285&rootCategory=Men&designer=1664",
            '20' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=20&view=90&scale=285&rootCategory=Men&designer=1664",
            '21' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=21&view=90&scale=285&rootCategory=Men&designer=1664",
            '22' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=22&view=90&scale=285&rootCategory=Men&designer=1664",
            '23' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=23&view=90&scale=285&rootCategory=Men&designer=1664",
            '24' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=24&view=90&scale=285&rootCategory=Men&designer=1664",
            '25' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=25&view=90&scale=285&rootCategory=Men&designer=1664",
            '26' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=26&view=90&scale=285&rootCategory=Men&designer=1664",
            '27' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=27&view=90&scale=285&rootCategory=Men&designer=1664",
            '28' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=28&view=90&scale=285&rootCategory=Men&designer=1664",
            '29' : "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=29&view=90&scale=285&rootCategory=Men&designer=1664",

        }[page_number]