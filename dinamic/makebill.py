n, m = map(int, input().split(" "))
bill = []
for i in range(n):
    bill.append(int(input()))

d = [10001] * 10000

d[0] = 0
for i in bill: 
    d[i] = 1

for i in range(bill[-1] + 1, m + 1):

    d[i] = d[i - bill[0]] + 1
    for j in bill:
        cnt = d[i - j] + 1
        if cnt < d[i]:
            d[i] = cnt

result = d[m]

if result == 10001:
    print("-1")
else:
    print(d[m])