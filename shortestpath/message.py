# 도시의 수 : n, 경로의 수 : m, 시작 도시 : c가 주어졌을 때 c에서 시작하여 연결된 모든 도시의 수와 
# 도달하는 데에 가장 많이 걸리는 시간을 출력
# 경로는 [출발도시 도착도시 걸리는 시간]으로 주어진다

from collections import deque

def myf(start):
    queue = deque()
    queue.append(start)
    # 도시별 걸리는 시간을 구하기 위한 딕셔너리
    check = {}
    # 도시 수
    citys = 0
    while queue:
        cnt = queue.popleft()
        
        for i in data:
            # 시작도시와 출발도시가 일치하면
            if cnt == i[0]:
                # 딕셔너리에 도착하는 도시에 대한 정보 확인하여 없으면
                if i[1] not in check:
                    # 해당 도착 도시까지 걸리는 시간을 쌍으로 추가하는데 
                    if i[0] in check:
                        # 출발하는 도시까지 이미 소요한 시간이 있다면 걸린 시간을 합산하여 갱신
                        check.update({i[1] : i[2] + check[i[0]]})
                    else:
                        # 출발하는 도시가 처음이라면 그냥 갱신
                        check.update({i[1] : i[2]})
                    # 큐에 도착한 도시 추가
                    queue.append(i[1])
                    # 도시 개수 업데이트
                    citys += 1
                # 이미 딕셔너리에 도착한 도시까지의 정보가 있으면 지금까지 소요하여 온 시간과 이미 기록된 시간 중 짧은 것으로 업데이트
                else:
                    check.update({i[1] : min(i[2] + check[i[0]], check[i[1]])})
    print(check)
    # 도시 수와 소요된 시간중 가장 긴 시간 리턴
    return citys, max(check.values())


n, m, c = map(int, input().split(" "))
data = []
# 경로의 수만큼 경로 입력
for i in range(m):
    data.append(list(map(int, input().split(" "))))

r1, r2 = myf(c)

print("{} {}".format(r1, r2))