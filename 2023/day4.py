def clean_card(allCards: str):
    ret = []
    for card in allCards.split("\n"):
        nums = card.split(": ")[1].split(" | ")
        winNums = set(nums[0].split(" "))
        myNums = list(nums[1].split(" "))
        ret.append([winNums, myNums])
    return ret

def accumCards(cards):
    ret = [1]*len(cards)
    for i in range(len(ret)):
        numWon = len(list(filter(lambda x: x in cards[i][0], cards[i][1])))
        for j in range(i + 1, i + numWon + 1):
            ret[j] += ret[i]
    return ret

def calculate_points(winNum: set[str], myNums: list[str]):
    return 2**(len(list(filter(lambda x: x in winNum, myNums))) - 1)//1

with open("temp4.txt", "r") as file:
    allCards = file.read().replace("  ", " ").strip()

cards = clean_card(allCards)

points = list(map(lambda x: calculate_points(x[0], x[1]), cards))
print(sum(points))

print(sum(accumCards(cards)))