import collections

def printBoard(board: list):
    for line in board:
        string = ""
        for val in line:
            if isinstance(val, str):
                string += "."
            else:
                string += str(val%10)
        print(string)
    print()


def findStart(graph: list[str]) -> tuple[int, int]:
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "S":
                return (i, j)
    raise Exception

def findNextPosition(graph: list[str], pos: tuple[int, int]) -> list[tuple[int, int]]:
    symb = graph[pos[0]][pos[1]]
    ret = []
    if symb == "S":
        ret = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
               (pos[0], pos[1] + 1), (pos[0], pos[1] - 1),
               pos]
    elif symb == "F":
        ret = [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1)]
    elif symb == "7":
        ret = [(pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)]
    elif symb == "J":
        ret = [(pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]
    elif symb == "L":
        ret = [(pos[0] - 1, pos[1]), (pos[0], pos[1] + 1)]
    elif symb == "-":
        ret = [(pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    elif symb == "|":
        ret = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1])]

    N = len(graph)
    M = len(graph[0])
    isWithin = lambda pos: 0 <= pos[0] and pos[0] < N and \
                           0 <= pos[1] and pos[1] < M
    return list(filter(isWithin, ret))

def findHalfLoopDist(graph: list[str]) -> tuple[int, list[str]]:
    start = findStart(graph)
    board = [list(line) for line in graph]
    bfsQueue = collections.deque()
    bfsQueue.append((start, start, 0))
    while len(bfsQueue):
        (pos, prev, steps) = bfsQueue.popleft()
        if isinstance(board[pos[0]][pos[1]], int):
            printBoard(board)
            return (steps, board)

        newPos = findNextPosition(graph, pos)
        if not prev in newPos:
            continue
        board[pos[0]][pos[1]] = steps
        newPos = list(filter(lambda x: x != prev, newPos))
        for i in range(len(newPos)):
            if graph[newPos[i][0]][newPos[i][1]] == ".":
                continue
            bfsQueue.append((newPos[i], pos, steps + 1))
    raise Exception

def replaceStartPipe(graph: list[str], board: list) -> None:
    pos = findStart(graph)
    nextPos = findNextPosition(graph, pos)
    firstStep = list(filter(lambda x: board[x[0]][x[1]] == 1, nextPos))
    firstDiff = list(map(lambda x: (x[0] - pos[0], x[1] - pos[1]), firstStep))
    if (1, 0) in firstDiff and (0, 1) in firstDiff:
        symb = "F"
    if (1, 0) in firstDiff and (0, -1) in firstDiff:
        symb = "7"
    if (-1, 0) in firstDiff and (0, 1) in firstDiff:
        symb = "J"
    if (-1, 0) in firstDiff and (0, -1) in firstDiff:
        symb = "L"
    if (1, 0) in firstDiff and (-1, 0) in firstDiff:
        symb = "|"
    if (0, 1) in firstDiff and (0, -1) in firstDiff:
        symb = "-"
    graph[pos[0]] = graph[pos[0]][0:pos[1]] + symb + graph[pos[0]][pos[1] + 1:]

def augmentGraph(graph: list[str], board: list) -> list[str]:
    N = 2 * len(graph) + 1
    M = 2 * len(graph[0]) + 1
    augGraph = [["."] * M for _ in range(N)]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if isinstance(board[i][j], str):
                continue
            idx = 2 * i + 1
            jdx = 2 * j + 1
            augGraph[idx][jdx] = "+"
            symb = graph[i][j]
            if symb == "F":
                augGraph[idx + 1][jdx] = "|"
                augGraph[idx][jdx + 1] = "-"
            elif symb == "7":
                augGraph[idx + 1][jdx] = "|"
                augGraph[idx][jdx - 1] = "-"
            elif symb == "J":
                augGraph[idx - 1][jdx] = "|"
                augGraph[idx][jdx - 1] = "-"
            elif symb == "L":
                augGraph[idx - 1][jdx] = "|"
                augGraph[idx][jdx + 1] = "-"
            elif symb == "-":
                augGraph[idx][jdx + 1] = "-"
                augGraph[idx][jdx - 1] = "-"
            elif symb == "|":
                augGraph[idx + 1][jdx] = "|"
                augGraph[idx + 1][jdx] = "|"
    return augGraph

def floodGraph(board: list[str]) -> list[str]:
    floodGraph = [list(line) for line in board]
    start = (0,0)
    bfsQueue = collections.deque()
    bfsQueue.append(start)
    N = len(floodGraph)
    M = len(floodGraph[0])
    isWithin = lambda x: 0 <= x[0] and x[0] < N and \
                         0 <= x[1] and x[1] < M
    while len(bfsQueue):
        pos = bfsQueue.popleft()
        if floodGraph[pos[0]][pos[1]] != ".":
            continue
        floodGraph[pos[0]][pos[1]] = "O"
        newPos = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
                  (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
        newPos = list(filter(isWithin, newPos))
        for i in range(len(newPos)):
            bfsQueue.append(newPos[i])
    return floodGraph

def countDrySpots(augFloodGraph: list[list[str]]) -> int:
    count = 0
    for i in range(1, len(augFloodGraph), 2):
        for j in range(1, len(augFloodGraph[i]), 2):
            if augFloodGraph[i][j] == ".":
                count += 1
    return count


with open("data/input10.txt") as file:
    txt = file.read().strip()

graph = txt.split("\n")

(steps, board) = findHalfLoopDist(graph)
print(steps)
replaceStartPipe(graph, board)

augGraph = augmentGraph(graph, board)
augFloodGraph = floodGraph(augGraph)

print(countDrySpots(augFloodGraph))

