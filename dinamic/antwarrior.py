
def max_of_food(n, boxes):
    d[0] = boxes[0]

    d[1] = max(boxes[0], boxes[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + boxes[i])
    return d[n-1]

num = int(input())
data = list(map(int, input().split(" ")))
d = [0] * num

result = max_of_food(num, data)
print(result)