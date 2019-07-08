from tkinter import Tk, Canvas, Frame, BOTH
from tangram import TangramShape
import math

bgTri_1 = TangramShape([(0, 0), (320, 320), (0, 640), (0, 0)], '#f00', 0)
bgTri_2 = TangramShape([(0, 0), (320, 320), (0, 640), (0, 0)], '#0f0', 90)
mdTri = TangramShape([(0, 0), (320, 0), (0, 320), (0, 0)], '#00f', 180)
smTri_1 = TangramShape([(0, 0), (320, 0), (160, 160), (0, 0)], '#ff0', 180)
smTri_2 = TangramShape([(0, 0), (320, 0), (160, 160), (0, 0)], '#f0f', 90)

sqr = TangramShape([(160, 160), (320, 320), (160, 480),
                    (0, 320), (160, 160)], '#0ff', 0)
paral = TangramShape([(0, 160), (160, 0), (480, 0),
                      (320, 160), (0, 160)], '#faf', 0)


class CreateCanvas(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Solution")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectangle = [0, 0, 640, 0, 640, 640, 0, 640, 0, 0]

        canvas.create_line(rectangle, dash=(4, 2), width=5)

        # draw all shapes
        canvas.create_polygon(bgTri_1.getRotatedPoints(0,0),
                              outline="#000", fill=bgTri_1.color)
        canvas.create_polygon(bgTri_2.getRotatedPoints(320,-160),
                              outline="#000", fill=bgTri_2.color)
        canvas.create_polygon(mdTri.getRotatedPoints(480,480),
                              outline="#000", fill=mdTri.color)
        canvas.create_polygon(smTri_1.getRotatedPoints(240,400),
                              outline="#000", fill=smTri_1.color)
        canvas.create_polygon(smTri_2.getRotatedPoints(480,80),
                              outline="#000", fill=smTri_2.color)
        canvas.create_polygon(sqr.getRotatedPoints(320,0),
                              outline="#000", fill=sqr.color)
        canvas.create_polygon(paral.getRotatedPoints(0,480),
                              outline="#000", fill=paral.color)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = CreateCanvas()
    root.geometry("700x700+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
