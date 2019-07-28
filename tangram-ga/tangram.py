import math
import random
import numpy as np
from scipy.spatial import ConvexHull
from shapely.geometry import Polygon

# shape object
MUTATION_PROB = 0.3


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

    # get points of shape in position X,Y and angle
    def getRotatedPoints(self, X, Y, angle):
        coords = []
        for i in range(len(self.points)):
            coords.append((self.points[i][0]+X, self.points[i][1]+Y))
        rads = math.radians(angle)
        cos_val = math.cos(rads)
        sin_val = math.sin(rads)
        cx, cy = self.getCenter(X, Y)
        new_points = []
        for x_old, y_old in coords:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([roundup(x_new + cx), roundup(y_new + cy)])
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

#
# getGenomeFitness - receive a fitness number that should be minimized.
#


def getGenomeFitness(genome):
    fitness = 0
    # get all points of genome
    points = []
    for i in range(len(genome)):
        shape_points = shapeArray[i].getRotatedPoints(
            genome[i][0],
            genome[i][1],
            genome[i][2]
        )
        points = points+shape_points
    out_of_bounds_points = len(list(filter(filterOutOfBounds, points)))
    fitness += out_of_bounds_points * 500
    # calculate convex hull
    convex_volume = ConvexHull(np.array(points)).volume
    # diff the areas
    fitness += (640**2 - convex_volume)**2
    # shouldn't be the only thing to compute the fitness
    # also need to find collisions between shapes
    intersections = 0
    for i in range(len(shapeArray)):
        points_i = shapeArray[i].getRotatedPoints(
            genome[i][0],
            genome[i][1],
            genome[i][2]
        )
        for j in range(len(shapeArray)):
            if i != j:
                points_j = shapeArray[j].getRotatedPoints(
                    genome[j][0],
                    genome[j][1],
                    genome[j][2]
                )
                if polygonsIntersect(points_i, points_j):
                    intersections += 1
    fitness += 500*(intersections/2)
    return roundup(fitness)

# check if two polygons intersect


def polygonsIntersect(points1, points2):
    p1 = Polygon(points1)
    p2 = Polygon(points2)
    return p1.intersects(p2)


def filterOutOfBounds(point):
    if point[0] > 640 or point[0] < 0:
        return True
    if point[1] > 640 or point[1] < 0:
        return True


def roundup(x):
    return int(x)

# generate a random shape genome


def randomGenome():
    genome = []
    for i in range(len(shapeArray)):
        x = random.randint(0, 480)
        y = random.randint(-160, 480)
        a = random.randint(0, 180)
        genome.append([x, y, a])
    return genome


def mutated_genes():
    x = random.randint(0, 480)
    y = random.randint(-160, 480)
    a = random.randint(0, 180)
    return [x, y, a]


def crossover_operator(parent1, parent2):
    child_chromosome = []
    for gp1, gp2 in zip(parent1, parent2):
        prob = random.random()

        # if prob is less than half of the unmutated probability, insert gene
        # from parent 1
        if prob < (1-MUTATION_PROB)/2:
            child_chromosome.append(gp1)

        # if prob is the other half, insert
        # gene from parent 2
        elif prob < 1-MUTATION_PROB:
            child_chromosome.append(gp2)
        # Mutate with MUTATION_PROB probability
        else:
            child_chromosome.append(mutated_genes())
    return child_chromosome
