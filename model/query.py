# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:42:49 2016

@author: Hong
"""

import lib.formatters as formatters
from collections import OrderedDict
from lib.adapters import adapter_factory


class DataRequest(object):
    
    def __init__(self, query_definition, output_format=None):
        self._query_definition = query_definition
        self._output_format = output_format or 'html'
    
    def data(self):
        return self._query_definition.data()

    def to_file(self, dir_path, filename_without_ext):
        formatter = formatters.formatter_factory(output_format=self._output_format)
        data = self.data()
        file_path = '%s%s.%s'%(dir_path, filename_without_ext, self._output_format)
        formatter.to_file(file_path=file_path, data=data, time_series=self._query_definition._time_series)
        return (data, file_path)

    def to_html(self, file_path):
        formatter = formatters.formatter_factory(output_format='html')
        data = self.data()
        formatter.to_file(file_path=file_path, data=data, time_series=self._query_definition._time_series)
        return data

    def to_pdf(self, file_path):
        formatter = formatters.formatter_factory(output_format='pdf')
        data = self.data()
        formatter.to_file(file_path=file_path, data=data, time_series=self._query_definition._time_series)
        return data


class QueryDefinition(object):
    
    def __init__(self):
        self._time_series = OrderedDict()
        
    def add_time_series(self, time_series_id, time_series):
        self._time_series[time_series_id] = time_series
        
    def data(self):
        data = OrderedDict()
        for time_series_id, time_series in self._time_series.items():
            data[time_series_id] = time_series.data()
        return data


class TimeSeries(object):
    
    def __init__(self, database, data_id, data_source, from_date=None, to_date=None, fillna=None, title=None):
        self._params = {
            'database':database,
            'data_id':data_id,
            'data_source':data_source,
            'from_date':from_date,
            'to_date':to_date,
            'fillna':fillna,
            'title':title
            }
        self._operations = []
            
    def params(self):
        return self._params
        
    def add_operation(self, operation, operation_arg):
        self._operations.append((operation, operation_arg))

    def title(self):
        return self._params['title']
        
    def set_title(self, title):
        self._params['title'] = title

    def data(self):
        return adapter_factory(data_source=self._params['data_source']).data(query_params=self._params)