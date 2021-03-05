# 적록색약 맵을 입력으로 받아 일반인과 색약인 사람이 각각 읽어내는 구획의 수를 구하시오
# 일반인은 빨, 초, 파 구획을 구분, 색약은 빨, 초를 하나로 생각

from collections import deque

# def dfs(x, y, cnt):
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False

#     if graph[x][y] == cnt and visited[x][y] == False:
#         visited[x][y] = True
#         dfs(x-1, y, cnt)
#         dfs(x+1, y, cnt)
#         dfs(x, y-1, cnt)
#         dfs(x, y+1, cnt)
#         return True
#     return False

def bfs(x, y, cnt):
    # 이미 방문처리 되었으면 패스
    if visited[x][y] == True:
        return False
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + qx[i]
            ny = y + qy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue

            # 인접한 곳이 시작된 색과 같다면 방문처리 후 큐에 추가
            if graph[nx][ny] == cnt and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return True

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

# 방향
qx = [-1, 1, 0, 0]
qy = [0, 0, -1, 1]

result_normal = 0
result_colorweakness = 0

visited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        # 현재 맵의 위치의 색을 인자로 넘겨줌
        cnt = graph[i][j]
        # if dfs(i, j, cnt) == True:
        #     result_normal += 1
        if bfs(i, j, cnt) == True:
            result_normal += 1


for i in range(n):
    for j in range(n):
        # 색약을 이해 빨, 초를 하나로 합침
        if graph[i][j] == "G":
            graph[i][j] = "R"


visited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        cnt = graph[i][j]
        # if dfs(i, j, cnt) == True:
        #     result_colorweakness += 1
        if bfs(i, j, cnt) == True:
            result_colorweakness += 1


print("{} {}".format(result_normal, result_colorweakness))

# dfs로 재귀함수의 형태로 구현시 런타임 에러 발생...... bfs deque를 이용했더니 잘 돌아감....ㅠㅠㅠ