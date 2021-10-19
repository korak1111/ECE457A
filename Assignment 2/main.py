# Cyrus Rupa 2021 for ECE457A A#2
import collections
import math
import numpy as np
from queue import Queue
from queue import LifoQueue
import heapq
from termcolor import colored

mazeList = ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]])


class Maze:
    def __init__(self, mazeArr, start, end):
        self.mazeArr = mazeArr
        self.start = start
        self.end = end
        self.visitedTiles = np.zeros((len(mazeArr), len(mazeArr[0])))
        self.numNodesVisited = 0
        self.cost = 0

    def printMaze(self):
        temp = []
        print("Printing Maze:")
        for i in range(len(self.mazeArr), -2, -1):
            for j in range(-1, len(self.mazeArr[0]) + 1):
                if i == -1 or i == 25:
                    temp.append(colored("-", "red"))
                elif j == -1 or j == 25:
                    temp.append(colored("|", "red"))
                elif i == self.start[0] and j == self.start[1]:
                    temp.append(colored("S", "green"))
                elif i == self.end[0] and j == self.end[1]:
                    temp.append(colored("E", "red"))
                elif self.visitedTiles[i][j] == -1:
                    temp.append(colored("X", "green"))
                    self.cost += 1
                elif self.visitedTiles[i][j] == 2:
                    temp.append(colored("*", "cyan"))
                elif self.mazeArr[i][j] == 1:
                    temp.append("#")
                elif self.mazeArr[i][j] == 0:
                    temp.append(" ")
            print(*temp)
            temp = []

    def nodesVisited(self):
        for i in range(len(self.visitedTiles)):
            for j in range(len(self.visitedTiles[0])):
                if self.visitedTiles[i][j] != 0:
                    self.numNodesVisited += 1
        return self.numNodesVisited


class Node:
    def __init__(self, x, y, distStart=0, parent=None, aStar=False):
        self.x = x
        self.y = y
        self.distStart = distStart
        self.parent = parent
        self.aStar = aStar
        self.estimate = math.sqrt(((end[0] - self.x) * 2) + ((end[1] - self.y) * 2))  # pythagorean distance to goal

    def __lt__(self, other):
        return True


def addMoves(currentNode, Maze, queue, aStar=False):
    if not aStar:
        # Go Up?
        # not at edge, not at wall, not already visited
        if (not currentNode.x == 24) and Maze.mazeArr[currentNode.x + 1][currentNode.y] == 0 and (
                Maze.visitedTiles[currentNode.x + 1][currentNode.y] == 0):
            newNode = Node(currentNode.x + 1, currentNode.y, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x + 1, currentNode.y] = 1  # Added to Queue
            queue.put(newNode)
        # Go down?
        # not at edge, not at wall, not already visited
        if (not currentNode.x == 0) and Maze.mazeArr[currentNode.x - 1][currentNode.y] == 0 and (
                Maze.visitedTiles[currentNode.x - 1][currentNode.y] == 0):
            newNode = Node(currentNode.x - 1, currentNode.y, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x - 1, currentNode.y] = 1  # Added to Queue
            queue.put(newNode)
        # Go Right?
        # not at edge, not at wall, not already visited
        if (not currentNode.y == 24) and Maze.mazeArr[currentNode.x][currentNode.y + 1] == 0 and (
                Maze.visitedTiles[currentNode.x][currentNode.y + 1] == 0):
            newNode = Node(currentNode.x, currentNode.y + 1, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x, currentNode.y + 1] = 1  # Added to Queue
            queue.put(newNode)
        # Go Left?
        # not at edge, not at wall, not already visited
        if (not currentNode.y == 0) and Maze.mazeArr[currentNode.x][currentNode.y - 1] == 0 and (
                Maze.visitedTiles[currentNode.x][currentNode.y - 1] == 0):
            newNode = Node(currentNode.x, currentNode.y - 1, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x, currentNode.y - 1] = 1  # Added to Queue
            queue.put(newNode)
    else:
        # Go Up?
        # not at edge, not at wall, not already visited
        if (not currentNode.x == 24) and Maze.mazeArr[currentNode.x + 1][currentNode.y] == 0 and (
                Maze.visitedTiles[currentNode.x + 1][currentNode.y] == 0):
            newNode = Node(currentNode.x + 1, currentNode.y, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x + 1, currentNode.y] = 1  # Added to Queue
            newNode.estimate = newNode.distStart + newNode.estimate
            heapq.heappush(queue, (newNode.estimate, newNode))
        # Go down?
        # not at edge, not at wall, not already visited
        if (not currentNode.x == 0) and Maze.mazeArr[currentNode.x - 1][currentNode.y] == 0 and (
                Maze.visitedTiles[currentNode.x - 1][currentNode.y] == 0):
            newNode = Node(currentNode.x - 1, currentNode.y, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x - 1, currentNode.y] = 1  # Added to Queue
            newNode.estimate = newNode.distStart + newNode.estimate
            heapq.heappush(queue, (newNode.estimate, newNode))

        # Go Right?
        # not at edge, not at wall, not already visited
        if (not currentNode.y == 24) and Maze.mazeArr[currentNode.x][currentNode.y + 1] == 0 and (
                Maze.visitedTiles[currentNode.x][currentNode.y + 1] == 0):
            newNode = Node(currentNode.x, currentNode.y + 1, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x, currentNode.y + 1] = 1  # Added to Queue
            newNode.estimate = newNode.distStart + newNode.estimate
            heapq.heappush(queue, (newNode.estimate, newNode))

        # Go Left?
        # not at edge, not at wall, not already visited
        if (not currentNode.y == 0) and Maze.mazeArr[currentNode.x][currentNode.y - 1] == 0 and (
                Maze.visitedTiles[currentNode.x][currentNode.y - 1] == 0):
            newNode = Node(currentNode.x, currentNode.y - 1, currentNode.distStart + 1, currentNode)
            Maze.visitedTiles[currentNode.x, currentNode.y - 1] = 1  # Added to Queue
            newNode.estimate = newNode.distStart + newNode.estimate
            heapq.heappush(queue, (newNode.estimate, newNode))


