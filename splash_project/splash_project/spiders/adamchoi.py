from typing import Iterable
import scrapy
from scrapy_splash import SplashRequest
from scrapy.utils.request import fingerprint

class AdamchoiSpider(scrapy.Spider):
    name = "adamchoi"
    allowed_domains = ["www.adamchoi.co.uk"]
    
    # Define the Lua script for Splash
    # script = """
    # function main(splash, args)
    #     splash.private_mode_enabled = false
    #     assert(splash:go(args.url))
    #     assert(splash:wait(3))
    #     all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
    #     if #all_matches > 1 then
    #         all_matches[2]:mouse_click()
    #         assert(splash:wait(3))
    #     end
    #     splash:set_viewport_full()
    #     return splash:html()
    # end
    #"""
    
    script = """
      function main(splash, args)
        -- Disable private mode if the website doesn't render correctly
        splash.private_mode_enabled = false
        -- Go to the URL set on the splash browser and wait for 3 seconds to let the page render
        assert(splash:go(args.url))
        assert(splash:wait(3))
        -- Select all elements with the CSS selector "label.btn.btn-sm.btn-primary"
        all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
        -- Click on the second button and wait for 3 seconds to let the page render
        all_matches[2]:mouse_click()
        assert(splash:wait(3))
        -- Set the viewport to full size to make all content visible
        splash:set_viewport_full()
        return {splash:png(), splash:html()}
    end
    """

    def start_requests(self):
        url = "https://www.adamchoi.co.uk/overs/detailed"
        yield SplashRequest(
            url=url,
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source": self.script,
                "wait": 3  # Additional wait time if needed
            },
            headers={"User-Agent": "Mozilla/5.0"},
            dont_filter=True  # Ensure that the request is not filtered by Scrapy's rules
        )

    def parse(self, response):
        print(response.body)

    
        # Process the response here
