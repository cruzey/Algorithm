import heapq
INF = int(1e9)

def dijkstra(start, end):
    global length, graph

    distance = [INF] * (length + 1)

    queue = []
    
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    # bfs 진행
    while queue:
        dist, now = heapq.heappop(queue)
        
        # 해당노드를 방문하는데 드는 비용이 기존 최소비용보다 큰 경우는 무시
        if dist > distance[now]:
            continue
        
        # 그 다음 방문 가능한 노드 탐색
        for i in graph[now]:
            cost = dist + i[1]
            
            # 만약 새로운 비용이 기존의 방문노드를 방문하는데 드는 비용보다 작을 경우만 진행
            if cost < distance[i[0]]:
                # 방문노드 값을 갱신
                distance[i[0]] = cost
                # heapq에 넣어주고 계속 진행
                heapq.heappush(queue, (cost, i[0]))
    
    return distance[end]
    

def solution(n, s, a, b, fares):
    global length, graph

    answer = INF
    length = n

    graph = [[] for _ in range(n+1)]

    for i, j, cost in fares:
        graph[i].append((j, cost))
        graph[j].append((i, cost))

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))


    return answer

fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

print(solution(7, 3, 4, 1, fares))