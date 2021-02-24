#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
#import decrypt
import keyring
import config
from shutil import copyfile

inputFullPath = r''+str(sys.argv[1])
print(inputFullPath)
#pwd = u''+'123'
#pwd = decrypt.decrypt_message()
host = config.getHost()
user = config.getUser()
pwd = keyring.get_password(host,user)
outputPath = os.path.dirname(r''+str(sys.argv[2]))
#convScriptPath = r'C:\conversion\scripts\conversion.py'
convScriptPath = config.getScriptPath()
path = os.path.split(inputFullPath)
print(path)
#fileName = path[1].split('_')
fileName = path
inputFullPath = path[0]+'\\'+fileName[1]
tmpDir = r'C:\conversion\tmp'
csvFile = tmpDir+'\\'+fileName[1]
#print(inputFullPath)
#print(csvFile)
copyfile(inputFullPath, csvFile)

command = []
command.append('echo '+pwd+'|')
command.append('C:\Windows\system32\schtasks.exe')
command.append('/change')
command.append('/tr')
command.append('\"'+convScriptPath)
command.append('\\\"'+csvFile+'\\\"')
command.append(outputPath+'\"')
command.append('/tn test')
command = ' '.join(command)

print(command)
subprocess.run(command, shell=True)
command = "C:\Windows\system32\schtasks.exe /run /tn test"
print(command)
subprocess.run(command, shell=True)