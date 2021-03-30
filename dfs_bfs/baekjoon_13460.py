from collections import deque

def move(x, y, qx, qy):
    count = 0
    # 다음 칸이 벽이 아니거나 현재 이동한 칸이 구멍이 아니라면 반복해서 나아가며 간 거리를 체크
    while graph[x + qx][y + qy] != '#' and graph[x][y] != 'O':
        x += qx
        y += qy
        count += 1
    return x, y, count


def bfs(rx, ry, bx, by, depth):
    queue = deque()
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue.append((rx, ry, bx, by, depth))
    visited[rx][ry][bx][by] = True
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        for i in range(4):
            nrx, nry, r_cnt = move(rx, ry, qx[i], qy[i])
            nbx, nby, b_cnt = move(bx, by, qx[i], qy[i])

            # 파란 구슬이 구멍에 떨어지면(실패)
            if graph[nbx][nby] == 'O': 
                continue
            # 빨간 구슬이 구멍에 떨어지면(성공)
            if graph[nrx][nry] == 'O': 
                print(depth)
                return
            # 빨간 구슬과 파란 구슬이 같은 칸에 존재하면
            if nrx == nbx and nry == nby : 
                # 이동 거리가 많은 구슬을 한칸 뒤로
                if r_cnt > b_cnt: 
                    nrx -= qx[i]
                    nry -= qy[i]
                else:
                    nbx -= qx[i]
                    nby -= qy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    print(-1) # 실패
    return 

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx = i
            ry = j
        elif graph[i][j] == 'B':
            bx = i
            by = j

qx = [-1, 1, 0, 0]
qy = [0, 0, -1, 1]

bfs(rx, ry, bx, by, 1)