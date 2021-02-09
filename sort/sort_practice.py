# 두 리스트를 k번 만큼 스왑하여 a배열의 합의 최댓값을 리턴
def sort(a, b, k):
    for i in range(k):
        tmp = max(b)
        a.append(tmp)
        b.remove(tmp)
        a.remove(min(a))
    return sum(a)

n, k = map(int, input().split(" "))
listA = list(map(int, input().split(" ")))
listB = list(map(int, input().split(" ")))

print(sort(listA, listB, k))
