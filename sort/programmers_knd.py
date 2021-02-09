# 배열을 슬라이싱하여 정렬후 k번째 원소 리턴
def solution(start, end, k):
    start -= 1
    target = []
    target = array[start:end]
    target = sorted(target)
    return target[k-1]


array = [1,5,2,6,3,7,4]

start, end, k = map(int, input().split(","))
print(solution(start, end, k))