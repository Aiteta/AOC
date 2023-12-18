import heapq

class Node(object):
    def __init__(this, position, direction, heatloss):
        this.position = position
        this.direction = direction
        this.heatloss = heatloss

    def __lt__(this, other):
        return this.heatloss < other.heatloss

def fake_dijkstra(board: list[list[int]]) -> int:
    visited = [[{"left": -1, "right": -1, "up": -1, "down": -1} for _ in range(len(line))] for line in board]
    heap = []
    heatLosses = [[-1] * len(board[-1]) for _ in board]
    heatLosses[0][0] = 0
    heapq.heappush(heap, Node((0,1), "right", 0))
    heapq.heappush(heap, Node((1,0), "down", 0))
    while len(heap):
        node = heapq.heappop(heap)
        pos = node.position
        hl = node.heatloss
        dir = node.direction
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(board) or pos[1] >= len(board[-1]):
            continue
        hl_prev = visited[pos[0]][pos[1]][dir]
        if hl_prev != -1 and hl_prev <= hl:
            continue
        visited[pos[0]][pos[1]][dir] = hl
        print(hl, pos, dir)
        if dir == "left":
            for i in range(pos[1], max(pos[1] - 3, -1), -1):
                if heatLosses[pos[0]][i] == -1 or hl < heatLosses[pos[0]][i]:
                    heatLosses[pos[0]][i] = hl
                hl += board[pos[0]][i]
                heapq.heappush(heap, Node((pos[0] - 1, i), "up", hl))
                heapq.heappush(heap, Node((pos[0] + 1, i), "down", hl))
        elif dir == "right":
            for i in range(pos[1], min(pos[1] + 3, len(board[-1]))):
                if heatLosses[pos[0]][i] == -1 or hl < heatLosses[pos[0]][i]:
                    heatLosses[pos[0]][i] = hl
                hl += board[pos[0]][i]
                heapq.heappush(heap, Node((pos[0] - 1, i), "up", hl))
                heapq.heappush(heap, Node((pos[0] + 1, i), "down", hl))
        elif dir == "up":
            for i in range(pos[0], max(pos[0] - 3, -1), -1):
                if heatLosses[i][pos[1]] == -1 or hl < heatLosses[i][pos[1]]:
                    heatLosses[i][pos[1]] = hl
                hl += board[i][pos[1]]
                heapq.heappush(heap, Node((i, pos[1] - 1), "left", hl))
                heapq.heappush(heap, Node((i, pos[1] + 1), "right", hl))
        elif dir == "down":
            for i in range(pos[0], min(pos[0] + 3, len(board[-1]))):
                if heatLosses[i][pos[1]] == -1 or hl < heatLosses[i][pos[1]]:
                    heatLosses[i][pos[1]] = hl
                hl += board[i][pos[1]]
                heapq.heappush(heap, Node((i, pos[1] - 1), "left", hl))
                heapq.heappush(heap, Node((i, pos[1] + 1), "right", hl))
    return heatLosses[-1][-1] + board[-1][-1]

def fake_dijkstra2(board: list[list[int]]) -> int:
    visited = [[{"left": -1, "right": -1, "up": -1, "down": -1} for _ in range(len(line))] for line in board]
    heap = []
    heatLosses = [[-1] * len(board[-1]) for _ in board]
    heatLosses[0][0] = 0
    heapq.heappush(heap, Node((0,1), "right", 0))
    heapq.heappush(heap, Node((1,0), "down", 0))
    while len(heap):
        node = heapq.heappop(heap)
        pos = node.position
        hl = node.heatloss
        dir = node.direction
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(board) or pos[1] >= len(board[-1]):
            continue
        hl_prev = visited[pos[0]][pos[1]][dir]
        if hl_prev != -1 and hl_prev <= hl:
            continue
        visited[pos[0]][pos[1]][dir] = hl
        if dir == "left":
            start1 = pos[1]
            start2 = max(pos[1] - 3, -1)
            end2 = max(pos[1] - 10, -1)
            for i in range(start1, start2, -1):
                hl += board[pos[0]][i]
            for i in range(start2, end2, -1):
                if heatLosses[pos[0]][i] == -1 or hl < heatLosses[pos[0]][i]:
                    heatLosses[pos[0]][i] = hl
                hl += board[pos[0]][i]
                heapq.heappush(heap, Node((pos[0] - 1, i), "up", hl))
                heapq.heappush(heap, Node((pos[0] + 1, i), "down", hl))
        elif dir == "right":
            start1 = pos[1]
            start2 = min(pos[1] + 3, len(board[-1]))
            end2 = min(pos[1] + 10, len(board[-1]))
            for i in range(start1, start2):
                hl += board[pos[0]][i]
            for i in range(start2, end2):
                if heatLosses[pos[0]][i] == -1 or hl < heatLosses[pos[0]][i]:
                    heatLosses[pos[0]][i] = hl
                hl += board[pos[0]][i]
                heapq.heappush(heap, Node((pos[0] - 1, i), "up", hl))
                heapq.heappush(heap, Node((pos[0] + 1, i), "down", hl))
        elif dir == "up":
            start1 = pos[0]
            start2 = max(pos[0] - 3, -1)
            end2 = max(pos[0] - 10, -1)
            for i in range(start1, start2, -1):
                hl += board[i][pos[1]]
            for i in range(start2, end2, -1):
                if heatLosses[i][pos[1]] == -1 or hl < heatLosses[i][pos[1]]:
                    heatLosses[i][pos[1]] = hl
                hl += board[i][pos[1]]
                heapq.heappush(heap, Node((i, pos[1] - 1), "left", hl))
                heapq.heappush(heap, Node((i, pos[1] + 1), "right", hl))
        elif dir == "down":
            start1 = pos[0]
            start2 = min(pos[0] + 3, len(board))
            end2 = min(pos[0] + 10, len(board))
            for i in range(start1, start2):
                hl += board[i][pos[1]]
            for i in range(start2, end2):
                if heatLosses[i][pos[1]] == -1 or hl < heatLosses[i][pos[1]]:
                    heatLosses[i][pos[1]] = hl
                hl += board[i][pos[1]]
                heapq.heappush(heap, Node((i, pos[1] - 1), "left", hl))
                heapq.heappush(heap, Node((i, pos[1] + 1), "right", hl))
    return heatLosses[-1][-1] + board[-1][-1]

with open("data/input17.txt", "r") as file:
    txt = file.read().strip()

board = [[int(char) for char in line] for line in txt.split("\n")]

print(fake_dijkstra2(board))