# 병사의 수와 병사들의 전투력을 입력으로 받아 병사를 최소한으로 제거하여 전투력을 내림차순 순으로 정렬하시오

n = int(input())
power = list(map(int, input().split(" ")))
power.reverse()

# lis 알고리즘 점화식 이용

# 원소 하나인 수열의 가장 긴 부분수열의 개수는 1 이기에 처음에 1로 초기화
d = [1] * n

for i in range(1, n):
    for j in range(i):
        if power[j] < power[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
