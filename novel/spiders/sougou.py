# -*- coding: utf-8 -*-
import scrapy
from novel.items import NovelItem
from scrapy.http import Request


class SogouSpider(scrapy.Spider):
    name = "sogou"
    allowed_domains = ["sogou.com"]

    start_urls = ['http://xiaoshuo.sogou.com/c0/0_1_0_0/']

    def parse(self, response):
        item = NovelItem()
        li=response.xpath("//div[@class='fic_graphic_list mb15']/ul[@class='cf']/li")
        #li是个<li>的列表，每个<li>里含一条信息
        for each in li:
            tx = each.xpath('div[@class="fgl_lp_info"]')
            item['title'] = tx.xpath('h4/a/text()').extract()
            item['img'] = each.xpath('div[@class="fgl_lp_pic"]/a/img/@src').extract()
            item['author'] = tx.xpath('p[@class="tx"]/a/text()').extract()
            item['uptx'] = tx.xpath('p[@class="tx uptx"]/a/text()').extract()
            yield item
        # 获取下一页的url
        urls = response.xpath('//div[@class="pagination cf"]/a[@class="next"]/@href').extract()

        if urls:
            url = 'http://xiaoshuo.sogou.com' + urls[0]
            print('=' * 30, url)
            yield Request(url, callback=self.parse)#这是重点，将新获取的request返回给引擎，实现继续循环
