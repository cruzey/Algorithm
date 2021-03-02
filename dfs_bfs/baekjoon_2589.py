# 땅은 "L", 바다는 "W"로 표시된 지도를 입력으로 받아서 이어져 있는 땅 중에 땅과 땅 사이의 최대 거리를 구하기

from collections import deque
import copy

def bfs(x, y):
    queue = deque()
    # 땅 좌표를 넣고 시작
    queue.append((x, y))
    count = -1
    # visited용 복사된 맵 생성
    copy_graph = copy.deepcopy(graph)
    
    while queue:
        count += 1
        # 하나의 땅에서 최대 상하좌우 4개의 연결된 땅이 있을 경우 모두 1씩 증가 시키기 위해 한번에 pop
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵의 범위 벗아나면 패스
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                # 인접한 곳이 물이면 패스
                if graph[nx][ny] == "W":
                    continue

                # 인접한 곳이 땅이고 방문한 적이 없으면
                if graph[nx][ny] == "L" and copy_graph[nx][ny] != "check":
                    # 방문 처리
                    copy_graph[nx][ny] = "check"
                    print(copy_graph)
                    # 땅을 queue에 삽입
                    queue.append((nx, ny))
    
    return count
                

result = []
n, m = map(int, input().split(" "))
graph = []
for i in range(n):
    graph.append(list(input()))


# 방향 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지도 상의 모든 땅에서 시작해야 하기 때문에 모든 "L"을 찾아서 시작으로 입력
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            x = bfs(i, j)
            result.append(x)

print(max(result))


