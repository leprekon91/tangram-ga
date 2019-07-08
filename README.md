# tangram-ga

Tangram Solving Genetic Algorithm

## Description:

there are 7 pieces of tangram:

- large triangle (area 1/4)
- large triangle (area 1/4)
- medium triangle (area 1/8)
- small triangle (area 1/16)
- small triangle (area 1/16)
- square (area 1/8)
- parallelogram (area 1/8)

Arrange shapes into a sqaure to solve te puzzle.

### Shape object:

```
Shape:
 points,
 position, - centroid of shape, used to rotate. can be calculated.
 angle, in iterations of 45 degrees
 color, string of three hex values

```

### do two shapes collide?

```
isIntersection(pointArray1, pointArray2){
  p1 = Polygon(pointArray1)
  p2 = Polygon(pointArray2)
  return p1.intersects(p2)
}
```

### Random Genome

```
genome(){
  for each shape of the tangram:
    generate random position: (x,y)
    random angle: a
    add to genome array
}
```

### Crossover Operator

```
getSibling(papa,mama){
  x <= random(0,1)
  if x < mutationChance
    get random shape
}
```

### Fitness

```
fitnessFunctio(genome){
  generate all points of all shapes
    and put them into an array
  get convexhull of array
  get volume of convexHull
  //count intersections in the genome
  intersections = 0
  for each two shapes a,b in the genome:
    if(isIntersection(a.points,b.points)){
      intersections++
    }
  fitness <= (areaOfSquare + hullVolume)^2 + intersections* 10
  return fitness
}
```
