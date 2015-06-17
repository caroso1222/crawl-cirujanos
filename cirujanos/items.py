# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CirujanoItem(scrapy.Item):
    nombres = scrapy.Field()
    apellidos = scrapy.Field()
    email = scrapy.Field()
    direccion = scrapy.Field()
    ciudad = scrapy.Field()
    estado = scrapy.Field()
    pais = scrapy.Field()
    telefono = scrapy.Field()
