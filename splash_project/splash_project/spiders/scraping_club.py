from typing import Iterable
import scrapy
from scrapy_splash import SplashRequest

lua_script = """
    function main(splash, args)  
      splash:go(args.url)
    
      -- custom rendering script logic...
      
      return splash:html()
    end
    """

class ScrapingClubSpider(scrapy.Spider):
    name = "scraping_club"
    allowed_domains = ["scrapingclub.com"]
    #start_urls = ["https://scrapingclub.com/exercise/list_infinite_scroll/"]
    
    def start_requests(self):
            url = "https://scrapingclub.com/exercise/list_infinite_scroll/"
            yield SplashRequest(url, callback=self.parse, endpoint="execute", args={"lua_source": lua_script})

    def parse(self, response):
        # iterate over the product elements
        for product in response.css(".post"):
            url = product.css("a").attrib["href"]
            image = product.css(".card-img-top").attrib["src"]
            name = product.css("h4 a::text").get()
            price = product.css("h5::text").get()
        
                # add scraped product data to the list
                # of scraped items
        
            yield {
                "url": url,
                "image": image,
                "name": name,
                "price": price
            }
