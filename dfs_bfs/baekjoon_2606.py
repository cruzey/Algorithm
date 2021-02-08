# 컴퓨터의 수와 연결된 관계의 수를 입력으로 받고 그 관계를 일일히 입력으로 받아서
# 하나의 컴퓨터를 주면 그 컴퓨터와 연결된 모든 컴퓨터를 리턴

def dfs(v, graph, linked, visited):
    if v in linked:
        return
    else:
        linked.append(v)
        for i in graph:
            # 그래프의 원소들 중 v를 포함하고 있는 원소가 있고 그 원소가 방문한 것이 아니면
            if v in i and i not in visited:
                visited.append(i)
                # v가 아닌 원소로 다시 연결된 것을 찾는다
                if not i[0] in linked:
                    dfs(i[0], graph, linked, visited)
                if not i[1] in linked:
                    dfs(i[1], graph, linked, visited)
        return
    

num = int(input())
relation = int(input())
graph = []
for i in range(relation):
    graph.append(list(map(int, input().split(" "))))

linked = []
visited = []
# 1번 컴퓨터와 연결된 모든 컴퓨터 찾기
dfs(1, graph, linked, visited)

print(linked)