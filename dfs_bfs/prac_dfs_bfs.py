# dfs, bfs 연습

# from collections import deque

# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
    
#     return graph[r-1][c-1]

# r, c = map(int, input().split(" "))
# graph = []
# for i in range(r):
#     graph.append(list(map(int, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# print(bfs(0, 0))

# 만들수 있는 아이스크림 갯수 구하기
# 벽은 1로 빈 공간은 0으로 되어 있으며 액체를 부었을때 인접한 0끼리는 하나의 아이스크림이 된다
# 풀이 : 모든 공간을 탐색해서 0인 공간을 만나면 카운트하고 인접한 모든 0을 1로 바꾼다
# def dfs(x, y):
#     # 벽일 경우
#     if x <= -1 or x >= r or y <= -1 or y >= c:
#         return False
#     # 빈 공간일 경우
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#     # 아이스크림 틀일 경우 (x, y == 1)
#     return False

# r, c = map(int, input().split(" "))
# graph = []
# result = 0
# for i in range(r):
#     graph.append(list(map(int, input())))

# for i in range(r):
#     for j in range(c):
#         if dfs(i, j) == True:
#             result += 1

# print(result)

# 1, 1 에서 r, c까지 이동 가능한 경로를 따라서 도착하는 최소한의 경우의 수 찾기
# 0은 이동 불가 1만 이동 가능
# 풀이 : 1, 1에서 시작하여 상하좌우를 살피며 1을 만나면 지금까지 온 횟수에 1을 더하여 갱신하기
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 패스
            if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
                continue
            # 길이 없으면 패스
            if graph[nx][ny] == 0:
                continue
            # 처음으로 탐색한 길을 만나면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[r-1][c-1]

r, c = map(int, input().split(" "))
graph = []
for i in range(r):
    graph.append(list(map(int, input())))

# 방향 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))