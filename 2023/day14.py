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

def rollBoardSouth(board: list[list[str]]) -> list[list[str]]:
    newBoard = [["."]* len(board[-1]) for _ in range(len(board))]
    for i in range(len(board[-1])):
        bottom =  len(board) - 1
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] == "#":
                newBoard[j][i] = "#"
                bottom = j - 1
            if board[j][i] == "O":
                newBoard[bottom][i] = "O"
                bottom -= 1
    return newBoard

def rollBoardEast(board: list[list[str]]) -> list[list[str]]:
    newBoard = [["."]* len(board[-1]) for _ in range(len(board))]
    for i in range(len(board)):
        right =  len(board[i]) - 1
        for j in range(len(board[i]) - 1, -1, -1):
            if board[i][j] == "#":
                newBoard[i][j] = "#"
                right = j - 1
            if board[i][j] == "O":
                newBoard[i][right] = "O"
                right -= 1
    return newBoard

def rollBoardWest(board: list[list[str]]) -> list[list[str]]:
    newBoard = [["."]* len(board[-1]) for _ in range(len(board))]
    for i in range(len(board)):
        left =  0
        for j in range(len(board[i])):
            if board[i][j] == "#":
                newBoard[i][j] = "#"
                left = j + 1
            if board[i][j] == "O":
                newBoard[i][left] = "O"
                left += 1
    return newBoard

def loop(board: list[list[str]], N: int) -> list[list[str]]:
    preLoop = [[char for char in line]for line in board]
    visited = dict()
    for i in range(N):
        postLoop = rollBoardNorth(preLoop)
        postLoop = rollBoardWest(postLoop)
        postLoop = rollBoardSouth(postLoop)
        postLoop = rollBoardEast(postLoop)
        if str(postLoop) in visited:
            newN = i - visited[str(postLoop)]
            break
        visited[str(postLoop)] = i
        preLoop = postLoop
    for i in range((N - visited[str(postLoop)]) % newN - 1):
        postLoop = rollBoardNorth(postLoop)
        postLoop = rollBoardWest(postLoop)
        postLoop = rollBoardSouth(postLoop)
        postLoop = rollBoardEast(postLoop)
    return postLoop
    

with open("data/input14.txt", "r") as file:
    txt = file.read().strip()

board = [list(line) for line in txt.split("\n")]
newBoard = rollBoardNorth(board)

weights = [newBoard[i].count("O") * (len(newBoard) - i) for i in range(len(newBoard))]

print(sum(weights))

loopedBoard = loop(board, 1000000000)
weights = [loopedBoard[i].count("O") * (len(loopedBoard) - i) for i in range(len(loopedBoard))]

print(sum(weights))
# [print("".join(line)) for line in loopedBoard]
