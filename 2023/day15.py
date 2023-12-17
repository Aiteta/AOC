def runHash(word: str) -> int:
    total = 0
    for char in word:
        total = ((total + ord(char)) * 17) % 256
    return total

def findBoxOperation(combo: str) -> tuple[str, int, bool]:
    label = -1
    if combo.count("-"):
        word = combo.split("-")[0]
        operation = False
    if combo.count("="):
        word = combo.split("=")[0]
        label = int(combo[-1])
        operation = True
    return word, label, operation

def runOperations(operations: list[tuple[str, int, bool]]) -> list[list[tuple[str, int]]]:
    boxes = [[] for _ in range(256)]
    for operation in operations:
        idx = runHash(operation[0])
        hasLabel = False
        for j in range(len(boxes[idx])):
            if operation[2] and boxes[idx][j][0] == operation[0]:
                boxes[idx][j][1] = operation[1]
                hasLabel = True
                break
            elif not operation[2] and boxes[idx][j][0] == operation[0]:
                boxes[idx].pop(j)
                break
        if operation[2] and not hasLabel:
            boxes[idx].append([operation[0], operation[1]])
    return boxes



with open("data/input15.txt") as file:
    txt = file.read().strip()

words = txt.split(",")
hashes = list(map(runHash, words))
print(sum(hashes))

operations = list(map(findBoxOperation, words))
boxes = runOperations(operations)
powers = [[(i + 1) * (j + 1) * boxes[i][j][1] for j in range(len(boxes[i]))] for i in range(len(boxes))]

print(sum(map(sum, powers)))