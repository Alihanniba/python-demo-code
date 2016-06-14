# _*_ coding:utf-8 _*_
import webbrowser as webimport
import time
import os


count = 0
while count < 0:
    count = count+1
    webimport.open_new_tab("http://www.cnblogs.com/smiler/archive/2010/04/20/1716418.html#2856973")
    time.sleep(1)
else:
    os.system('taskkill /F/IM 360se.exe')


