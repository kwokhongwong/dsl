# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:30:56 2016

@author: Hong
"""

from abc import ABCMeta, abstractmethod
import pandas as pd


class BaseFormatter(metaclass=ABCMeta):

    def dataframe_plot_png(self, data_frame, fname, logy=False, title=None):
        title = title or ''
        data_frame.plot(title=title, logy=logy).get_figure().savefig(fname)
        
    def stats(self, dataframe, operation_arg):
        if hasattr(dataframe, operation_arg):
            return pd.DataFrame(getattr(dataframe, operation_arg)(), columns=[operation_arg])
        else:
            raise ValueError('Invalid stats_arg %s'%operation_arg)
            
    @abstractmethod
    def to_file(self, file_path, data, time_series):
        pass