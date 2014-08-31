INBUDS Scraper
==============

This is a simple scraper to extract bibliographic references from
`INBUDS`_.

It uses `Scrapy`_ (known to work with 0.24.2).


Usage
-----

Create a file `search_titles.txt` in the directory containing this
file, populating it with titles to search on, one per line. This file
must be encoded in UTF-8.

Then run `scrapy crawl INBUDS`. The output will be in the file
`export.csv`. The first line contains the column names. Unfortunately
these are not helpful, and should be replaced with::

    search_title,名前,タイトル,タイトル読み,サブタイトル,タイトル(欧文),サブタイトル(欧文),該当ページ,媒体名,通号,編者,発行日,発行者,発行地,本文,isbn,url


.. _INBUDS: http://bauddha.dhii.jp/INBUDS/search.php
.. _Scrapy: https://pypi.python.org/pypi/Scrapy
