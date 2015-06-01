import scrapy 
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ucsb.items import UcsbItem
import re

class UcsbSpider(CrawlSpider):
	name = "ucsb"
	allowed_domains = ["presidency.ucsb.edu"]
	start_urls = ["http://www.presidency.ucsb.edu/inaugurals.php"]
	rules = [Rule(LinkExtractor(allow=()), 'parse_ucsb')]
	# rules = [Rule(LinkExtractor(allow=['/ws/index.php?pid=\d+']), 'parse')]

	def parse_ucsb(self, response):
		i = UcsbItem()
		i['year'] = response.xpath("//span[@class='docdate']/text()").extract()
		i['text'] = " ".join(response.xpath("//span[@class='displaytext']/i/text()").extract() + response.xpath("//span[@class='displaytext']/p/text()").extract()).replace(u'\u2014', ' ')
		if i['year'] != '' and i['text'] != '':
			yield i