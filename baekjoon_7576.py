# 토마토가 없으면 -1, 토마토가 익지 않았으면 0, 토마토가 익었으면 1로 표현될 때 입력을 받아서
# 며칠 후면 토마토가 모두 익는 지 알아내는 문제 단 익지 않은 토마토는 익은 토마토와 근접해 있을 때만 하루뒤에 익는다

from collections import deque

def bfs(x, y):
    days = -1

    while queue:
        days += 1
        # 큐에 있는 원소의 수만큼 반복하여 pop을 수행한다 즉 1일안에 모든 1에 대한 동작을 수행한다
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위를 벗어나지 않는 내에서 0을 1로 바꿔주고 바뀐 좌표를 다시 큐에 넣어준다
                if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 0):
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
    # 토마토가 익지 못하는 상황이면 -1 리턴
    for i in graph:
        if 0 in i:
            return -1
    return days



m, n = map(int, input().split(" "))
graph = []

# 메소드 내의 큐를 바깥에서 초기화해서 사용하는 방법 기억하자!!
queue = deque()
result = 0
for i in range(n):
    graph.append(list(map(int, input().split(" "))))


# 방향 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        # 처음에 1로 시작하는 좌표를 모두 구해서 bfs 큐에 모두 넣어준다
        if graph[i][j] == 1:
            queue.append((i, j))


result = bfs(m, n)

print(result)

