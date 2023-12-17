def rollBoardNorth(board: list[list[str]]) -> list[list[str]]:
    newBoard = [["."]* len(board[-1]) for _ in range(len(board))]
    for i in range(len(board[-1])):
        top = 0
        for j in range(len(board)):
            if board[j][i] == "#":
                newBoard[j][i] = "#"
                top = j + 1
            if board[j][i] == "O":
                newBoard[top][i] = "O"
                top += 1
    return newBoard

with open("data/input14.txt", "r") as file:
    txt = file.read().strip()

board = [list(line) for line in txt.split("\n")]
newBoard = rollBoardNorth(board)

weights = [newBoard[i].count("O") * (len(newBoard) - i) for i in range(len(newBoard))]

print(sum(weights))
