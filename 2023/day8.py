from functools import reduce
import math

def createGraph(txtLines: list[str]) -> dict[str, tuple[str, str]]:
    graph = dict()
    for line in txtLines:
        line = reduce(lambda x, y: x.replace(y, ""), [line, " ", "(", ")"])
        line = line.split("=")
        origin = line[0]
        sources = line[1].split(",")
        graph[origin] = tuple(sources)
    return graph

def findNumSteps(instructions: list[int], graph: dict[str, tuple[str, str]], start: str, end: str) -> int:
    steps = 0
    N = len(instructions)
    curr = start
    while curr != end and steps < 1e5:
        curr = graph[curr][instructions[steps % N]]
        steps = steps + 1
    return steps

def findStartsEnds(graph: dict[str, tuple[str, str]]) -> tuple[list[str], list[str]]:
    locs = graph.keys()
    starts = list(filter(lambda x: x[2] == "A", locs))
    ends = list(filter(lambda x: x[2] == "Z", locs))

    return (starts, ends)

def findAllDist(instructions: list[int], graph: dict[str, tuple[str, str]], starts: list[str], ends: list[str]) -> dict[str, dict[str, int]]:
    allDist = dict()
    for start in starts:
        allDist[start] = dict()
        for end in ends:
            allDist[start][end] = findNumSteps(instructions, graph, start, end)
    return allDist


def findMinComb(allDist: dict[str, dict[str, int]]) -> int:
    minDist = 1
    print(allDist)
    for start in allDist:
        for end in allDist[start]:
            if allDist[start][end] == 1e5:
                continue
            minDist = math.lcm(minDist, allDist[start][end])
    return minDist

with open("data/input8.txt") as file:
    txt = file.read().strip()

txtLines = txt.split("\n")
instructions = txtLines.pop(0).strip().replace("L","0").replace("R","1")
instructions = list(map(int, instructions))

txtLines.pop(0)
graph = createGraph(txtLines)
steps = findNumSteps(instructions, graph, "AAA", "ZZZ")
print(steps)

(starts, ends) = findStartsEnds(graph)
allDist = findAllDist(instructions, graph, starts, ends)
print(findMinComb(allDist))

