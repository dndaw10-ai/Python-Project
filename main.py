# convert_gui.pyw
# Program to convert Celsius to Fahrenheit using a simple
#   graphical interface.

from graphics import *

def main():
    win = GraphWin("House", 300, 200)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Draw the interface
    Rectangle(Point(1,1), Point(2,2)).draw(win)
    Line(Point(2,2), Point(1.5,3)).draw(win)
    Line(Point(1,2), Point(1.5,3)).draw(win)
  
    # wait for click and then quit
    win.getMouse()
    win.close()
    
main()