import scrapy.contrib.exporter


class CsvItemExporter (scrapy.contrib.exporter.CsvItemExporter):

    def __init__ (self, *args, **kwargs):
        kwargs['fields_to_export'] = [
            'search_title', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
            'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'isbn', 'url']
        super(CsvItemExporter, self).__init__(*args, **kwargs)
