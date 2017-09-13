# Tool 	        	: XFO_Detector.py
# Author		      : Mayendran Govender
# Date Created    : 17 June 2014
# Description		: This tool scans  your webserver and determines what directive you have set for X-FRAME-OPTIONS. This will allow you to determine what settings you should decide on to prevent Click Jacking  
# Usage           : python XFO_Detector.py 

###########Important Notice - Please test this Tool in a test platorm and understand how this tool works before using in a production platform. 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#For Details please see - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

###########Modules Loaded
import platform		                # Loading the list of  Modules
import os
import subprocess
import sys
import datetime
import time

#########Core Detection Module
with open("XFO_Detector.log","a+") as stdout: # The XFO_Detector.log file is the output file that will contain the X-Frame Option settings.
   subprocess.Popen('HEAD example.com | grep "X-FRAME-OPTIONS"' ,  shell=True, stdout=stdout, stderr=stdout) # change example.com to your domain  name 

########Date Timestamp
import datetime 
f=open("XFO_Detector.log",'a')

f.write ("This is your Setting for X-FRAME-OPTIONS, Please see link in script to determine what to setting to use to prevent clickjacking"+'\t') # Appending info 

f.write ('\n')
f.write(datetime.datetime.now().ctime())

