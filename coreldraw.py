#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import win32com.client, win32gui, win32process
import subprocess
import time
import config

def convert(inputFullPath,fullOutputPath):
   
   app = win32com.client.Dispatch('CorelDRAW.Application')

   myDocument = app.OpenDocument(inputFullPath)

   i = 0
   pages = myDocument.Pages.Count

   while i < pages:
      i = i + 1

      shapes = myDocument.Pages.Item(i).Shapes.Count
      myDocument.Pages.Item(i).Layers.Item(2).Shapes.All().CreateSelection()
      shape = app.ActiveSelection.Group()
      width = shape.BoundingBox.Width
      height = shape.BoundingBox.Height  
      myDocument.Pages.Item(i).SetSize(width, height)
      shape.CenterY = myDocument.Pages.Item(i).CenterY
      shape.CenterX = myDocument.Pages.Item(i).CenterX
      myDocument.PDFSettings.Author = "123456789"
      if i == pages:
         break

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
      
