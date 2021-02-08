global answer

answer = 0

def dfs(numbers, target, length, value):
    global answer
    if length == len(numbers) and target == value:
        answer += 1
        return
    else:
        if length < len(numbers):
            dfs(numbers, target, length + 1,value + numbers[length])
            dfs(numbers, target, length + 1,value - numbers[length])
    


numbers = list(map(int, input()))
target = int(input())

dfs(numbers, target, 0, 0)
print(answer)