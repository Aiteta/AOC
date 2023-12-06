import math
from functools import reduce

def findMinMaxHoldTime(time: int, dist: int) -> tuple[int, int]:
    dist += 1
    det = math.sqrt(time**2 - 4*dist)
    return (math.ceil(0.5*(time - det)), math.floor(0.5*(time + det)))

with open("input6.txt", "r") as file:
    txt = file.read().strip()

info = [list(map(lambda x: int(x), filter(lambda x: len(x) != 0, line.split(":")[1].split(" ")))) for line in txt.split("\n")]
timeRanges = [findMinMaxHoldTime(info[0][i], info[1][i]) for i in range(len(info[0]))]
margins = list(map(lambda x: x[1] - x[0] + 1, timeRanges))

print(reduce(lambda x, y: x * y, margins))

newInfo = [int(line.split(":")[1]) for line in txt.replace(" ", "").split("\n")]
timeRange = findMinMaxHoldTime(newInfo[0], newInfo[1])
margin = timeRange[1] - timeRange[0] + 1

print(margin)
