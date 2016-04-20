# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:43:02 2016

@author: Hong
"""

from model.adapters import BaseAdapter
import Quandl


def adapter_factory(data_source):

    '''
    Adapter factory
    '''    

    class QuandlAdapter(BaseAdapter):
    
        def data(self, query_params):
            '''
            Return pandas dataframe containing Quandl data series
            '''
            # TODO store authtoken as configuration
            dataframe = Quandl.get('%s/%s'%(query_params['database'], query_params['data_id']), authtoken="uM-pW7KJQ61e_H7i6TEB")
            dataframe.columns = [query_params['data_id']]
            return dataframe

    if data_source == 'quandl':
        return QuandlAdapter()
    else:
        raise NotImplementedError('Missing adapter implementation for data_source = %s'%data_source)