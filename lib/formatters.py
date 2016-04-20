# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:30:56 2016

@author: Hong
"""

from model.formatters import BaseFormatter
from constants import Operation
from matplotlib.backends.backend_pdf import PdfPages
import os


def formatter_factory(output_format=None):

    '''
    Formatter factory
    - Plotly would be cool e.g. from INotebook/Jupyter https://plot.ly/pandas/multiple-axes/
    '''

    class HTMLFormatter(BaseFormatter):
    
        def to_file(self, file_path, data, time_series):
            '''
            TODO Use a templating module
            '''
            with open(file_path, 'w') as html_file:
                html_file.write('''
        <!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
         <HTML>
            <HEAD>
               <TITLE>
                  Example DSL HTML Report
               </TITLE>
            </HEAD>
         <BODY>
            <H2>Example DSL HTML Report</H2>
                ''')
                for data_label, dataframe in data.items():
                    time_series_ref = time_series[data_label]
                    for (operation, operation_arg) in time_series_ref._operations:
                        if operation == Operation.stats:
                            self.stats(dataframe=dataframe, operation_arg=operation_arg).to_html(html_file)
                        elif operation == Operation.table:
                            dataframe.to_html(html_file)
                        elif operation == Operation.graph:
                            file_name_png = '%s.png' % data_label
                            file_path_png = file_path.replace(file_path.split(os.path.sep)[-1], file_name_png)
                            logy = False
                            if operation_arg == 'monthly':
                                dataframe = dataframe.resample(rule='BM')
                            elif operation_arg == 'scale_log':
                                logy = True
                            self.dataframe_plot_png(data_frame=dataframe, fname=file_path_png, title=time_series_ref.title(), logy=logy)
                            html_file.write('<img src="%s" alt="%s">'%(file_name_png, file_name_png))
                        else:
                            raise NotImplementedError('Missing implementation for HTML operation %s'%operation)
                    html_file.write('<br/>')
                html_file.write('''
         </BODY>
         </HTML>
                ''')


    class PDFFormatter(BaseFormatter):    
    
        def to_file(self, file_path, data, time_series):
            '''
            Matplotlib
            '''
            pdf_pages = PdfPages(file_path)
            for data_label, dataframe in data.items():
                time_series_ref = time_series[data_label]
                for (operation, operation_arg) in time_series_ref._operations:
                    if operation == Operation.graph:
                        logy = False
                        if operation_arg == 'monthly':
                            dataframe = dataframe.resample(rule='BM')
                        elif operation_arg == 'scale_log':
                            logy = True
                        pdf_pages.savefig(figure=dataframe.plot(title=time_series_ref.title(), logy=logy).get_figure())
                    elif operation == Operation.table:
                        pdf_pages.savefig(figure=dataframe.plot(title=time_series_ref.title(), table=True).get_figure())
                    elif operation == Operation.stats:
                        dataframe = self.stats(dataframe=dataframe, operation_arg=operation_arg)
                        pdf_pages.savefig(figure=dataframe.plot(table=True).get_figure())
                    else:
                        raise NotImplementedError('Missing implementation for PDF operation %s'%operation)
            pdf_pages.close()

    if output_format is None or output_format == 'html':
        return HTMLFormatter()
    elif output_format == 'pdf':
        return PDFFormatter()
    else:
        raise NotImplementedError('Missing formatter implementation for output_format = %s'%output_format)