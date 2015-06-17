#!/usr/bin/python
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from cirujanos.items import *

class SpiderCirujano(CrawlSpider):

	name = 'cirujanos'
	allowed_domains = ['cirugiaplastica.org.co']
	las_urls = ["http://cirugiaplastica.org.co/listado-de-miembros-de-la-sccp/miembros-de-numero"]
	for i in range(2,36):
		url_temp = 'http://cirugiaplastica.org.co/listado-de-miembros-de-la-sccp/miembros-de-numero/Pagina-%d.html' %i
		las_urls.append(url_temp)
	print las_urls
	#start_urls = ['http://cirugiaplastica.org.co/listado-de-miembros-de-la-sccp/miembros-de-numero']
	start_urls = las_urls
	#rules = [Rule(LinkExtractor(allow=['/listado-de-miembros-de-la-sccp/miembros-de-numero/\S+/view-details.html']),callback='parse_cirujanos',follow=True)]
	rules = [Rule(LinkExtractor(allow=['/listado-de-miembros-de-la-sccp/miembros-de-numero/\S+/view-details.html']),'parse_cirujano')]
	#rules = [Rule(LinkExtractor(allow=['']),'parses_cirujano')]

	def parse_cirujano(self,response):
		cirujano = CirujanoItem()

		nombres = response.xpath("//div[@id='field_37']/div[@class='output']/text()").extract()
		nombres = nombres[0].title().strip()
		cirujano['nombres'] = nombres

		apellidos = response.xpath("//div[@id='field_29']/div[@class='output']/text()").extract()
		apellidos = apellidos[0].title().strip()
		cirujano['apellidos'] = apellidos

		#email processing
		email = response.xpath("//div[@id='field_11']/div[@class='output']").extract()[0]
		mi_str = "%"+"2e"+"%"+"63"
		direccion = (email.split("%",1)[1]).split(mi_str)
		solo_correo = direccion[0]
		solo_extension = direccion[1].split('"')[0]

		arreglo_correo = solo_correo.split("%")
		string_total = ""
		for letter in arreglo_correo:
			string_total = string_total + letter
		solo_correo_dec = string_total.decode("hex")

		arreglo_extension = solo_extension.split("%")
		string_total = ""
		for letter in arreglo_extension:
			string_total = string_total + letter
		solo_extension_dec = string_total.decode("hex")

		correo_final = solo_correo_dec + ".c" + solo_extension_dec
		cirujano['email'] = correo_final

		direccion = response.xpath("//div[@id='field_4']/div[@class='output']/text()").extract()
		direccion = direccion[0].title().strip()
		cirujano['direccion'] = direccion

		ciudad = response.xpath("//div[@id='field_5']/div[@class='output']/a/text()").extract()
		ciudad = ciudad[0].title().strip()
		cirujano['ciudad'] = ciudad

		estado = response.xpath("//div[@id='field_6']/div[@class='output']/a/text()").extract()
		estado = estado[0].title().strip()
		cirujano['estado'] = estado

		pais = response.xpath("//div[@id='field_7']/div[@class='output']/a/text()").extract()
		pais = pais[0].title().strip()
		cirujano['pais'] = pais

		cirujano['telefono'] = response.xpath("//div[@id='field_9']/div[@class='output']/text()").extract()
		return cirujano
