from tkinter import Tk, X, Label, Canvas, Frame, BOTH
from tangram import TangramShape, shapeArray
import math

canvas_padding = 20


class CreateCanvas(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Solution")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        rectangle = [0, 0, 640, 0, 640, 640, 0, 640, 0, 0]
        for i in range(len(rectangle)):
            rectangle[i] += canvas_padding

        canvas.create_line(rectangle, dash=(4, 2), width=5)

        # draw an example genome
        example_genome = [
            [0, 0, 0],
            [320, -160, 90],
            [480, 480, 180],
            [240, 400, 180],
            [480, 80, 90],
            [320, 0, 0],
            [0, 480, 0],
        ]

        drawGenome(canvas, example_genome)
        canvas.pack(fill=BOTH, expand=1)


def drawGenome(canvas, genome):
    for i in range(len(genome)):
        shapeArray[i].angle = genome[i][2]
        points = shapeArray[i].getRotatedPoints(
            genome[i][0]+canvas_padding,
            genome[i][1]+canvas_padding
        )
        canvas.create_polygon(
            points,
            outline="#000",
            fill=shapeArray[i].color
        )


def main():
    root = Tk()
    ex = CreateCanvas()
    root.geometry("700x700+100+100")
    root.mainloop()


if __name__ == '__main__':
    main()
