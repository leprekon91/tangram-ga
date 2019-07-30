import math
import random
import numpy as np
from scipy.spatial import ConvexHull
from shapely.geometry import Polygon
from functools import reduce

class TangramShape:
    def __init__(self, points, color, angle):
        self.points = points
        self.color = color
        self.angle = angle

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
    # receive a fitness number that should be zero if the sokution is correct.
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

    # calculate distance of all points that are out of bounds of the square
    out_of_bounds_distances = map(filterOutOfBounds, points)
    fitness += sum(out_of_bounds_distances)

    # calculate convex hull volume and add
    # the diffrence from the square to the fitness value
    convex_volume = ConvexHull(np.array(points)).volume
    # diff the areas
    volume_diff = (convex_volume - (640**2))
    if volume_diff < 0:
        volume_diff *= -1
    fitness += volume_diff

    # find and sum all intersections areas between shapes and add it to the fitness
    intersections_area = 0
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
                intersections_area += polygonsIntersect(points_i, points_j)
    fitness += intersections_area
    return fitness

def polygonsIntersect(points1, points2):
    # calculate intersection area between two polygons
    p1 = Polygon(points1)
    p2 = Polygon(points2)
    return p1.intersection(p2).area

def filterOutOfBounds(point):
    # if a point is out of the square,
    # calculate the distance in x and y and return a sum
    distance = 0
    if point[0] > 650:
        distance += point[0]-650
    if point[0] < 0:
        distance += (point[0]*-1)-10
    if point[1] > 650:
        distance += point[1]-650
    if point[1] < -10:
        distance += (point[0]*-1)-10
    return distance

def roundup(x):
    # roundup a float number to integer value
    return int(x)

def mutated_genes():
    #random shape generator
    possible_angles = [0,15,30,45,60,75,90,105,120,135,150,165,180]
    x = random.randint(0, 480)
    y = random.randint(-160, 480)
    a = possible_angles[random.randint(0, 12)]
    return [x, y, a]

def randomGenome():
    # random genome generator
    genome = []
    for i in range(len(shapeArray)):
        genome.append(mutated_genes())
    return genome

def crossover_operator(parent1, parent2,mutation_prob):
    # crossover operator
    child_chromosome = []
    for gp1, gp2 in zip(parent1, parent2):
        prob = random.random()

        # if prob is less than half of the unmutated probability, insert gene
        # from parent 1
        if prob < (1-mutation_prob)/2:
            child_chromosome.append(gp1)

        # if prob is the other half, insert
        # gene from parent 2
        elif prob < 1-mutation_prob:
            child_chromosome.append(gp2)
        # Mutate with MUTATION_PROB probability
        else:
            child_chromosome.append(mutated_genes())
    return child_chromosome
