#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import win32gui, win32con, win32com.client


def convert(inputFullPath,fullOutputPath):

    app = win32com.client.Dispatch('InDesign.Application')
    time.sleep(1)
    app.ScriptPreferences.UserInteractionLevel=1699640946

    inDesignWindow = win32gui.FindWindow('indesign',None)
    win32gui.ShowWindow(inDesignWindow,win32con.SW_HIDE)

    try:
        myDocument = app.Open(inputFullPath, False)
        directory = os.path.dirname(fullOutputPath)

        idPDFType = 1952403524
        idNo = 1852776480
        myPDFPreset = app.PDFExportPresets.Item(6)
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            if os.path.exists(directory):
                myDocument.Export(idPDFType, fullOutputPath, False, myPDFPreset)
                print('Выходной файл: '+fullOutputPath)
        except Exception as e:
            print('Export to PDF failed: ' + str(e))
        myDocument.Close(idNo)
    except Exception as e:
        print('Export to PDF failed: ' + str(e))
