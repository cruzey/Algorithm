# # 두 값 사이의 갯수 구하기
# bisect를 이용하여 타겟의 겟수 리턴
# from bisect import *

# def count_by_range(list1, left_value, right_value):
#     if not left_value in list1:
#         return -1
#     # right_value 값을 list1에 추가할 때 가질수 있는 가장 오른쪽의 인덱스 구하기
#     right_index = bisect_right(list1, right_value)
#     # left_value 값을 list1에 추가할 때 가질수 있는 가장 왼쪽의 인덱스 구하기
#     left_index = bisect_left(list1, left_value)
#     return right_index - left_index

# 바이너리 서치를 구현하여 타겟의 갯수를 리턴
def binary_search (array, start, end, target):
    result = 0
    while result == 0:
        mid = (start + end) // 2
        if mid == target:
            result = mid
        elif mid > target:
            end = mid - 1
        elif mid < target:
            start = mid + 1

    totalnum = 0
    for i in array:
        if array[result] == i:  
            totalnum += 1
    return totalnum


n, x = map(int, input().split())
array = list(map(int, input("{}개의 원소를 순서대로 입력하시오 : ".format(n)).split()))

# print(count_by_range(array, x, x))
print(binary_search(array, 0, max(array), x))