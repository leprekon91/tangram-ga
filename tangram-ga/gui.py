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

        shape = [(0, 0), (100, 0), (100, 100), (0, 0)]

        canvas.create_polygon(get_shape(shape, 100, 100, 90),
                              outline="#fff", fill='#f00')

        canvas.pack(fill=BOTH, expand=1)


def rotate(points, angle, center):
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points


def get_shape(points, X, Y, angle):
    coords = []
    centroid = ((sum([p[0] for p in points]) / len(points))+X,
                (sum([p[1] for p in points]) / len(points))+Y)

    for i in range(len(points)):
        coords.append((points[i][0]+X, points[i][1]+Y))
    print(rotate(coords, angle, centroid))
    # rotate

    return rotate(coords, angle, centroid)


def main():

    root = Tk()
    ex = CreateCanvas()
    root.geometry("400x400+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
