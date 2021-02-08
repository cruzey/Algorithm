# 상하좌우 문제
# n*n크기의 정사각형 공간(가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (n, n))에서
# (1, 1)에서 출발하여 방향에 따라 이동하여 최종 목적지에 도착하는 알고리즘
# 갈 수 없는 방향으로의 이동은 무시한다

space = int(input("공간의 크기를 결정하시오 : "))
plans = input("방향을 입력하시오 : ").split()

x, y = 1, 1

# ----------------------------------------
move_types = {"L" : (0, -1), "R" : (0, 1), "U": (-1, 0), "D" : (1, 0)}

for plan in plans:
    for move_type, value in move_types.items():
        if move_type == plan:
            nx = x + value[0]
            ny = y + value[1]
    
    if nx < 1 or ny < 1 or nx > space or ny > space:
        continue

    x, y = nx, ny

print("({}, {})".format(x, y))
#------------------------------------------
# #L, R, U, D 에 따른 이동방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > space or ny > space:
#         continue

#     x, y = nx, ny

# print("({}, {})".format(x, y))

# # for i in route:
# #     if i == "L":
# #         x += dx[0]
# #         y -= dy[0]
# #     elif i == "R":
# #         x += dx[1]
# #         y -= dy[1]
# #     elif i == "U":
# #         x += dx[2]
# #         y -= dy[2]
# #     else:
# #         x += dx[3]
# #         y -= dy[3]

# 0시 0분 0초부터 N시 59분 59초까지 3이 하나라도 들어있는 모든 시간의 경우의 수 구하기

# n = int(input("시간을 입력하시오 : "))

# count = 0
# for hour in range(n+1):
#     for minute in range(60):
#         for second in range(60):
#             if '3' in str(hour)+str(minute)+str(second):
#                 count += 1

# print(count)

# 8 * 8 체스판에서 나이트의 위치를 알 때 나이트가 이동할 수 있는 곳의 경우의 수 구하기
# 체스판의 행은 1~8, 열은 a~h로 표현된다

# data = input("나이트의 위치 : ")
# r = int(data[1])
# c = int(ord(data[0])) - int(ord('a')) + 1

# count = 0
    
#이동가능한 방향
# dx = [0, -2, -1, 1, 2, 2, 1, -1, -2]
# dy = [0, -1 ,-2, -2, -1, 1, 2, 2, 1]

# for i in range(1, 9):
#     nr = r + dx[i]
#     nc = c + dy[i]

#     if nr < 1 or nc < 1 or nr > 8 or nc > 8:
#         continue
#     count += 1
# ---------------------------------
# 다른 풀이

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# for step in steps:
#     nr = r + step[0]
#     nc = c + step[1]
#     if nr < 1 or nc < 1 or nr > 8 or nc > 8:
#         continue
#     count += 1

# print (count)