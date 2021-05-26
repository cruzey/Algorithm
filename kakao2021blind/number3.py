def solution(info, query):
    answer = []
    info_list = []
    query_list = []

    for info_value in info:
        info_list.append(list(info_value.split(" ")))
    for query_value in query:
        query_list.append(list(query_value.split(" ")))
    for querys in query_list:
        for val in querys:
            if val == 'and':
                querys.remove(val)
    # print(info_list)
    # print(query_list)

    for query_val in query_list:
        result = 0
        for info_val in info_list:
            cnt = 0
            for i in range(5):
                if i != 4:
                    if query_val[i] == info_val[i] or query_val[i] == '-':
                        cnt += i + 1
                else:
                    if int(query_val[i]) <= int(info_val[i]):
                        cnt += i + 1
            # print(cnt)
            if cnt == 15:
                # print(info_val)
                result += 1
        answer.append(result)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))