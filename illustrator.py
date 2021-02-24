#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import win32gui, win32con, win32com.client

def convert(inputFullPath,fullOutputPath):

    app = win32com.client.Dispatch('Illustrator.Application')
    time.sleep(1)
    app.UserInteractionLevel = -1

    IllustratorWindow = win32gui.FindWindow('illustrator',None)
    win32gui.ShowWindow(IllustratorWindow,win32con.SW_HIDE)
    
    try:
        myDocument = app.Open(inputFullPath)
        
        i = 0
        for i in range(myDocument.Layers.Count):
            myDocument.Layers[i].Locked = False
            myDocument.Layers[i].HasSelectedArtwork = True
            
        myDocument.FitArtboardToSelectedArt(0)
        
        directory = os.path.dirname(fullOutputPath)

        saveOpts = win32com.client.Dispatch('Illustrator.PDFSaveOptions')
        saveOpts.Compatibility = 5

        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            if os.path.exists(directory):
                myDocument.SaveAs(fullOutputPath,saveOpts)
                print('Выходной файл: '+fullOutputPath)
        except Exception as e:
            print('Export to PDF failed: ' + str(e))
        myDocument.Close(2)
    except Exception as e:
        print('Export to PDF failed: ' + str(e))
