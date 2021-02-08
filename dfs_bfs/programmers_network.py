
def bfs(n, graph):
    result = n
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if graph[i][j] == 1:
                result -= 1
                graph[i][j] = 0
                graph[j][i] = 0
    return result


num = int(input())
computers = []
for i in range(num):
    computers.append(list(map(int, input())))

print(bfs(num, computers))
