def findAllDistances(locs: list[tuple[int, int]]) -> list[int]:
    dists = list()
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            dists.append(abs(locs[j][0] - locs[i][0]) + abs(locs[j][1] - locs[i][1]))
    return dists

def findEmptyRowsColumns(universe: list[str]) -> tuple[set[int], set[int]]:
    rows = set()
    cols = set()
    transpose = lambda x: ["".join([x[i][j] for i in range(len(x))]) for j in range(len(x[0]))]
    emptySpace = "." * len(universe[0])
    for i in range(len(universe)):
        if universe[i] == emptySpace:
            rows.add(i)
    universeT = transpose(universe)
    emptySpace = "." * len(universeT[0])
    for j in range(len(universeT)):
        if universeT[j] == emptySpace:
            cols.add(j)
    return rows, cols

def findExpandedGalaxies(universe: list[str], mult: int) -> list[tuple[int, int]]:
    emptyRows, emptyCols = findEmptyRowsColumns(universe)
    offsetX = 0
    locs = list()
    for i in range(len(universe)):
        if i in emptyRows:
            offsetX += 1
        offsetY = 0
        for j in range(len(universe[i])):
            if j in emptyCols:
                offsetY += 1
            if universe[i][j] == "#":
                locs.append((i + offsetX*mult,j + offsetY*mult))
    return locs


with open("data/input11.txt", "r") as file:
    txt = file.read().strip()

universe = txt.split("\n")
galaxies = findExpandedGalaxies(universe, 1)
dists = findAllDistances(galaxies)
print(sum(dists))

galaxies = findExpandedGalaxies(universe, 1e6 - 1)
dists = findAllDistances(galaxies)
print(sum(dists))