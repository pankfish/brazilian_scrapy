import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['xbzbrindes.com.br']
    start_urls = [
        'https://www.xbzbrindes.com.br/lancamentos',
        'https://www.xbzbrindes.com.br/brindes',
        'https://www.xbzbrindes.com.br/ponta-de-estoque'
    ]

    def parse(self, response):
        product_links = response.xpath("//div[@class='thumbnail prod']/div/a/@href").getall()
        for link in product_links:
            yield scrapy.Request(
                url=link,
                callback=self.process_link
            )

    def process_link(self, response):
        product_link = response.url
        title = response.xpath('//p[@class= "produto-nome"]/text()').get()
        ref = response.xpath('//h1[@id="item_referencia"]/text()').get()
        description = response.xpath("//span[@class='desc-sub my-desc-sub']/text()").get()
        yield{
            'url': product_link,
            'name': title,
            'ref #': ref,
            'description': description 
        }