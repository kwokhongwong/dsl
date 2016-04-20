# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:57:29 2016

@author: Hong
"""

import antlr4
import os
import unittest
from dsl.dslLexer import dslLexer
from dsl.dslParser import dslParser
from dsl.dslVisitorOverride import dslVisitorOverride

'''
antlr4 -no-listener -visitor dsl.g4
- see /dsl/dsl.g4
'''

def dir_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp', '')

def test_output(input_stream, dir_path, filename_without_ext):
    dsl_lexer = dslLexer(antlr4.InputStream(input_stream))
    common_token_stream = antlr4.CommonTokenStream(dsl_lexer)
    dsl_parser = dslParser(common_token_stream)
    dsl_visitor = dslVisitorOverride()
    dsl_visitor.setDebug(debug=False)
    dsl_visitor.visit(tree=dsl_parser.expression())
    data_request = dsl_visitor._data_request
    return data_request.to_file(dir_path=dir_path, filename_without_ext=filename_without_ext)


class TestDslHtmlWDFUELLA(unittest.TestCase):

    def setUp(self):
        self._input_stream = 'html "Nat Gas" t WDFUELLA'

    def test_dsl(self):
        (data, file_path) = test_output(self._input_stream, dir_path=dir_path(), filename_without_ext='TestDslHtmlWDFUELLA')
        assert len(data) > 0
        assert len(file_path) > 0


class TestDslPdfWDFUELLA(unittest.TestCase):

    def setUp(self):
        self._input_stream = 'pdf "Nat Gas" g WDFUELLA'

    def test_dsl(self):
        (data, file_path) = test_output(self._input_stream, dir_path=dir_path(), filename_without_ext='TestDslPdfWDFUELLA')
        assert len(data) > 0
        assert len(file_path) > 0

        
class TestDslHtmlTable(unittest.TestCase):

    def setUp(self):
        self._input_stream = '"Nat Gas" g WDFUELLA; "New York CPI" t CUUSA101SAF1'

    def test_dsl(self):
        (data, file_path) = test_output(self._input_stream, dir_path=dir_path(), filename_without_ext='TestDslHtmlTable')
        assert len(data) > 0
        assert len(file_path) > 0


class TestDslHtmlSplat(unittest.TestCase):

    def setUp(self):
        self._input_stream = 'html "New York CPI" g?scale_log,s?mean CUUSA101SAF1; "Nat Gas" g?monthly WDFUELLA'

    def test_dsl(self):
        (data, file_path) = test_output(self._input_stream, dir_path=dir_path(), filename_without_ext='TestDslHtmlSplat')
        assert len(data) > 0
        assert len(file_path) > 0


class TestDslPdfSplat(unittest.TestCase):

    def setUp(self):
        self._input_stream = 'pdf "New York CPI" g?scale_log,s?mean CUUSA101SAF1; "Nat Gas" g?monthly WDFUELLA'

    def test_dsl(self):
        (data, file_path) = test_output(self._input_stream, dir_path=dir_path(), filename_without_ext='TestDslPdfSplat')
        assert len(data) > 0
        assert len(file_path) > 0


if __name__ == '__main__':
    unittest.main()