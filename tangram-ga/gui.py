from tkinter import Tk, X, Label, Canvas, Frame, BOTH
from tangram import TangramShape, shapeArray, getGenomeFitness, randomGenome, crossover_operator
from ga import GA
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
        # solve genetic algorithm:
        solution = GA(
                    randomGenome,
                    getGenomeFitness,
                    crossover_operator,
                    print_genome,
                    10,
                    100
                )
        drawGenome(canvas, solution)

        w = Label(
            self.master,
            text="Fitness: " + str(getGenomeFitness(solution)),
        )
        canvas.pack(fill=BOTH, expand=1)
        w.pack()


def print_genome(genome):
    print(str(genome))


def drawGenome(canvas, genome):

    for i in range(len(genome)):
        points = shapeArray[i].getRotatedPoints(
            genome[i][0]+canvas_padding,
            genome[i][1]+canvas_padding,
            genome[i][2]
        )
        canvas.create_polygon(
            points,
            outline="#000",
            fill=shapeArray[i].color,
        )


def main():
    root = Tk()
    ex = CreateCanvas()
    root.geometry("700x700+100+100")
    root.mainloop()


if __name__ == '__main__':
    main()
