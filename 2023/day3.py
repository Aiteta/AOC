def isSurrounding(schema: list[str], i: int, j: int, N: int, M: int) -> bool:
    surrounding = []
    if i > 0:
        surrounding.append(schema[i - 1][j])
    if j > 0:
        surrounding.append(schema[i][j - 1])
    if i < N - 1:
        surrounding.append(schema[i + 1][j])
    if j < M -1:
        surrounding.append(schema[i][j + 1])
    if i > 0 and j > 0:
        surrounding.append(schema[i - 1][j - 1])
    if i > 0 and j < M - 1:
        surrounding.append(schema[i - 1][j + 1])
    if i < N - 1 and j > 0:
        surrounding.append(schema[i + 1][j - 1])
    if i < N - 1 and j < M - 1:
        surrounding.append(schema[i + 1][j + 1])
    
    symbols = filter(lambda x: not x.isnumeric() and x != ".", surrounding)
    return len(list(symbols)) > 0


def getPartLoc(schema: list[str], i: int, j: int, M: int) -> (int, int):
    while j > 0 and schema[i][j - 1].isnumeric():
        j -= 1
    part = 0
    while j < M and schema[i][j].isnumeric():
        part *= 10
        part += int(schema[i][j])
        j += 1
    return (part, j)


def findValidParts(schema: list[str]) -> list[int]:
    N = len(schema)
    M = len(schema[0])
    ret = []
    i = 0
    while i < N:
        j = 0
        while j < M:
            if schema[i][j].isnumeric() and isSurrounding(schema, i, j, N, M):
                partLoc = getPartLoc(schema, i, j, M)
                ret.append(partLoc[0])
                j = partLoc[1]
                continue
            j += 1
        i += 1
    return ret

def findAdjacentNumbers(schema: list[str], i: int, j: int, N: int, M: int) -> list[int]:
    parts = []

    if i > 0:
        if schema[i - 1][j].isnumeric():
            parts.append(getPartLoc(schema, i - 1, j, M)[0])
        else:
            if j > 0 and schema[i - 1][j - 1].isnumeric():
                parts.append(getPartLoc(schema, i - 1, j - 1, M)[0])
            if j < M - 1 and schema[i - 1][j + 1].isnumeric():
                parts.append(getPartLoc(schema, i - 1, j + 1, M)[0])
    if i < N - 1:
        if schema[i + 1][j].isnumeric():
            parts.append(getPartLoc(schema, i + 1, j, M)[0])
        else:
            if j > 0 and schema[i + 1][j - 1].isnumeric():
                parts.append(getPartLoc(schema, i + 1, j - 1, M)[0])
            if j < M - 1 and schema[i + 1][j + 1].isnumeric():
                parts.append(getPartLoc(schema, i + 1, j + 1, M)[0])
    
    if j > 0 and schema[i][j - 1].isnumeric():
        parts.append(getPartLoc(schema, i, j - 1, M)[0])

    if j < M - 1 and schema[i][j + 1].isnumeric():
        parts.append(getPartLoc(schema, i, j + 1, M)[0])

    return parts

def findAllGearRatio(schema: list[str]) -> list[int]:
    N = len(schema)
    M = len(schema[0])

    gearLocs = filter(lambda x: schema[x[0]][x[1]] == "*", [(i, j) for i in range(N) for j in range(M)])
    gearParts = map(lambda x: findAdjacentNumbers(schema, x[0], x[1], N, M), gearLocs)
    return list(map(lambda x: x[0] * x[1], filter(lambda x: len(x) == 2, gearParts)))


f = open("input3.txt")
schema = list(map(lambda x: x.strip(" \n"), f.readlines()))

partsList = findValidParts(schema)

print(f"Sum of Part Numbers: {sum(partsList)}")

gearRatios = findAllGearRatio(schema)

print(f"Sum of Gear Ratios: {sum(gearRatios)}")
