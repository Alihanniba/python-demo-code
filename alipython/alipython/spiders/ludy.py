#!/usr/bin/env python


import scrapy

class ludy(scrapy.Spider):
	name = 'alihanniba'
	allowed_domains = ['alihanniba']
	start_urls = [
		'http://www.ludy520.com'
	]

	def parse(self, response):
		self.log('A response from %s just arrived!' % response.url)
