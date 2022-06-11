"""
Author: Michael Smith
Date: February, 2021
Description: This program reads from an input file given
through the command line arguments(graph.txt). Takes the
points in the .txt file and then finds the min. spanning
tree of the graph. The results are outputted to the 
terminal with the edges and the total weight of the tree.
The process is repeated for every test case in the .txt 
that is used. I used piazza for majority of this assignment
as well as general internet research. I got some advice 
from one of my classmates when implementing the algorithm
functions inside the Graph class.
"""
import sys
import math

"""
Class: Graph
Description: Used to create the MST graph with the data 
given in the .txt file. Calculates the distance between
two points as well as the total weight of the graph. 
Then it prints to the terminal. The idea of using a class
was given to me from piazza, I haven't used classes in 
python very much so I had to use a lot of internet 
resources.
"""
class Graph:

    # Initializes the graph class attributes.
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
            for row in range(vertices)]

    # Calculates the distance between two coordinates
    def distance(self, x1, y1, x2, y2):
        xDistance = abs(x1 - x2)
        yDistance = abs(y1 - y2)
        x = xDistance*xDistance
        y = yDistance*yDistance
        finalDistance = round(math.sqrt(x + y))
        return int(finalDistance)

    # Returns the minimum index after comparing it
    def get_min(self, idx, inMST):
        min = sys.maxint
        for v in range(self.v):
            if idx[v] < min and inMST[v] == False:
                min = idx[v]
                minIndex = v
        return minIndex

    # Prints the point, (x,y), distance, and total weight of 
    # the MST to the terminal 
    def print_output(self, parent, xCoordinate, yCoordinate):
        weight = 0
        print("Edges in MST")
        print("Point  (x,y)          Distance")
        for i in range(1, self.v):
            u = parent[i]
            v = i
            point = "(" + str(xCoordinate[u]) + "," + str(yCoordinate[u]) + ") - (" + str(xCoordinate[v]) + "," + str(yCoordinate[v]) + ")"
            dist = self.graph[v][u]
            output = '{:<27} {:<12}'.format(point, dist)
            print(output)
            weight += self.graph[v][u]
        print("            Total distance %d \n" % (weight))

    # Finds a minimum spanning tree using the algorithm
    def get_mst(self, xCoordinate, yCoordinate):
        idx = [sys.maxint]*self.v
        parent = [None]*self.v
        idx[0] = 0
        inMST = [False]*self.v
        parent[0] = -1
        for x in range(self.v):
            u = self.get_min(idx, inMST)
            inMST[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and inMST[v] == False and idx[v] > self.graph[u][v]:
                    idx[v] = self.graph[u][v]
                    parent[v] = u;

        self.print_output(parent, xCoordinate, yCoordinate)

"""
This portion of code opens and reads the graph.txt file from
the command line arguments. It first gets the amount of 
test cases which should be the first line of the .txt file
being used. Then it iterates over the test cases and calls 
the Graph class for each one. I didn't really need as 
outside help for this portion of code because its pretty
similar to our previous homework assignments.
"""
file_name = sys.argv[1]
fp = open(file_name, "r")
num = fp.readline()
cases = int(num)
for f in range(cases):
    print("Test case: %d" % (f + 1))
    vertices = fp.readline()
    newGraph = Graph(int(vertices))
    xCoordinate = [None]*newGraph.v
    yCoordinate = [None]*newGraph.v
    for i in range(newGraph.v):
        coord = fp.readline()
        edge = coord.split()
        xCoordinate[i] = int(edge[0])
        yCoordinate[i] = int(edge[1])
    for u in range(newGraph.v):
        for v in range(newGraph.v):
            newGraph.graph[u][v] = newGraph.distance(xCoordinate[u], yCoordinate[u], xCoordinate[v], yCoordinate[v])
    newGraph.get_mst(xCoordinate, yCoordinate)

fp.close()