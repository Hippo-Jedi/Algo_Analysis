"""
Author: Michael Smith
Date: March, 2021
Description: This software uses 2-opt and greedy algorithm to 
solve the travelling salesman problem. The command to run it is
'python3 tsp.py tsp_example_n.txt'. It will output a .tour file
with the calculated optimal path.
"""
import math
import time
import sys

# City class with id, x, and y attributes
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

# Function reads input values and called functions, then writes ouput file
def begin():
    inputfilename = sys.argv[1]
    startT = time.time()
    cities = []
    with open(inputfilename, "r") as inputFile:
        num = int(inputFile.readline())
        for l in range(num):
            line = inputFile.readline()
            var = line.split()
            city = []
            for item in var:
                city.append(int(item))
            cities.append(City(city[0], city[1], city[2]))
    path = closest_city(cities)
    path = two_opt_path(path, startT)
    total = get_total(path)
    with open(inputfilename + ".tour", "w") as outputFile:
        outputFile.write(str(total) + '\n')
        for city in path:
            outputFile.write("%s\n" % city.id)
    runtime = time.time() - startT
    print("Tour = %s" % str(total))
    print("runtime = %.2f" % runtime)

# Function reoders the overlapping route of the 2-opt
def swap(R, i, j):
    newR = R[0:i]
    newR.extend(reversed(R[i:j + 1]))
    newR.extend(R[j + 1:])
    return newR

# Function optimizes 2-opt route
def two_opt_path(path, startT):
    endT = startT + 179
    check = True
    while check:
        check = False
        min = get_total(path)
        for i in range(len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                if distance(path[i - 1], path[i]) + distance(path[j], path[j + 1]) >= distance(path[i], path[j + 1]) + distance(path[i - 1], path[j]):
                    newpath = swap(path, i, j)
                    newDistance = get_total(newpath)
                    if newDistance < min:
                        path = newpath
                        min = newDistance
                        check = True
                    if time.time() > endT:
                        return path
    return path

# Function finds distance between cities
def distance(city1, city2):
    distance = int(round(math.sqrt(pow((int(city1.x) - int(city2.x)), 2) + pow((int(city1.y) - int(city2.y)), 2))))
    return distance

# Function finds the total distance bettween a list of cities
def get_total(path):
    total = 0
    for i in range(0, len(path) - 1):
        total += distance(path[i], path[i + 1])
    total += distance(path[len(path) - 1], path[0])
    return total

# Function finds the optimal city given distances
def closest_city(cities):
    path = []
    current = cities.pop(0)
    path.append(current)
    while (cities):
        min = float("inf")
        next = current
        for city in cities:
            newDistance = distance(current, city)
            if newDistance < min:
                min = newDistance
                next = city
        current = next
        path.append(current)
        cities.remove(current)
    return path

begin()