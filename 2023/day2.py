from functools import reduce

def getCubes(rounds: list[str]) -> list[list[int]]:
    colors = {"red": 0, "green": 1, "blue": 2}
    gameStat = []
    for round in rounds:
        stat = [0, 0, 0]
        cubes = round.split(",")
        for cube in cubes:
            cubeNum = cube.strip().split(" ")
            stat[colors[cubeNum[1]]] = int(cubeNum[0])
        gameStat.append(stat)
    return gameStat

def getStats(txt: list[str]) -> list[list[list[int]]]:
    stats = []
    for game in txt:
        game = game.split(":")[1].strip()
        rounds = game.split(";")
        gameStat = getCubes(rounds)
        stats.append(gameStat)
    return stats

def isValid(gameStat: list[list[int]]) -> bool:
    maxes = [12, 13, 14]
    for round in gameStat:
        for i in range(len(maxes)):
            if maxes[i] < round[i]:
                return False
    return True

def findRoundPower(gameStat):
    numColors = [[round[i] for round in gameStat] for i in range(len(gameStat[0]))]
    minNeeded = map(max,numColors)
    return reduce(lambda x, y: x * y, minNeeded)


f = open("input2.txt")

txt = f.readlines()
stats = getStats(txt)

validRounds = [i+1 if isValid(stats[i]) else 0 for i in range(len(stats))]

print(f"Sum of IDs: {sum(validRounds)}")

powers = [findRoundPower(gameStat) for gameStat in stats]

print(f"Sum of Powers: {sum(powers)}")