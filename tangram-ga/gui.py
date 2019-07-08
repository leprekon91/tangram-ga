from tkinter import Tk, X, Label, Canvas, Frame, BOTH
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


canvas_padding = 20


class CreateCanvas(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Solution")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectangle = [canvas_padding, canvas_padding, 640+canvas_padding,
                     canvas_padding, canvas_padding + 640, canvas_padding + 640, canvas_padding, canvas_padding + 640, canvas_padding, canvas_padding]

        canvas.create_line(rectangle, dash=(4, 2), width=5)

        # draw all shapes
        canvasDraw(canvas, bgTri_1, 0, 0)
        canvasDraw(canvas, bgTri_2, 320, -160)
        canvasDraw(canvas, mdTri, 480, 480)
        canvasDraw(canvas, smTri_1, 240, 400)
        canvasDraw(canvas, smTri_2, 480, 80)
        canvasDraw(canvas, sqr, 320, 0)
        canvasDraw(canvas, paral, 0, 480)

        canvas.pack(fill=BOTH, expand=1)


def canvasDraw(canvas, shape, positionX, positionY):
    points = shape.getRotatedPoints(
        positionX+canvas_padding, positionY+canvas_padding)
    canvas.create_polygon(points, outline="#000", fill=shape.color)


def main():

    root = Tk()
    ex = CreateCanvas()
    root.geometry("700x700+100+100")
    root.mainloop()


if __name__ == '__main__':
    main()
