def solution(n, k, cmd):
    flag = n - 1
    answer = ''
    arr = ''
    save = []
    for i in range(n):
        arr += str(i)

    for order in cmd:
        if order[0] == 'D':
            k += int(order[2])
        elif order[0] == 'U':
            k -= int(order[2])
        elif order == 'C':
            save.append(k)
            arr = arr[:-1]
            if k == flag:
                k -= 1
            flag -= 1
        elif order == 'Z':
            flag += 1
            arr += str(flag)
            x = save.pop()
            if x <= k:
                k += 1

    for i in range(n):
        if i in save:
            answer += 'X'
        else:
            answer += 'O'
            
    return answer

n = 8
k = 2 
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
result = solution(n, k, cmd)
print(result)