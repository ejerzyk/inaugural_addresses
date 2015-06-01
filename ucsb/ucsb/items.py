import scrapy

class UcsbItem(scrapy.Item):
	year = scrapy.Field()
	text = scrapy.Field()