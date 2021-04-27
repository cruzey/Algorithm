from collections import deque

def bfs(x, y, arr):
    queue = deque()
    i = 0
    queue.append((x, y, arr[i]))

    dice = [[0] * 4 for _ in range(4)]

    # 동, 서, 북, 남
    move_types = {1 : (0, 1), 2 : (0, -1), 3 : (-1, 0), 4 : (1, 0)}

    while queue:
        x, y, order = queue.popleft()

        for move, value in move_types.items():
            if order == move:
                nx = x + value[0]
                ny = y + value[1]
                direction = move

        # print(nx, ny, direction)
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            if (i + 1) == len(arr):
                return
            else:
                i += 1
                queue.append((x, y, arr[i]))
            continue
        elif direction == 1:
            for j in range(3, -1, -1):
                if j == 3:
                    tmp = dice[1][j]
                else:
                    tmp2 = dice[1][j]
                    dice[1][j] = tmp 
                    tmp = tmp2
            dice[1][3] = tmp
            dice[3][1] = dice[1][3]
        elif direction == 2:
            for j in range(4):
                if j == 0:
                    tmp = dice[1][j]
                else:
                    tmp2 = dice[1][j]
                    dice[1][j] = tmp 
                    tmp = tmp2
            dice[1][0] = tmp
            dice[3][1] = dice[1][3]
        elif direction == 3:
            for j in range(4):
                if j == 0:
                    tmp = dice[j][1]
                else:
                    tmp2 = dice[j][1]
                    dice[j][1] = tmp 
                    tmp = tmp2
            dice[0][1] = tmp
            dice[1][3] = dice[3][1]
        elif direction == 4:
            for j in range(3, -1, -1):
                if j == 3:
                    tmp = dice[j][1]
                else:
                    tmp2 = dice[j][1]
                    dice[j][1] = tmp 
                    tmp = tmp2
            dice[3][1] = tmp
            dice[1][3] = dice[3][1]
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[1][1]
            print(dice[1][3])
            if (i + 1) == len(arr):
                return
            else:
                i += 1
                queue.append((nx, ny, arr[i]))
        else:
            dice[1][1] = graph[nx][ny]
            graph[nx][ny] = 0
            print(dice[1][3])
            if (i + 1) == len(arr):
                return
            else:
                i += 1
                queue.append((nx, ny, arr[i]))


n, m, x1, y1, num = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
order = list(map(int, input().split()))

result = bfs(x1, y1, order)


