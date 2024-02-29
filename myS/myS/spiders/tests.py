import scrapy
from myS.items import MysItem
import json

class TestsSpider(scrapy.Spider):
    name = "tests"
    allowed_domains = ["www.luogu.com.cn"]
    start_urls = ["https://www.luogu.com.cn/training/3858#problems"]

    def parse(self, response):
        xml = "/html/body/div/div/article//li"
        body = response.xpath(xml)
        numbers = body.xpath("//a/@href")
        names = body.xpath("//a/text()")

        for i in range(len(numbers)):
            item = MysItem()
            item["number"] = numbers[i].extract()
            item["name"] = names[i].extract()
            yield item