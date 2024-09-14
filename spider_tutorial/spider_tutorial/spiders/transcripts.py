import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies"]

    rules = (Rule(LinkExtractor(restrict_xpaths = ("//ul[@class='scripts-list']/li/a")), callback="parse_item", follow=True),)
#for immideate child you can you ./
    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")
        yield {
            "title": article.xpath("//article[@class='main-article']/h1/text()").get(),
            "plot": article.xpath("./p/text()").get(),
            "transcripts": article.xpath("//article[@class='main-article']/div[@class = 'full-script']/text()").getall(),
            "url": response.url,

        }