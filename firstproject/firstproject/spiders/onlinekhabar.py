import scrapy

class onlineKhabar(scrapy.Spider):
    name='onlinekhabar'
    start_urls=['https://www.onlinekhabar.com/']

    def parse(self,response):
        for items in response.css("div#page"):
            yield{
                'link':items.css("a::attr('href')").getall(),
                #'hi':items.css("img::attr('alt')").getall()
            }