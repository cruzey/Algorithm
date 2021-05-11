from collections import deque

def bfs(x, y, place):
    fx = x
    fy = y
    visited = [[False] * 5 for _ in range(5)]
    queue = deque()

    visited[x][y] = True
    queue.append((x, y))

    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or visited[nx][ny] == True:  
                continue

            if place[nx][ny] == 'X':
                continue
            elif place[nx][ny] == 'O':
                queue.append((nx, ny))
                visited[nx][ny] == True
            elif place[nx][ny] == 'P':
                answer = abs(fx - nx) + abs(fy - ny)
                if answer >= 2:
                    return True
                else:
                    return False

    return True
    

def solution(places):
    answer = []
    for place in places:
        tmp = 1
        for i in range(len(place)):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(i, j, place) == False:
                        tmp = 0
                        break
            if tmp == 0:
                break
        answer.append(tmp)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

result = solution(places)
print(result)

