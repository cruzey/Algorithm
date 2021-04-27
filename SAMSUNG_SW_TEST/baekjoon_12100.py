# 2048 문제에서 5번 이동하여 구할수 있는 최댓값 구하기

from collections import deque
from copy import deepcopy

def move(graph1, dir):
    graph = deepcopy(graph1)
    if dir == '상':
        for j in range(n):
            flag = 0
            tmp = 0
            for i in range(n):
                if graph[i][j] == 0:
                    continue
                if tmp == 0:
                    tmp = graph[i][j]
                else:
                    if tmp == graph[i][j]:
                        graph[flag][j] = tmp * 2
                        tmp = 0
                        flag += 1
                    else:
                        graph[flag][j] = tmp
                        tmp = graph[i][j]
                        flag += 1

                graph[i][j] = 0
                if tmp != 0:
                    graph[flag][j] = tmp

    elif dir == '하':
        for j in range(n):
            flag = n - 1
            tmp = 0
            for i in range(n - 1, -1, -1):
                if graph[i][j] == 0:
                    continue
                if tmp == 0:
                    tmp = graph[i][j]
                else:
                    if tmp == graph[i][j]:
                        graph[flag][j] = tmp * 2
                        tmp = 0
                        flag -= 1
                    else:
                        graph[flag][j] = tmp
                        tmp = graph[i][j]
                        flag -= 1

                graph[i][j] = 0
                if tmp != 0:
                    graph[flag][j] = tmp

    elif dir == '좌':
        for i in range(n):
            flag = 0
            tmp = 0
            for j in range(n):
                if graph[i][j] == 0:
                    continue
                if tmp == 0:
                    tmp = graph[i][j]
                else:
                    if tmp == graph[i][j]:
                        graph[i][flag] = tmp * 2
                        tmp = 0
                        flag += 1
                    else:
                        graph[i][flag] = tmp
                        tmp = graph[i][j]
                        flag += 1

                graph[i][j] = 0
                if tmp != 0:
                    graph[i][flag] = tmp

    elif dir == '우':
        for i in range(n):
            flag = n - 1
            tmp = 0
            for j in range(n - 1, -1, -1):
                if graph[i][j] == 0:
                    continue
                if tmp == 0:
                    tmp = graph[i][j]
                else:
                    if tmp == graph[i][j]:
                        graph[i][flag] = tmp * 2
                        tmp = 0
                        flag -= 1
                    else:
                        graph[i][flag] = tmp
                        tmp = graph[i][j]
                        flag -= 1

                graph[i][j] = 0
                if tmp != 0:
                    graph[i][flag] = tmp

    return graph




n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dir = ['상', '하', '좌', '우']

queue = deque()
queue.append(graph)
cnt = 0
while cnt < 5:
    cnt += 1
    for _ in range(len(queue)):
        graph = queue.popleft()
        print(graph)
        for i in range(4):
            zip = move(graph, dir[i]) 
            queue.append(zip)
    
result = 0
for i in range(len(queue)):
    for j in range(n):
        if result < max(queue[i][j]):
            result = max(queue[i][j])

print(result)