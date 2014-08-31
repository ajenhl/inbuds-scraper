# -*- coding: utf-8 -*-

# Scrapy settings for inbuds project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'inbuds'

SPIDER_MODULES = ['inbuds.spiders']
NEWSPIDER_MODULE = 'inbuds.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'INBUDS Crawler'

FEED_URI = 'file:///home/jamie/code/inbuds/export.csv'
FEED_EXPORTERS = {'my_csv': 'inbuds.exporter.CsvItemExporter'}
FEED_FORMAT = 'my_csv'

#LOG_LEVEL = 'INFO'
