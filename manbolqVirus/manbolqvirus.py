from graphics import *

def main():
    width = 2000
    height = 1200

    win = GraphWin("MyWindow", width, height)
    win.setBackground('black')

    gordo = Image(Point(0, 0), "manbolq.gif").getWidth()
    gordo_de_alto = Image(Point(0, 0), "manbolq.gif").getHeight()


    for i in range (int(gordo/2), width, gordo):
        for j in range (int(gordo_de_alto/2), height, gordo_de_alto):
            manbolq = Image(Point(i, j), "manbolq.gif")
            manbolq.draw(win)

    while True:
        key = win.checkKey()
        if key == "a":
            win.close()
        else: main()

    win.getMouse()
    win.close()


main()
