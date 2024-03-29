from typing import Any
import scrapy
from scrapy.http import Response
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name= 'quotes'
    start_urls = [
        'https://quotes.toscrape.com'
    ]

    def parse(self, response):

        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').get()
            author = quotes.css('.author::text').get()
            tag = quotes.css('.tag::text').getall()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items
        
            next_page = response.css('.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)      
