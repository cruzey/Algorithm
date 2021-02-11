

# def make_ricecake(array, target):
#     array.sort(reverse=True)

#     count = 0

#     for i in range(len(array)):
#         cnt = array[i] - array[i+1]
#         count += cnt * (i+1)
#         if target > count:
#             continue
#         elif target == count:
#             return array[i+1]
#         elif target < count:
#             return array[i+1] + (count-target) // (i+1) 
            
def make_ricecake(start, end, target):
    mid = (start + end) // 2
    sum_rc = 0
    # 모든 떡을 기준치만큼 잘랐을 때 떡이 더 길어서 얻을 수 있는 경우 떡들을 더해준다
    for i in array:
        if i > mid:
            sum_rc += i - mid
    
    if sum_rc == target:
        return mid
    elif sum_rc > target:
        return make_ricecake(mid+1, end, target)
    elif sum_rc < target:
        return make_ricecake(start, mid-1, target)



n, m = map(int, input().split())
array = list(map(int, input().split()))

print(make_ricecake(0, max(array), m))
