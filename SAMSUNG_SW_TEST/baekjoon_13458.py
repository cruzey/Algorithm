def solution(class_num, md, sd):

    result = 0

    for i in std_num:
        if i <= md:
            result += 1
        else:
            tmp = (i - md) // sd
            if (i - md) % sd == 0:
                result += tmp + 1
            else:
                result += tmp + 2
    
    return result


class_num = int(input())
std_num = list(map(int, input().split()))

md, sd = map(int, input().split())

result = solution(class_num, md, sd)
print(result)


