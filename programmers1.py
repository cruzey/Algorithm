def solution(lottos, win_nums):
    answer = []
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    zero_num = 0
    result = 0
    for i in lottos:
        if i == 0:
            zero_num += 1
    if zero_num >= 1:
        lottos.remove(0)

    print(zero_num)

    for i in lottos:
        for j in win_nums:
            if i == j:
                result += 1
    
    high = 7 - (result + zero_num)
    if result == 0:
        low = 6
    else:
        low = 7 - result

    answer.append(high)
    answer.append(low)
    print(answer)
    

    return answer


lottos = list(map(int, input().split()))
win_nums = list(map(int, input().split()))

result = solution(lottos, win_nums)
print(result)

