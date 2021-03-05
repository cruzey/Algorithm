# total층 짜리 건물에서 up만큼 올라가는 버튼과 down만큼 내려가는 버튼을 가진 엘리베이터로 
# now층에서 target층을 가고자할 때 최소한의 경우의 수 출력


from collections import deque

def bfs(total, start, target, up, down):
    queue = deque()
    # 몇번 움직였는 지에 해당하는 카운트를 큐에 같이 입력
    queue.append((start, 0))
    # visited = [] 한후 visited.append[now] 했더니 시간초과
    # 앞으로 visited는 인자를 순서를 이용하여 구현하자
    # 토탈층만큼의 0 생성 후 해당 층을 방문시 1로 변경
    visited = [0] * (total + 1)
    visited[start] = 1
    while queue:
        now, count = queue.popleft()
        if now == target:
            return count
        # 올라갈 떄
        if now + up <= total and visited[now + up] == 0:
            visited[now + up] = 1
            queue.append((now + up, count + 1))
        # 내려갈 때
        if now - down >= 1 and visited[now - down] == 0:
            visited[now - down] = 1
            queue.append((now - down, count + 1))
    return "use the stairs"

total, now, target, up, down = map(int, input().split(" "))

result = bfs(total, now, target, up, down)

print(result)
