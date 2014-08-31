# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InbudsItem (scrapy.Item):

    field_data = {
        'f1': u'名前',
        'f2': u'タイトル',
        'f3': u'タイトル読み',
        'f4': u'サブタイトル',
        'f5': u'タイトル(欧文)',
        'f6': u'サブタイトル(欧文)',
        'f7': u'該当ページ',
        'f8': u'媒体名',
        'f9': u'通号',
        'f10': u'編者',
        'f11': u'発行日',
        'f12': u'発行者',
        'f13': u'発行地',
        'f14': u'本文',
        'isbn': u'ISBN',
    }
    search_title = scrapy.Field()
    f1 = scrapy.Field()
    f2 = scrapy.Field()
    f3 = scrapy.Field()
    f4 = scrapy.Field()
    f5 = scrapy.Field()
    f6 = scrapy.Field()
    f7 = scrapy.Field()
    f8 = scrapy.Field()
    f9 = scrapy.Field()
    f10 = scrapy.Field()
    f11 = scrapy.Field()
    f12 = scrapy.Field()
    f13 = scrapy.Field()
    f14 = scrapy.Field()
    isbn = scrapy.Field()
    url = scrapy.Field()