def getPath(currentNode, Maze):
    path = []
    while currentNode.parent != None:
        path.append([currentNode.x, currentNode.y])
        Maze.visitedTiles[currentNode.x, currentNode.y] = -1  # mark on path
        currentNode = currentNode.parent
    path.append([currentNode.x, currentNode.y])
    revPath = path[::-1]
    for i in revPath:
        temp = i[0]
        i[0] = i[1]
        i[1] = temp
    return revPath


def BFS(Maze):
    currentNode = Node(Maze.start[0], Maze.start[1])
    while not (currentNode.x == Maze.end[0] and currentNode.y == Maze.end[1]):
        Maze.visitedTiles[currentNode.x, currentNode.y] = 2
        addMoves(currentNode, Maze, bfsQ)
        currentNode = bfsQ.get()
    # print("Path Found!")
    bfsPath = getPath(currentNode, Maze)
    return bfsPath


def DFS(Maze):
    currentNode = Node(Maze.start[0], Maze.start[1])
    while not (currentNode.x == Maze.end[0] and currentNode.y == Maze.end[1]):
        Maze.visitedTiles[currentNode.x, currentNode.y] = 2
        addMoves(currentNode, Maze, dfsQ)
        currentNode = dfsQ.get()
    # print("Path Found!")
    dfsPath = getPath(currentNode, Maze)
    return dfsPath


def aStarS(Maze):
    currentNode = Node(Maze.start[0], Maze.start[1])
    while not (currentNode.x == Maze.end[0] and currentNode.y == Maze.end[1]):
        Maze.visitedTiles[currentNode.x, currentNode.y] = 2
        addMoves(currentNode, Maze, aStarQ, True)
        currentNode = heapq.heappop(aStarQ)[1]
    # print("Path Found!")
    aStarPath = getPath(currentNode, Maze)
    return aStarPath


print("Case 1 S:(3,12) to E:(24,20)")
start = [11, 2]
end = [19, 23]

print("Case 2: 3,12 to 3,22")
start = [11, 2]
end = [21, 2]

print("Case 3: 0,0 to 24,24")
start = [0, 0]
end = [24, 24]

bfsQ = Queue()
dfsQ = LifoQueue()
aStarQ = []
heapq.heapify(aStarQ)

maze = Maze(mazeList, start, end)

# path = BFS(maze)
# path = DFS(maze)
path = aStarS(maze)

maze.printMaze()
print("Cost: ", maze.cost)
print("Nodes Visited: ", maze.nodesVisited())
print("Path: ", path)