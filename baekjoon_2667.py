# 정사각형 모양의 지도에서 빈공간은 0, 집이 있는 공간은 1일때 연결된 집들을 하나의 단지로 판별하여
# 총 단지의 수와 단지 별 집들의 수를 리턴


def dfs(x, y, cnt):
    if x <= -1 or x >= num or y <= -1 or y >=num:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = cnt
        dfs(x-1, y, cnt)
        dfs(x+1, y, cnt)
        dfs(x, y-1, cnt)
        dfs(x, y+1, cnt)
        return True
    return False

# 총 단지의 수
result = 0
# 단지 별 집들의 수
numofhouse = 0
# 탐색한 집의 숫자를 바꿔줄 변수, 나중에 이 변수의 갯수를 세어서 집들의 수 확인
cnt = 2
num = int(input())
graph = []
for i in range(num):
    graph.append(list(map(int, input())))

for i in range(num):
    for j in range(num):
        # 집이 있으면 리턴 true로 총 단지 수를 하나 추가하고 다음번 단지의 집들을 판별하기 위해 cnt 증가
         if dfs(i, j, cnt) == True:
             result += 1
             cnt += 1

print(result)

# cnt 시작을 2부터 하여서 단지들의 수만큼 그 단지에 포함된 집들을 출력
for i in range(2, cnt):
    for j in graph:
        numofhouse += j.count(i)
    print(numofhouse)
    numofhouse = 0
