#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32gui, win32con, win32com.client

IllustratorWindow = win32gui.FindWindow('illustrator',None)
InDesignWindow = win32gui.FindWindow('indesign',None)
CorelDrawWindow = win32com.client.Dispatch('CorelDRAW.Application')
CorelPhotoPaintWindow = win32com.client.Dispatch('CorelPHOTOPAINT.Application')

win32gui.ShowWindow(IllustratorWindow,win32con.SW_HIDE)
win32gui.ShowWindow(InDesignWindow,win32con.SW_HIDE)
CorelPhotoPaintWindow.Visible = False
CorelDrawWindow.Visible = False