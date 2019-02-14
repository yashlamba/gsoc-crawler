# -*- coding: utf-8 -*-
import scrapy

class GsocSpider(scrapy.Spider):
    name = 'GSOC'
    allowed_domains = ['summerofcode.withgoogle.com/archive/2018/organizations/']
    start_urls = ['https://summerofcode.withgoogle.com/archive/2018/organizations/']
    
    def parse(self, response):
        org_links = response.css('a.organization-card__link::attr(href)').extract()
        for org in org_links:
            link = response.urljoin(org)
            yield scrapy.Request(url = link, callback = self.parseorg, dont_filter = True)

    def parseorg(self, response):
        yield {
            'name': response.css('h3.banner__title::text').extract_first(),
            'website': response.css('a.org__link::attr(href)').extract_first(),
            'Idea_List': response.css('main > section > div > div > div > md-card > div > div > md-button::attr(href)').extract()[0]
        }

