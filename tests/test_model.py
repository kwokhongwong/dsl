# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:07:27 2016

@author: Hong
"""

import unittest
from lib.adapters import adapter_factory
from model.query import QueryDefinition, TimeSeries, DataRequest


class TestAdapters(unittest.TestCase):
    
    def setUp(self):
        self._params = {'database':'FRED', 'data_id':'GDPMC1'}
        self._adapter = adapter_factory(data_source='quandl')
        
    def test_quandl_adapter(self):
        # Test Quandl data query adapter
        assert len(self._adapter.data(query_params=self._params)) > 0
        
        exception_raised = False
        try:
            adapter_factory(data_source='bloomberg')
        except NotImplementedError:
            exception_raised = True
        self.assertTrue(exception_raised, 'NotImplementedError raised')


class TestTimeSeries(unittest.TestCase):
    
    def setUp(self):
        self._time_series = TimeSeries(database='FRED', data_id='GDPMC1', data_source='quandl')
        
    def test_time_series_data(self):
        # Test data query from time series object using the Quandl adapter
        assert len(self._time_series.data()) > 0


class TestQueryDefinitions(unittest.TestCase):
    
    def setUp(self):

        self._query_definition = QueryDefinition()

        time_series_GDPMC1 = TimeSeries(database='FRED', data_id='GDPMC1', data_source='quandl')
        self._query_definition.add_time_series(time_series_id='GDPMC1', time_series=time_series_GDPMC1)

        time_series_CUUSA101SAF1 = TimeSeries(database='FRED', data_id='CUUSA101SAF1', data_source='quandl')
        self._query_definition.add_time_series(time_series_id='CUUSA101SAF1', time_series=time_series_CUUSA101SAF1)

        time_series_WDFUELLA = TimeSeries(database='FRED', data_id='WDFUELLA', data_source='quandl')
        self._query_definition.add_time_series(time_series_id='WDFUELLA', time_series=time_series_WDFUELLA)
        
        
    def test_query_definition(self):
        # Test query definition
        data = self._query_definition.data()
        for dataframe in data:
            assert len(dataframe) > 0


class TestDataRequest(unittest.TestCase):
    
    def setUp(self):

        query_definition = QueryDefinition()

        time_series_GDPMC1 = TimeSeries(database='FRED', data_id='GDPMC1', data_source='quandl')
        query_definition.add_time_series(time_series_id='GDPMC1', time_series=time_series_GDPMC1)

        time_series_CUUSA101SAF1 = TimeSeries(database='FRED', data_id='CUUSA101SAF1', data_source='quandl')
        query_definition.add_time_series(time_series_id='CUUSA101SAF1', time_series=time_series_CUUSA101SAF1)

        time_series_WDFUELLA = TimeSeries(database='FRED', data_id='WDFUELLA', data_source='quandl')
        query_definition.add_time_series(time_series_id='WDFUELLA', time_series=time_series_WDFUELLA)
        
        self._data_request = DataRequest(query_definition=query_definition, output_format='html')
        
        
    def test_query_definition(self):
        # Test query definition
        data = self._data_request.data()
        for dataframe in data:
            assert len(dataframe) > 0



if __name__ == '__main__':
    unittest.main()