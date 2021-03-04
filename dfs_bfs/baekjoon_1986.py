# 체스판에 퀸, 나이트, 폰들의 위치를 입력으로 받아 퀸과 나이트가 이동할 수 있는 칸을 제외한 안전한 칸을 출력
# 폰은 장애물의 역할만 한다

from collections import deque

def forqueen(x, y):
    queue = deque()

    # 8방향으로 움직일 수 있지만 한번 움직이면 그 방향으로만 계속 이동해야 하기에
    for i in range(8):
        # 방향당 처음 한번만 말의 위치를 넣어준다
        queue.append((x, y))

        while queue:
            xx, yy = queue.popleft()
            nx = xx + qx[i]
            ny = yy + qy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            
            # 갈 수 있는 곳이면 체크한 후 큐에 이동한 후의 자리 추가
            if graph[nx][ny] == 0 or graph[nx][ny] == "check":
                graph[nx][ny] = "check"
                queue.append((nx, ny))

    return 0

def forknight(x, y):
    queue = deque()

    for i in range(8):
        queue.append((x, y))
        
        while queue:
            xx, yy = queue.popleft()
            nx = xx + kx[i]
            ny = yy + ky[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break

            if graph[nx][ny] == 0:
                graph[nx][ny] = "check"

    return 0


n, m = map(int, input().split())
queens = list(map(int, input().split()))
knights = list(map(int, input().split()))
pawns = list(map(int, input().split()))

# 맵의 크기만큼 이차원 리스트 생성, 0으로 초기화
graph = [[0] * m for j in range(n)]


# 방향 for queens
qx = [-1, -1, -1, 0, 0, 1, 1, 1]
qy = [-1, 0, 1, -1, 1, -1, 0, 1] 

# 방향 for knights
kx = [-2, -2, -1, -1, 1, 1, 2, 2]
ky = [-1, 1, -2, 2, -2, 2, -1, 1]

# 생성한 맵에 말들을 입력
for i in range(1, len(pawns), 2):
    graph[pawns[i] - 1][pawns[i + 1] - 1] = "P"

for i in range(1, len(knights), 2):
    graph[knights[i] - 1][knights[i + 1] - 1] = "K"

for i in range(1, len(queens), 2):
    graph[queens[i] - 1][queens[i + 1] - 1] = "Q"

print(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] == "Q":
            forqueen(i, j)
        if graph[i][j] == "K":
            forknight(i, j)

print(graph)
result = 0

# 체크되지 않은 안전한 칸만 세어 출력
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1

print(result)