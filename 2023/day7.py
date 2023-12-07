def modifyJoker(hand: str, cardCount: dict[str,int]) -> str:
    if not "J" in cardCount:
        return hand
    numJoker = cardCount["J"]

    if hand == "highcard":
        hand = "onepair"
    elif hand == "onepair":
        hand = "threeofakind"
    elif hand == "twopair":
        hand = "fullhouse"
        if numJoker == 2:
            hand = "fourofakind"
    elif hand == "threeofakind":
        hand = "fourofakind"
    elif hand == "fullhouse":
        hand = "fiveofakind"
    elif hand == "fourofakind":
        hand = "fiveofakind"
    return hand

def classifyHand(cards: str, joker: bool = False) -> str:
    cardCount = {}
    for c in cards:
        if not c in cardCount:
            cardCount[c] = 1
        else:
            cardCount[c] += 1
    N = len(cardCount)

    hand = "fiveofakind"
    if N == 5:
        hand = "highcard"
    elif N == 4:
        hand = "onepair"
    elif N == 3:
        if max(cardCount.values()) == 2:
            hand = "twopair"
        else:
            hand = "threeofakind"
    elif N == 2:
        if max(cardCount.values()) == 3:
            hand = "fullhouse"
        else:
            hand = "fourofakind"

    if joker:
        hand = modifyJoker(hand, cardCount)

    return hand


class Hand(object):
    def __init__(self, cards: str, value: int, joker: bool = False):
        self.Cards = cards
        self.Value = value
        self.Type = classifyHand(cards, joker)

        cardsTypes = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        if joker:
            cardsTypes = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
        handsTypes = ["highcard", "onepair", "twopair", "threeofakind", "fullhouse", "fourofakind", "fiveofakind"]
        self._cardReference = {cardsTypes[i]: i for i in range(len(cardsTypes))}
        self._handReference = {handsTypes[i]: i for i in range(len(handsTypes))}

    def __lt__(self, other) -> bool:
        if self._handReference[self.Type] == self._handReference[other.Type]:
            for i in range(len(self.Cards)):
                if self._cardReference[self.Cards[i]] == self._cardReference[other.Cards[i]]:
                    continue
                return self._cardReference[self.Cards[i]] < self._cardReference[other.Cards[i]]
            raise Exception
        return self._handReference[self.Type] < self._handReference[other.Type]

with open("data/temp7.txt", "r") as file:
    txt = file.read().strip()

lines = txt.split("\n")
hands = list(map(lambda x: Hand(x[0], int(x[1])), [line.split(" ") for line in lines]))

sortedValues = list(map(lambda x: x.Value, sorted(hands)))

total = sum(map(lambda x: (x + 1) * sortedValues[x], range(len(sortedValues))))

print(total)

hands = list(map(lambda x: Hand(x[0], int(x[1]), True), [line.split(" ") for line in lines]))
sortedValues = list(map(lambda x: x.Value, sorted(hands)))

total = sum(map(lambda x: (x + 1) * sortedValues[x], range(len(sortedValues))))

print(total)
