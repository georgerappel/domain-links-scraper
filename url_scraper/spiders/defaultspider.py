# -*- coding: utf-8 -*-
# Adapted from https://www.data-blogger.com/2016/08/18/scraping-a-website-with-python-scrapy/

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from url_scraper.items import LinkScraperItem

class DefaultspiderSpider(scrapy.Spider):
    name = 'defaultspider'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    custom_settings = {
        'DNS_TIMEOUT': 6,
        'DOWNLOAD_TIMEOUT': 6
    }

    # This spider has one rule: extract all (unique and canonicalized)
    # links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            print('Start url ' + url)
            yield scrapy.Request(url, callback=self.parse_items, dont_filter=False)


    # Method for parsing items
    def parse_items(self, response):
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)

        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True

            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = LinkScraperItem()
                item['url_from'] = response.url
                item['url_to'] = link.url

                if link.url not in self.start_urls:
                    print("not in ")
                    self.start_urls.append(link.url)

                yield scrapy.Request(link.url, callback=self.parse_items)
                yield item


    def call_next(self, url):
        yield scrapy.Request(url, callback=self.parse_items)
