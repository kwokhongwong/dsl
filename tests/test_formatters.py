# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:57:29 2016

@author: Hong
"""

import os
import unittest
import lib.formatters as formatters
from model.query import TimeSeries
from constants import Operation


class TestFormatterFactory(unittest.TestCase):
            
    def test_format_factory(self):

        formatters.formatter_factory(output_format='html')
        # assert type(formatter) is formatters.HTMLFormatter
        
        formatters.formatter_factory(output_format='pdf')
        # assert type(formatter) is formatters.PDFFormatter

        exception_raised = False
        try:
            formatters.formatter_factory(output_format='plotly')
        except NotImplementedError:
            exception_raised = True
        self.assertTrue(exception_raised, 'NotImplementedError raised')


class TestHTMLFormatter(unittest.TestCase):
    
    def setUp(self):
        self._formatter = formatters.formatter_factory(output_format='html')
        time_series = TimeSeries(database='FRED', data_id='GDPMC1', data_source='quandl', title='TestHTMLFormatter')
        time_series.add_operation(operation=Operation.table, operation_arg=None)
        self._dataframe = {'GDPMC1':time_series.data()}
        self._time_series = {'GDPMC1':time_series}

    def test_formatter(self):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp', 'TestHTMLFormatter.html')
        self._formatter.to_file(file_path=file_path, data=self._dataframe, time_series=self._time_series)
        print('HTML file saved to %s'%file_path)


class TestPDFFormatter(unittest.TestCase):
    
    def setUp(self):
        self._formatter = formatters.formatter_factory(output_format='pdf')
        time_series = TimeSeries(database='FRED', data_id='GDPMC1', data_source='quandl', title='TestPDFFormatter')
        time_series.add_operation(operation=Operation.graph, operation_arg=None)
        self._dataframe = {'GDPMC1':time_series.data()}
        self._time_series = {'GDPMC1':time_series}

    def test_formatter(self):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp', 'TestPDFFormatter.pdf')
        self._formatter.to_file(file_path=file_path, data=self._dataframe, time_series=self._time_series)
        print('PDF file saved to %s'%file_path)


if __name__ == '__main__':
    unittest.main()