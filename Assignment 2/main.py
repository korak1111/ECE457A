# Cyrus Rupa 2021 for ECE457A A#2

import numpy as py
import queue as queue
import copy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def case_Zero(maze):
    tempMaze = copy.deepcopy(maze)
    tempMaze[6][5] = "S"
    tempMaze[0][5] = "E"
    start = [6, 5]
    # end = [19, 23]
    print_maze(tempMaze)
    print("Case 0 S:(5,6) to E:(5,0)")
    solve_BFS(tempMaze, start)
    return


def case_one(maze):
    tempMaze = copy.deepcopy(maze)
    tempMaze[11][2] = "S"
    tempMaze[19][23] = "E"
    print_maze(tempMaze)
    start = [11, 2]
    end = [19, 23]
    print("Case 1 S:(3,12) to E:(24,20)")
    solve_BFS(tempMaze, start)
    return


def case_Two(maze):
    tempMaze = copy.deepcopy(maze)
    tempMaze[11][2] = "S"
    tempMaze[21][2] = "E"
    start = [11, 2]
    end = [21, 2]
    print("Case 2: 3,12 to 3,22")

    return


def case_Three(maze):
    tempMaze = copy.deepcopy(maze)
    tempMaze[0][0] = "S"
    tempMaze[24][24] = "E"
    start = [0, 0]
    end = [24, 24]
    print("Case 3: 0,0 to 24,24")
    solve_BFS(tempMaze, start)

    return tempMaze


def solve_BFS(maze, start):
    nums = queue.Queue()
    nums.put("")
    add = ""
    while not findEnd(maze, add, start):
        add = nums.get()
        for i in ["L", "R", "U", "D"]:
            put = add + i
            if validMove(maze, put, start):
                nums.put(put)


def findEnd(maze, moves, start):
    i = start[0]
    j = start[1]
    # print(moves)
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j += 1
        elif move == "D":
            j -= 1
    if maze[j][i] == "E":
        print("Found it!:" + moves)
        maze = addPath(maze, moves, start)
        print_maze(maze)
        return True


def validMove(maze, moves, start):
    i = start[0]
    j = start[1]

    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j += 1
        elif move == "D":
            j -= 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
    return True


def addPath(maze, moves, start):
    i = start[0]
    j = start[1]
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j += 1
        elif move == "D":
            j -= 1
        maze[j][i] = "X"
    return maze


def print_maze(maze):
    temp = []
    for j in range(len(maze[0])):
        temp.append(str(j))
    print(temp)


    for i in range(len(maze) - 1, -1, -1):
        temp = []
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                temp.append("S")
            elif maze[i][j] == "E":
                temp.append("E")
            elif maze[i][j] == "X":
                temp.append("X")
            elif maze[i][j] == 0 or maze[i][j]==" ":
                temp.append(" ")
            elif maze[i][j] == 1 or maze[i][j] == "#":
                temp.append("#")
        print(temp, i)


def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", " ", "#"])
    return maze


def main():
    # do a thing
    maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
             [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]
    maze2 = createMaze()
    case_Zero(maze2)
    # case_one(maze1)
    # case_Two(maze1)
    # case_Three(maze1)

    return 1


if __name__ == '__main__':
    print_hi("Cyrus")
    main()
