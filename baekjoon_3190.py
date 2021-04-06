# 뱀이 이동할 수 있는 시간 구하기

from collections import deque

def snake(graph, plans):
    queue = deque()

    # 1, 1에서 뱀이 오른쪽으로 출발
    queue.append((0, 0, 'R'))
    graph[0][0] = 'body'
    
    # 뱀의 길이만큼 표기 위한
    snake1 = deque()
    snake1.append((0, 0))
    
    # 방향 전환시 필요
    plan_L = ['U', 'L', 'D', 'R', 'U']
    plan_D = ['D', 'L', 'U', 'R', 'D']

    move_types = {"L" : (0, -1), "R" : (0, 1), "U": (-1, 0), "D" : (1, 0)}
    day = 0
    flag = 0
    while queue:
        
        day += 1
        x, y, direction = queue.popleft()

        # print(day, direction)
        
        # 무브 타입과 방향이 일치할시 그쪽 좌표로 이동
        for move_type, value in move_types.items():
            if move_type == direction:
                nx = x + value[0]
                ny = y + value[1]
        
        # 벽 만나면 끝
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            # print("end of map")
            return day
        
        # 자기 몸 먹으면 끝
        if graph[nx][ny] == 'body':
            # print("eat my body")
            return day

        # 사과 만나면 몸 크기 증가
        if graph[nx][ny] == 'apple':
            graph[nx][ny] = 'body'
            snake1.append((nx, ny))
        # 빈 땅이면 길이 그대로기에 꼬리를 지워준다
        else:
            graph[nx][ny] = 'body'
            snake1.append((nx, ny))
            tx, ty = snake1.popleft()
            graph[tx][ty] = 0
        
        # print(graph)

        # 해당 시간까지 이동을 마친후 방향 탐색
        # 해당 시간이 지났으면
        if day == int(plans[flag][0]):
            # print("catch!!, {}, {}".format(day, plans[flag][0]))
            # 왼쪽으로 도는지 오른쪽으로 도는지 확인
            if plans[flag][1] =='L':
                for i in range(4):
                    # 지금방향에서 왼쪽으로 돌기
                    if direction == plan_L[i]:
                        direction = plan_L[i + 1]
                        break
                
            elif plans[flag][1] =='D':
                for i in range(4):
                    # 지금방향에서 오른쪽으로 돌기
                    if direction == plan_D[i]:
                        direction = plan_D[i + 1]
                        break
            # 다음 번 방향 전환 계획을 살펴보기 위해 플래그 증가
            if flag < plan_num-1:
                flag += 1

        queue.append((nx, ny, direction))

# 맵 입력 1, 1부터 시작
n = int(input())

# 사과 갯수
apple_num = int(input())
# 수만큼 좌표
apples = []
for i in range(apple_num):
    apples.append(list(map(int, input().split())))

# 방향 갯수
plan_num = int(input())
# 수만큼 (몇초 뒤 방향을 바꿈, 왼쪽L 아니면 오른쪽D)
plans = []
for i in range(plan_num):
    plans.append(list(input().split()))

# 맵의 빈땅에 0 표기
graph = [[0] * (n) for _ in range(n)]

# 1, 1 부터 n, n 까지
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 사과의 좌표에 apple 표기
        if [i, j] in apples:
            graph[i - 1][j - 1] = 'apple'

result = snake(graph, plans)
print(result)

# print(graph)
# print(plans)
# print(apples)
# print(type(int(plans[0][0])))



