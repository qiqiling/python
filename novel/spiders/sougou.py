# -*- coding: utf-8 -*-
import scrapy
from novel.items import NovelItem


class SougouSpider(scrapy.Spider):
    name = "sougou"
    allowed_domains = ["sougou.com"]
    start_urls = ['http://xiaoshuo.sogou.com/c0/0_1_0_%s/'%i for i in range(5)]
    # for i in range(5)

    def parse(self, response):
        item = NovelItem()
        for each in response.xpath("//div[@class='fic_graphic_list mb15']/ul[@class='cf']/li"):
            tx=each.xpath('div[@class="fgl_lp_info"]')
            item['title'] = tx.xpath('h4/a/text()').extract()
            item['img']=each.xpath('div[@class="fgl_lp_pic"]/a/img/@src').extract()
            item['author']=tx.xpath('p[@class="tx"]/a/text()').extract()
            item['uptx'] = tx.xpath('p[@class="tx uptx"]/a/text()').extract()
            yield item

