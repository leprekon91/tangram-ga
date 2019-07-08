import math
import numpy as np
from scipy.spatial import ConvexHull

# shape object


class TangramShape:
    def __init__(self, points, color, angle):
        self.points = points
        self.color = color
        self.angle = angle
        self.posX = 0
        self.posY = 0

    def setPosition(self, x, y):
        self.posX = x
        self.posY = y

    def getCenter(self, X, Y):
        centroid = ((sum([p[0] for p in self.points]) / len(self.points))+X,
                    (sum([p[1] for p in self.points]) / len(self.points))+Y)
        return centroid

    # get points of shape in position X,Y and self.angle
    def getRotatedPoints(self, X, Y):
        coords = []
        for i in range(len(self.points)):
            coords.append((self.points[i][0]+X, self.points[i][1]+Y))
        rads = math.radians(self.angle)
        cos_val = math.cos(rads)
        sin_val = math.sin(rads)
        cx, cy = self.getCenter(X, Y)
        new_points = []
        for x_old, y_old in coords:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points


# possible shapes
bgTri_1 = TangramShape([(0, 0), (320, 320), (0, 640), (0, 0)], '#f00', 0)
bgTri_2 = TangramShape([(0, 0), (320, 320), (0, 640), (0, 0)], '#0f0', 90)
mdTri = TangramShape([(0, 0), (320, 0), (0, 320), (0, 0)], '#00f', 180)
smTri_1 = TangramShape([(0, 0), (320, 0), (160, 160), (0, 0)], '#ff0', 180)
smTri_2 = TangramShape([(0, 0), (320, 0), (160, 160), (0, 0)], '#f0f', 90)
sqr = TangramShape([(160, 160), (320, 320), (160, 480),
                    (0, 320), (160, 160)], '#0ff', 0)
paral = TangramShape([(0, 160), (160, 0), (480, 0),
                      (320, 160), (0, 160)], '#555', 0)


shapeArray = [bgTri_1, bgTri_2, mdTri, smTri_1, smTri_2, sqr, paral]


def getGenomeFitness(genome):
    # get all points of genome
    points = []
    for i in range(len(genome)):
        shapeArray[i].angle = genome[i][2]
        shape_points = shapeArray[i].getRotatedPoints(
            genome[i][0],
            genome[i][1]
        )
        points = points+shape_points
    # calculate convex hull
    print(points)
    convex_volume = ConvexHull(np.array(points)).volume
    print(convex_volume)


getGenomeFitness(
    [
        [0, 0, 0],
        [320, -160, 90],
        [480, 480, 180],
        [240, 400, 180],
        [480, 80, 90],
        [320, 0, 0],
        [0, 480, 0],
    ]
)
