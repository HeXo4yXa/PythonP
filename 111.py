import win32gui
import time
time.clock()
for y in range(0, 100, 10):
    for x in range(0, 100, 10):
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x , y)
        print color
print(time.clock())
