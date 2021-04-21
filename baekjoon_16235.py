# from collections import deque
# import time
# start = time.time()

# def tree_fintech(energy, trees_inf, years):
    
#     # 주어진 연수만큼 반복 후 종료
#     while years > 0:
#         print("남은 연 수")
#         print(years)

#         # 봄
#         for_del = []
#         for tree_inf in trees_inf:
#             # 그 칸에 양분이 나무의 나이와 같거나 그보다 많다면
#             if graph[tree_inf[0] - 1][tree_inf[1] - 1] >= tree_inf[2]:
#                 # 양분을 나이의 나무만큼 줄이고 나무의 나이를 1증가
#                 graph[tree_inf[0] - 1][tree_inf[1] - 1] = graph[tree_inf[0] - 1][tree_inf[1] - 1] - tree_inf[2]
#                 tree_inf[2] = tree_inf[2] + 1
#             # 양분이 부족하다면
#             else:
#                 # 나무를 삭제하기 위한 목록에 추가
#                 for_del.append(tree_inf)
#         # 추가된 나무들 삭제
#         for i in for_del:
#             trees_inf.remove(i)

#         print(n, trees, years)
#         print(graph)
#         print(trees_inf)
        
#         # 여름
#         for i in for_del:
#             graph[i[0] - 1][i[1] - 1] = graph[i[0] - 1][i[1] - 1] + i[2] // 2
        
#         for_del.clear()
#         print(n, trees, years)
#         print(graph)
#         print(trees_inf)

#         # 가을

#         # 인접한 8곳에 나무를 번식하기 위한 방향
#         dx = [-1, -1, -1, 0, 0, 1, 1, 1]
#         dy = [-1, 0, 1, -1, 1, -1, 0, 1]

#         for_add = []
#         for tree_inf in trees_inf:
#             # 나무의 나이가 5의 배수일 경우만
#             if tree_inf[2] % 5 == 0:
#                 x = tree_inf[0]
#                 y = tree_inf[1]
#                 for i in range(8):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     # 맵을 벗어나지 않는다면 나이가 1인 나무를 추가하기 위한 리스트에 저장
#                     if 0 < nx <= n and 0 < ny <= n:
#                         for_add.append([nx, ny, 1])
        
#         # 나이가 1인 나무 추가
#         for i in for_add:
#             trees_inf.append(i)
#         # 정렬
#         trees_inf = sorted(trees_inf)

#         for_add.clear()
#         print(n, trees, years)
#         print(graph)
#         print(trees_inf)

#         # 겨울
#         for i in range(n):
#             for j in range(n):
#                 graph[i][j] = graph[i][j] + energy[i][j]
        
#         print(n, trees, years)
#         print(graph)
#         print(trees_inf)

#         # 1년 끝!!
#         years = years - 1
#         print("나무의 수 = {}".format(len(trees_inf)))

#     # 나무의 수 반환
#     return len(trees_inf)

# # 맵의 크기와 나무의 수와 년수를 입력으로 받음
# n, trees, years = map(int, input().split())

# # 매년 추가될 에너지를 입력으로 받음
# energy = []
# for _ in range(n):
#     energy.append(list(map(int, input().split())))

# # 나무의 위치와 나이를 입력으로 받음
# trees_inf = []
# for _ in range(trees):
#     trees_inf.append(list(map(int, input().split())))

# # 같은 칸의 나무들의 나이 비교를 위한 정렬 
# trees_inf = sorted(trees_inf)

# # 처음에는 모든 칸에 5씩 에너지를 가지고 시작
# graph = [[5] * n for _ in range(n)]

# result = tree_fintech(energy, trees_inf, years)

# print(result)

# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간



tree = [[11 for _ in range(5)] for _ in range(3)]
print(tree)