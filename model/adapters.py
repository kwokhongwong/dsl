# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:43:02 2016

@author: Hong
"""

from abc import ABCMeta, abstractmethod


class BaseAdapter(metaclass=ABCMeta):

    @abstractmethod
    def data(self, query_params):
        pass