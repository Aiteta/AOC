patternSeq2count = dict()

def createPatternSequence(lines: list[str]) -> tuple[list[str], list[list[int]]]:
    patterns = list()
    sequences = list()
    for line in lines:
        splitLine = line.split(" ")
        patterns.append(splitLine[0])
        sequences.append([int(val) for val in splitLine[1].split(",")])
    return patterns, sequences

def numMatches(pattern: str, sequence: list[int]) -> int:
    if not len(sequence):
        return 1 if not pattern.count("#") else 0
    if pattern + str(sequence) in patternSeq2count:
        return patternSeq2count[pattern + str(sequence)]
    count = 0
    for i in range(len(pattern) - len(sequence) - sum(sequence) + 2):
        if pattern[i-1:i] == "#":
            break
        if pattern[i:i + sequence[0]].count("."):
            continue
        if pattern[i + sequence[0]:i + sequence[0] + 1] == "#":
            continue
        count += numMatches(pattern[i + sequence[0] + 1:], sequence[1:])
    patternSeq2count[pattern + str(sequence)] = count
    return count

def unfoldPattern(pattern: str) -> str:
    ret = (pattern + "?") * 5
    return ret[:-1]


with open("data/input12.txt", "r") as file:
    txt = file.read().strip()

lines = txt.split("\n")
patterns, sequences = createPatternSequence(lines)
matches = [numMatches(patterns[i], sequences[i]) for i in range(len(patterns))]


newPatterns = list(map(unfoldPattern, patterns))
newSequences = list(map(lambda x: x * 5, sequences))
newMatches = [numMatches(newPatterns[i], newSequences[i]) for i in range(len(newPatterns))]
print(sum(newMatches))


