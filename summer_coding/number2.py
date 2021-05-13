
def solution(t, r):

    answer = []
    queue = []
    guest = {}

    limit = max(t)
    
    for i in range(len(t)):
        guest[t[i]] = r[i]

    lift_num = 0
    while limit != lift_num:
        for num, rate in guest.items():
            if lift_num == num:
                queue.append([num, rate])
                print(queue)

        max_v = 0
        cnt = 0
        for i in queue:
            if i[1] > max_v:
                max_v = i[1]
                cnt = i[0]
        
        answer.append(cnt)

        for i in queue:
            if i[1] == max_v:
                queue.remove(i)
        lift_num += 1

    return answer

t = [0,1,3,0]
r = [0,1,2,3]

# dic = {}

# for i in range(len(t)):
#     dic[t[i]] = r[i]
# print(dic)

result = solution(t, r)
print(result)