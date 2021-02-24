#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import win32com.client


def convert(inputFullPath,fullOutputPath):

    app = win32com.client.Dispatch('CorelPHOTOPAINT.Application')
    app.Visible = False

    myDocument = app.OpenDocument(inputFullPath)
#    myDocument.PDFSettings.Load('Prepress')
    myDocument.PDFSettings.Author = "123456789"
#    myDocument.PDFSettings.JPEGQualityFactor = "80"
    directory = os.path.dirname(fullOutputPath)

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        if os.path.exists(directory):
            myDocument.PublishToPDF(fullOutputPath)
            print('Выходной файл: '+fullOutputPath)
    except Exception as e:
        print('Export to PDF failed: ' + str(e))
    myDocument.Dirty = False    
    myDocument.Close()