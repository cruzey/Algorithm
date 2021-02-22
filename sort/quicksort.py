def quicksort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)
    


data = list(map(int, input().split(" ")))

quicksort(data, 0, len(data) - 1)
print(data)
