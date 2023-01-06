import scrapy
from firstproject.items import FirstprojectItem
from scrapy.loader import ItemLoader

class books(scrapy.Spider):
    name="books"
    start_urls=[
        'https://books.toscrape.com/'
        ]
        
    def parse(self,response):
        for link in response.css("ul.nav.nav-list ul li a::attr('href')"):
            yield response.follow(link.get(),callback=self.parse_categories)

    
    def parse_categories(self,response):
        category=FirstprojectItem()
        for categories in response.css("li.col-xs-6.col-sm-4.col-md-3.col-lg-3 article.product_pod"):
            category['image'] = "https://books.toscrape.com/" + categories.css("div.image_container img::attr('src')").get()
            category['title_name'] = categories.css("h3 a::text").get()
            category['price'] = categories.css("div.product_price p.price_color::text").get().replace('£','')
            category['link'] = "https://books.toscrape.com/"+ categories.css("h3 a::attr('href')").get()
            yield category
        #    #item['category_name']=categories.css("ul.nav.nav-list ul li a::text").get()
        #    item['title_name']=categories.css("h3 a::text").get()
        next_page=response.css("ul.pager li.next a::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse_categories)










        
    #def parse(self,response):
    #    item=FirstprojectItem()
    #    for links in response.css("ul.nav.nav-list ul "):
    #        item['link'] = links.css("li a::attr('href')").get()
    #        yield response.follow( item['link'],callback=self.parse_categories)

    #def parse_categories(self,response):
    #    item=FirstprojectItem()
    #    for categories in response.css("li.col-xs-6.col-sm-4.col-md-3.col-lg-3 article.product_pod"):
    #        item['image'] = "https://books.toscrape.com/" + categories.css("div.image_container img::attr('src')").get()
    #        #item['category_name']=categories.css("ul.nav.nav-list ul li a::text").get()
    #        item['title_name']=categories.css("h3 a::text").get()
    #        yield item

    #def parse_categories(self,response):
    #    item=FirstprojectItem()
    #    for categories in response.css("div.row"):
    #        item['category_name']=categories.css("aside.sidebar.col-sm-4.col-md-3 div.side_categories ul.nav.nav-list ul li a::text").get()
    #        item['image']=categories.css("ol.row li.col-xs-6.col-sm-4.col-md-3.col-lg-3 div.image_container a::attr('href')").get()
    #        yield item

    #def parse(self, response):
    #    for items in response.css("li.col-xs-6.col-sm-4.col-md-3.col-lg-3 article.product_pod"):
    #        item=FirstprojectItem()
    #        item['price'] = items.css('div.product_price p.price_color::text').get().replace('£','')
    #        item['image'] ="https://books.toscrape.com/" + items.css('div.image_container a img::attr("src")').get()
    #        item['link'] = "https://books.toscrape.com/" + items.css('a::attr("href")').get()

    #        yield item

        # next_page=response.css("ul.pager li.next a::attr('href')").get()
    #    if next_page is not None:
    #        yield response.follow(next_page,callback=self.parse)
