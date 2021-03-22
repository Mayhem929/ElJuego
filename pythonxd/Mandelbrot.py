from graphics import *

width = 600
height = 600


def printm(a, b):
    z = complex(0, 0)
    c = complex(a / width - 1.5, b / height - 0.5)
    iterations = 0
    while (z.real * z.real + z.imag * z.imag) ** (1 / 2) < 2 and iterations <= 50:
        z = z * z + c
        iterations += 1

    if iterations >= 50:
        return True
    else: return False

    # if iterations >= 30:
    #     return "black"
    # else:
    #     return "white"


win = GraphWin("MyWindow", width, height)
win.setBackground('white')

for i in range(width):
    for j in range(height):
        if (printm(i, j)):
            win.plot(i, j, "black")
    #    win.plotPixel(i, j, printm(i, j))

win.getMouse()
win.close()

