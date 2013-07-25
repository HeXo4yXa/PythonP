# -*- coding: utf-8 -*-
'''import win32com.client
import ctypes

MessageBox = ctypes.windll.user32.MessageBoxA
MessageBox(None, 'Press OK to end the demo.', 'Deviare Python Demo', 0)
#-------------------------------------
import win32api
import time

while True:
	print "Caps Locking...", time.asctime()
	win32api.mouse_event(2,0,0)
	win32api.mouse_event(1,100,-50)
	win32api.mouse_event(4,0,0)
	time.sleep(1 * 5)
#-------------------------------------



import win32api

# Свободно / полная емкость указанного диска
print win32api.GetDiskFreeSpaceEx('C:\\')
print win32api.GetDiskFreeSpace('C:\\')
# информация о системе (количество процессоров и т.д)
print win32api.GetSystemInfo()
# Temp directory в ОС
print win32api.GetTempPath()
# инфа о диске, тип файловой системы и т.д.
print win32api.GetVolumeInformation('C:\\')
# Наименование логических дисков в системе
print win32api.GetLogicalDriveStrings().split("\x00")[:-1]
# установит курсор в позицию x,y
print win32api.SetCursorPos([100,500])
# Имя текущего компьютера
print win32api.GetComputerName()
# Имя текущего пользователя в системе
print win32api.GetUserName()
# текущие координаты курсора (помните 100 и 500 :) )
print win32api.GetCursorPos()
# время системы год,месяц,_,число,час,минута,секунда,милисекунда
print win32api.GetLocalTime()
# возвращает инфу и питании компа
print win32api.GetPwrCapabilities()
# путь к системной папке
print win32api.GetSystemDirectory()
# резерв памяти для файлового кеша
print win32api.GetSystemFileCacheSize()
# количество милисекунд со времени старта Windows
print win32api.GetTickCount()
# версия винды и установленый сервис пак
print win32api.GetVersionEx()
# директория с windows
print win32api.GetWindowsDirectory()
# информация о памяти в системе (подкачка, виртуальная...)
print win32api.GlobalMemoryStatusEx()
#----------------------------------------'''
from urllib import *

data = urlopen('http://www.kickboxing.md')
string = data.read()
print string