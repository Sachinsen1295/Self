
    # set the Splash local server endpoint
SPLASH_URL = "http://localhost:8050"
    
    # enable the Splash downloader middleware and 
    # give it a higher priority than HttpCompressionMiddleware
DOWNLOADER_MIDDLEWARES = {
        "scrapy_splash.SplashCookiesMiddleware": 723,
        "scrapy_splash.SplashMiddleware": 725,
        "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
    }
    
    # enable the Splash deduplication argument filter to
    # make Scrapy Splash saves spice disk on cached requests
SPIDER_MIDDLEWARES = {
        "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
    }
    
    # set the Splash deduplication class
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'