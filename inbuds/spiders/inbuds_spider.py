# -*- coding: utf-8 -*-

import os.path
import urlparse

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from ..items import InbudsItem


class InbudsSpider (CrawlSpider):

    name = 'INBUDS'
    allowed_domains = ['bauddha.dhii.jp']
    download_delay = 0.5

    rules = (
        Rule(LinkExtractor(allow=('search\.php\?m=trdd',)),
             callback='parse_item'),
    )

    def parse_item (self, response):
        self.log('Parsing response from %s as item' % response.url)
        item = InbudsItem()
        qs = urlparse.parse_qs(urlparse.urlsplit(
            response.request.headers['Referer'])[3])
        item['search_title'] = qs['uekey'][0]
        item['url'] = response.url
        for field, name in item.field_data.items():
            xpath = "//td[normalize-space(preceding-sibling::td)='%s']/text()" \
                    % name
            data = response.xpath(xpath).extract()
            if data:
                item[field] = '; '.join([piece.strip() for piece in data])
        return item

    def start_requests (self):
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        titles_path = os.path.join(base_path, 'search_titles.txt')
        for url in open(titles_path, 'rU').readlines():
            full_url = u'http://bauddha.dhii.jp/INBUDS/search.php?m=sch&a=&uekey=%s&ekey1=&lim=2000' % url.strip().decode('utf-8')
            yield self.make_requests_from_url(full_url)
