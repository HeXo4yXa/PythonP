from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(150,150), 100)
    c.draw(win)
	
    eye2 = Line(Point(150, 150), Point(250, 250))
    eye2.setWidth(3)
    eye2.draw(win)
	
    win.getMouse() # pause for click in window
    win.close()

main()