from collections import deque

def solution(rows, columns, queries):
    answer = []

    graph = [[0] * columns for _ in range(rows)]

    tmp = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = tmp
            tmp += 1

    queue = deque()

    move_types = {"L" : (0, -1), "R" : (0, 1), "U": (-1, 0), "D" : (1, 0)}
    
    for query in queries:
        result = []
        queue.append((query[0] - 1, query[1] - 1, 'R'))
        tmp = graph[query[0] - 1][query[1] - 1]
        result.append(tmp)
        while queue:
            x, y, direction = queue.popleft()
            for move_type, value in move_types.items():
                if direction == move_type:
                    nx = x + value[0]
                    ny = y + value[1]
            tmp2 = graph[nx][ny]
            graph[nx][ny] = tmp
            result.append(tmp2)
            tmp = tmp2

            
            if nx == query[0] - 1 and ny == query[3] - 1:
                direction = 'D'
                queue.append((nx, ny, direction))
            elif nx == query[2] -1 and ny == query[3] - 1:
                direction = 'L'
                queue.append((nx, ny, direction))
            elif nx == query[2] -1 and ny == query[1] - 1:
                direction = 'U'
                queue.append((nx, ny, direction))
            elif nx == query[0] - 1 and ny == query[1] - 1:
                break
            else:
                queue.append((nx, ny, direction))
        answer.append(min(result))
    
    print(graph)

    return answer

n, m = map(int, input().split())
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

result = solution(n, m, queries)
print(result)
