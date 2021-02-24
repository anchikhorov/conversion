#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import coreldraw
import indesign
import illustrator
import corelphotopaint
from shutil import copyfile

inputFullPath = r''+str(sys.argv[1])
outputPath = r''+str(sys.argv[2])
indExt = ['.indl','.indd']
aiExt = ['.ai']
corelExt = ['.cdr']
photoshopExt = ['.tif','.tiff','.jpg','.pdf','.psd']
ifErrorPath = '' 


def conversion(inputFullPath,fullOutputPath): 
   if extension.lower() in indExt:
      try:
        indesign.convert(inputFullPath,fullOutputPath)
      except Exception as e:
        print('Something was wrong with Adobe Indesign: ' + str(e))
        copyfile(inputFullPath, ifErrorPath)
   if extension.lower() in corelExt:
      try:
        coreldraw.convert(inputFullPath, fullOutputPath)
      except Exception as e:
        print('Something was wrong with CorelDraw: ' + str(e))
        copyfile(inputFullPath, ifErrorPath)
        
   if extension.lower() in aiExt:
      try:
        illustrator.convert(inputFullPath,fullOutputPath)
      except Exception as e:
        print('Something was wrong with Adobe Illustrator: ' + str(e))
        copyfile(inputFullPath, ifErrorPath)

   if extension.lower() in photoshopExt:
      try:
        corelphotopaint.convert(inputFullPath,fullOutputPath)
      except Exception as e:
        print('Something was wrong with CorelPhotoPaint: ' + str(e))
        copyfile(inputFullPath, ifErrorPath)
        
# это для FreeFlow Core 6.0      
#path = os.path.split(inputFullPath)
#fileName = path[1].split('_')
#inputFullPath = path[0]+'\\'+fileName[1]
def fileExtCheck(inputFullPath):
    fileName = os.path.basename(inputFullPath)
    name, extension = os.path.splitext(fileName) 
    return extension

extension = fileExtCheck(inputFullPath)
#print(extension)
if extension == '.csv':
    with open(inputFullPath, encoding = "utf-8") as file:  
       data = file.readlines()
#       print(data)
       for i in data: 
          path = i.rstrip('\n')
#          print(path)
          fileName = os.path.basename(path)
          name, extension = os.path.splitext(fileName)
          fullOutputPath = outputPath+"\\"+fileName
#          print(fullOutputPath)
          fullOutputPath = outputPath+"\\"+name+".pdf" 
#          print(fullOutputPath)
          ifErrorPath = fullOutputPath          
          print('Входной файл: '+ path)
        
          try:        
             conversion(path,fullOutputPath)
#           print('Выходной файл: '+fullOutputPath)

          except Exception as e:
             print('Export to PDF failed: ' + str(e))
else:
     path = inputFullPath
     fileName = os.path.basename(path)
     name, extension = os.path.splitext(fileName)
     fullOutputPath = outputPath+"\\"+fileName
     fullOutputPath = outputPath+"\\"+name+".pdf" 
     ifErrorPath = fullOutputPath          
     print('Входной файл: '+ path)
     try:        
       conversion(path,fullOutputPath)
       os.remove(path)

     except Exception as e:
       print('Export to PDF failed: ' + str(e))
sys.exit()