from tkinter import Tk, Canvas, Frame, BOTH
import math


class CreateCanvas(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Solution")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectangle = [5, 5, 395, 5, 395, 395, 5, 395, 5, 5]

        canvas.create_line(rectangle, dash=(4, 2), width=5)

        shape = [(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)]

        canvas.create_polygon(get_shape(shape, 100, 100),
                              outline="#fff", fill='#f00')

        canvas.pack(fill=BOTH, expand=1)


def get_shape(points, X, Y):
    coords = []
    print(points)
    for i in range(len(points)):
        coords.append(points[i][0]+X)
        coords.append(points[i][1]+Y)
    return coords


def main():

    root = Tk()
    ex = CreateCanvas()
    root.geometry("400x400+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
