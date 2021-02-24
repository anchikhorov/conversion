#!/usr/bin/env python
# -*- coding: utf-8 -*-

import findWindow
import subprocess
import win32com.client


command = "C:\Program Files\Corel\CorelDRAW Graphics Suite 2019\Programs64\CorelDRW.exe"
pid = subprocess.Popen(command).pid

findWindow.find(pid)

cpp = win32com.client.Dispatch('CorelPHOTOPAINT.Application')
ill = win32com.client.Dispatch('Illustrator.Application')
ind = win32com.client.Dispatch('InDesign.Application')
cdr = win32com.client.Dispatch('CorelDRAW.Application')
cdr.Visible = False