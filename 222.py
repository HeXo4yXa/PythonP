from ctypes import windll
import win32gui, win32api
#import time
#win32api.MessageBox(0,"yes no cancel?", "title",3)
while True:
    hdc = windll.user32.GetDC(0)
    z=win32gui.GetCursorPos()
    print z
    color = windll.gdi32.GetPixel(hdc, z[0] , z[1])
    print hex(color)

