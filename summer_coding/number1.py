def solution(code, day, data):
    answer = []
    
    for i in data:
        price_i, code_i, time_i = i.split(" ")
        if code_i[5:] == code and time_i[5:-2] == day:
            answer.append([int(price_i[6:]), int(time_i[-2:])])

    answer = sorted(answer, key= lambda x : x[1])
    print(answer)

    return answer

data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]

code = "012345"
day = "20190620"

result = solution(code, day, data)