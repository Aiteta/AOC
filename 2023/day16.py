visited = set()

def shineLight(pos: tuple[int,int], dir: str, board: list[str], energy: list[list[int]]) -> None:
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(board) or pos[1] >= len(board[-1]):
        return
    if str(pos)+dir in visited:
        return
    visited.add(str(pos)+dir)
    if dir == "up":
        for i in range(pos[0], -1, -1):
            energy[i][pos[1]] += 1
            if board[i][pos[1]] == "\\":
                shineLight((i, pos[1] - 1), "left", board, energy)
                break
            elif board[i][pos[1]] == "/":
                shineLight((i, pos[1] + 1), "right", board, energy)
                break
            elif board[i][pos[1]] == "-":
                shineLight((i, pos[1] - 1), "left", board, energy)
                shineLight((i, pos[1] + 1), "right", board, energy)
                break
    elif dir == "down":
        for i in range(pos[0], len(board)):
            energy[i][pos[1]] += 1
            if board[i][pos[1]] == "\\":
                shineLight((i, pos[1] + 1), "right", board, energy)
                break
            elif board[i][pos[1]] == "/":
                shineLight((i, pos[1] - 1), "left", board, energy)
                break
            elif board[i][pos[1]] == "-":
                shineLight((i, pos[1] - 1), "left", board, energy)
                shineLight((i, pos[1] + 1), "right", board, energy)
                break
    elif dir == "left":
        for i in range(pos[1], -1, -1):
            energy[pos[0]][i] += 1
            if board[pos[0]][i] == "\\":
                shineLight((pos[0] - 1, i), "up", board, energy)
                break
            elif board[pos[0]][i] == "/":
                shineLight((pos[0] + 1, i), "down", board, energy)
                break
            elif board[pos[0]][i] == "|":
                shineLight((pos[0] - 1, i), "up", board, energy)
                shineLight((pos[0] + 1, i), "down", board, energy)
                break
    elif dir == "right":
        for i in range(pos[1], len(board[pos[1]])):
            energy[pos[0]][i] += 1
            if board[pos[0]][i] == "\\":
                shineLight((pos[0] + 1, i), "down", board, energy)
                break
            elif board[pos[0]][i] == "/":
                shineLight((pos[0] - 1, i), "up", board, energy)
                break
            elif board[pos[0]][i] == "|":
                shineLight((pos[0] - 1, i), "up", board, energy)
                shineLight((pos[0] + 1, i), "down", board, energy)
                break

def findMostLight(board: list[str]) -> int:
    maxi = 0
    for i in range(len(board)):
        energy = [[0] * len(board[-1]) for _ in board]
        visited.clear()
        shineLight([i, 0], "right", board, energy)
        maxi = max(maxi, sum(map(lambda x: sum(map(lambda y: y > 0, x)), energy)))
        energy = [[0] * len(board[-1]) for _ in board]
        visited.clear()
        shineLight([i, len(board[-1]) - 1], "left", board, energy)
        maxi = max(maxi, sum(map(lambda x: sum(map(lambda y: y > 0, x)), energy)))
    for i in range(len(board[-1])):
        energy = [[0] * len(board[-1]) for _ in board]
        visited.clear()
        shineLight([0, i], "down", board, energy)
        maxi = max(maxi, sum(map(lambda x: sum(map(lambda y: y > 0, x)), energy)))
        energy = [[0] * len(board[-1]) for _ in board]
        visited.clear()
        shineLight([len(board) - 1, i], "up", board, energy)
        maxi = max(maxi, sum(map(lambda x: sum(map(lambda y: y > 0, x)), energy)))
    return maxi

with open("data/input16.txt", "r") as file:
    txt = file.read().strip()

board = txt.split("\n")
energy = [[0] * len(board[-1]) for _ in board]

shineLight((0,0), "right", board, energy)

total = sum(map(lambda x: sum(map(lambda y: y > 0, x)), energy))
print(total)

print(findMostLight(board))
