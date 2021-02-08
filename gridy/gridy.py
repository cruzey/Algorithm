# 거스름 돈 해결

# n = 1260
# count = 0

# coins = [500, 100, 50, 10]

# for coin in coins:
#     count += n // coin
#     n %= coin

# print(count)

# 주어진 수 n을 1로 만드는 최소한의 경우의 수
# 조건1 : k로 나눈다
# 조건2 : -1 한다

# n, k = map(int, input().split())

# count = 0

# while n != 1:
#     if n % k == 0:
#         n //= k
#         count += 1
#     else:
#         n -= 1
#         count += 1
# print(count)

# 문자열 s를 입력받아 왼쪽부터 차례로 연산한다는 가정 하에 +, *으로 가장 큰 수를 만드시오

# s = input("문자열을 입력하시오 : ")

# result = int(s[0])

# for i in range(1, len(s)) :
#     if int(s[i]) + result >= int(s[i]) * result:
#         result += int(s[i])
#     else:
#         result *= int(s[i])

# print(result)

# 모험가 파티 최소로 구하기

n = input("모험가의 수 : ")
k = list(map(int, input("모험가의 공포도 : ").split(",")))

k = sorted(k)

count = 0
result = 0

for i in k:
    count += 1
    if i == count:
        result += 1
        count = 0

print(result)