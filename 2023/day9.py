def findMultipleTree(seq: list[int]) -> list[list[int]]:
    tree = [seq.copy()]
    for _ in range(len(seq)):
        tree.append([])
        isPoly = True
        for j in range(len(tree[-2]) - 1):
            tree[-1].append(tree[-2][j + 1] - tree[-2][j])
            if tree[-1][0] != tree[-1][j]:
                isPoly = False
        if isPoly:
            break
    return tree

def findNextSeq(tree: list[list[int]]) -> int:
    nextVal = tree[-1][-1]
    for i in range(len(tree) - 2, -1, -1):
        nextVal = tree[i][-1] + nextVal
    return nextVal

def findPrevSeq(tree: list[list[int]]) -> int:
    prevVal = tree[-1][0]
    for i in range(len(tree) - 2, -1, -1):
        prevVal = tree[i][0] - prevVal
    return prevVal

with open("data/input9.txt") as file:
    txt = file.read().strip()

seqTxt = [line.split(" ") for line in txt.split("\n")]
seq = [list(map(int, line)) for line in seqTxt]

trees = list(map(lambda x: findMultipleTree(x), seq))
nextVals = list(map(lambda x: findNextSeq(x), trees))
prevVals = list(map(lambda x: findPrevSeq(x), trees))

print(sum(nextVals))
print(sum(prevVals))
