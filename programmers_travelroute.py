global result, visited
# 답을 리턴할 변수
result = []
# 방문한 노드를 확인할 변수
visited = []

def dfs(start, graph):
    result.append(start)
    v = start
    cnt = []
    for i in graph:
        # 그래프의 원소의 [0]와 v를 비교하여 같고
        if i[0] == v:
            # 그 그래프의 원소가 방문한 적이 없으면
            if not i in visited:
                # 임시로 저장
                cnt.append(i)
    # 임시로 저장한 원소가 2개 이상이면, 즉 출발지와 연결된 도착지가 2개 이상이면
    if len(cnt) >= 2:
        x = cnt[0]
        # 도착지 중 알파벳이 가장 빠른 것부터 방문 처리
        for i in cnt:
            if i[1] < x[1]:
                x = i
        visited.append(x)
        # 방문처리 한 노드의 [0]을 시작으로 하는 다음 여행경로 찾기
        dfs(x[1], graph)
    # 저장한 원소가 하나이면 방문처리 후 다음 동작
    elif len(cnt) == 1:
        visited.append(cnt[0])
        dfs(cnt[0][1], graph)
    return

tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", 'HND']] 
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

# dfs("ICN", tickets1)

dfs("ICN", tickets2)
print(result)
print(visited)
