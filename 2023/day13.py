def isReflection(pattern1: list[str], pattern2: list[str]) -> bool:
    N = min(len(pattern1), len(pattern2))
    for i in range(N):
        if pattern1[i + len(pattern1) - N] != pattern2[N - i - 1]:
            return False
    return True

def isSmudgeReflection(pattern1: list[str], pattern2: list[str]) -> bool:
    N = min(len(pattern1), len(pattern2))
    diff = 0
    for i in range(N):
        str1 = pattern1[i + len(pattern1) - N]
        str2 = pattern2[N - i - 1]
        for j in range(len(str1)):
            diff += str1[j] != str2[j]
    return diff == 1

def findReflections(pattern: list[str]) -> int:
    pattern_T = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0]))]
    pattern_T = list(map(lambda x: "".join(x), pattern_T))

    hori = list()
    for i in range(len(pattern_T) - 1):
        if isReflection(pattern_T[0:i+1], pattern_T[i+1:]):
            hori.append(i)

    vert = list()
    for i in range(len(pattern) - 1):
        if isReflection(pattern[0:i+1], pattern[i+1:]):
            vert.append(i)

    return hori, vert

def findSmudgeReflections(pattern: list[str]) -> int:
    pattern_T = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0]))]
    pattern_T = list(map(lambda x: "".join(x), pattern_T))

    hori = list()
    for i in range(len(pattern_T) - 1):
        if isSmudgeReflection(pattern_T[0:i+1], pattern_T[i+1:]):
            hori.append(i)

    vert = list()
    for i in range(len(pattern) - 1):
        if isSmudgeReflection(pattern[0:i+1], pattern[i+1:]):
            vert.append(i)

    return hori, vert



with open("data/input13.txt", "r") as file:
    txt = file.read().strip()

patterns = [line.strip().split("\n") for line in txt.split("\n\n")]
reflections = [findReflections(pattern) for pattern in patterns]

total = 0
for mirror in reflections:
    total += sum(mirror[0]) + len(mirror[0]) + (sum(mirror[1]) + len(mirror[1])) * 100

print(total)

smudgeReflections = [findSmudgeReflections(pattern) for pattern in patterns]

smudgeTotal = 0
for mirror in smudgeReflections:
    smudgeTotal += sum(mirror[0]) + len(mirror[0]) + (sum(mirror[1]) + len(mirror[1])) * 100

print(smudgeTotal)