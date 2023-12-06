def getInitSeeds(txt_lines: list[str]) -> list[int]:
    firstLine = txt_lines[0]
    firstLine = firstLine.split(":")
    assert(firstLine[0] == "seeds")
    seeds = firstLine[1].strip().split(" ")
    return list(map(int, seeds))

def getParamMap(txt_lines: list[str]) -> list[dict[int, tuple[int, int]]]:
    paramMapList = []
    for i in range(1, len(txt_lines)):
        param = txt_lines[i].split("\n")
        paramMap = {}
        for j in range(1, len(param)):
            nums = param[j].split(" ")
            paramMap[int(nums[1])] = (int(nums[2]), int(nums[0]))
        paramMapList.append(paramMap)
    return paramMapList

def findNext(val: int, paramMap: dict[int, tuple[int, int]]) -> int:
    ret = val
    for key in sorted(paramMap.keys()):
        if val < key:
            continue
        if val < key + paramMap[key][0]:
            ret = paramMap[key][1] + val - key
            break
    return ret

def findLocation(seeds: list[int], paramMapList: list[dict[int, tuple[int, int]]]) -> list[int]:
    ret = seeds.copy()
    for paramMap in paramMapList:
        ret = list(map(lambda x: findNext(x, paramMap), ret))
    return list(ret)

def findNextPair(val: int, rangeVal: int, paramMap: dict[int, tuple[int, int]]) -> list[int]:
    ret = val
    retRange = rangeVal
    for key in sorted(paramMap.keys()):
        if val + rangeVal <= key:
            continue
        if val < key:
            ret = val
            retRange = rangeVal - (key - val)
            # print(val, rangeVal, key, paramMap[key], ret, retRange)
            break
        elif val >= key and val < key + paramMap[key][0]:
            ret = paramMap[key][1] + val - key
            retRange = min(rangeVal, paramMap[key][0] - (val - key))
            # print(val, rangeVal, key, paramMap[key], ret, retRange)
            break
    return [ret, retRange, val + retRange, rangeVal - retRange]

def findLocationPairs(seeds: list[int], paramMapList: list[dict[int, tuple[int, int]]]) -> list[int]:
    ret = seeds.copy()
    # print(ret)
    for paramMap in paramMapList:
        newRet = []
        for i in range(0, len(ret), 2):
            pairRange = ret[i:i+2]
            while pairRange[1] != 0:
                nextInfo = findNextPair(pairRange[0], pairRange[1], paramMap)
                # print(nextInfo)
                newRet.append(nextInfo[0])
                newRet.append(nextInfo[1])
                pairRange = nextInfo[2:4]
        ret = newRet
        # print(newRet)
    return ret



with open("input5.txt", "r") as file:
    txt = file.read().strip()

txt_lines = txt.split("\n\n")

seeds = getInitSeeds(txt_lines)
paramMapList = getParamMap(txt_lines)

locations = findLocation(seeds, paramMapList)

print(min(locations))

locations = findLocationPairs(seeds, paramMapList)

print(min(locations[0:len(locations):2]))