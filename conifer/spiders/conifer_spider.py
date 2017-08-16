import scrapy
from conifer.items import ConiferItem


class ConfierSpider(scrapy.Spider):

    name = 'conifer'
    start_urls = ['http://www.greatplantpicks.org/plantlists/by_plant_type/conifer',]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + ".html"
    #     with open(filename,'wb') as f:
    #         f.write(response.body)
    #
    def parse(self, response):
        for cel in response.xpath("//tbody/tr"):
            item = ConiferItem()
            # item['name'] = cel.xpath('//td[@class="plantname"]/a/span[@class="genus"]/text()').extract()
            item['name'] = cel.xpath('//td[@class="common-name"]/a/text()').extract()
            item['genus'] = cel.xpath('//td[@class="plantname"]/a/span[@class="genus"]/text()').extract()
            item['species'] = cel.xpath('//td[@class="plantname"]/a/span[@class="species"]/text()').extract()
            yield item
