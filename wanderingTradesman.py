import pygame as pg

import random, math, itertools

POINTS = 4

pg.init()

screen = pg.display.set_mode((800, 600))

screen.fill((255, 255, 255))

pointLocs = []

for i in range(POINTS):
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    pointLocs.append((x, y))
    pg.draw.circle(screen, (0, 0, 255), (x, y), 5)

print(pointLocs)

starting = pointLocs[0]
print("starting:", starting)

numPaths = int(math.factorial(POINTS - 1))

numSolutions = numPaths / 2

print("paths:", numPaths)


paths = list(itertools.permutations(pointLocs, POINTS))

filteredPaths = []

#print(paths)

for path in paths:
    path = list(path)
    if path[0] == starting:
        buffer = () + starting
        path.append(starting)
        filteredPaths.append(path)

print("filtered paths:", filteredPaths)



running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    minDist = 10000000000000000
    for i in range(numPaths):
        print(i)
        dist = 0
        curPath = filteredPaths[i]
        pg.draw.lines(screen, (0, 0, 255), False, curPath, 2)
        for j in range(len(curPath) - 1):
            dist += math.sqrt((curPath[j][0] + curPath[j + 1][0])**2 + (curPath[j][1] + curPath[j + 1][1])**2)
        print("dist:", dist)
        if dist <= minDist:
            minDist = dist
            print("min path:", i)
            minPath = [curPath, i]
    
    pg.draw.lines(screen, (0, 255, 0), False, minPath[0], 2)
    print("min path:", minPath[1])
    

    pg.display.flip()
    break
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
