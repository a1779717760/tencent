# -*- coding: utf-8 -*-
import scrapy


class HrSpider(scrapy.Spider):
    name = 'hr'
    #allowed_domains = ['https://hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")
        for tr in tr_list:
            item={}
            item['title'] = tr.xpath("./td[1]/a/text()").extract_first()
            item['position'] = tr.xpath("./td[2]/text()").extract_first()
            item['number'] = tr.xpath("./td[3]/text()").extract_first()
            item['location'] = tr.xpath("./td[4]/text()").extract_first()
            item['time'] = tr.xpath("./td[5]/text()").extract_first()
            yield item
        next_url = response.xpath("//a[@id='next']/@href").extract_first()

        if next_url != "javascript:;":
            next_url = "https://hr.tencent.com/" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
