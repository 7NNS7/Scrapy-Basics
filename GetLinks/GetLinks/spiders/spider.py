# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['attack.mitre.org']
    start_urls = ['http://attack.mitre.org/']

    def parse(self, response):
        links = response.xpath('//div[@class="ml-5 pr-5 pt-3"]//a')
        with open("Links.txt","w") as f:
            for link in links:
                new_link = link.xpath('./@href').extract_first()
                new_link_url = self.start_urls[0]+str(new_link)
                f.write(self.start_urls[0]+str(new_link)+"\n")
                #print(self.start_urls[0]+str(new_link)+"\n")
                yield scrapy.Request(new_link_url, callback=self.parse_url)


    def parse_url(self,response):
        print(response.status)
