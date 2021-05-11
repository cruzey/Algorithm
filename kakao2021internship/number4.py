n = 3
start = 1
end = 3
traps = [2, 3]
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
answer = 0
result = []
visited = [False] * (n+1)

def dfs(n, start, end, roads, traps):
    global answer
    global result
    global visited
    if start == end:
        result.append(answer)
        answer -= start
        visited[start] = False
        return 

    visited[start] = True

    if start in traps:
        for road in roads:
            if road[1] == start:
                road[0], road[1] = road[1], road[0]

    for road in roads:
        if road[0] == start:
            if not visited[road[1]]:
                visited[road[1]] = True
                answer += road[2]
                dfs(n, road[1], end, roads, traps)


    answer -= start
    visited[start] = False
    return 




dfs(n, start, end, roads, traps)
print(result)