import itertools

def solution(orders, course):
    answer = []
    # 들어온 orders에 해당하는 알파벳을 정렬하기 위함
    # ex) "WXA" -> sorted -> [A, W, X] -> join -> "AWX"
    for o in range(len(orders)):
        orders[o] = "".join(sorted(orders[o]))
    
    # course에 있는 수 만큼의 조합을 보기 위해
    for i in course:
        mid_result = []
        alter = []
        # orders중 첫번째부터 i만큼의 모든 조합을 생성해서 리스트의 형태로 mid_result에 append
        for order in orders:
            mid_result.append(list(map("".join, itertools.combinations(order, i))))
        # 2차원 리스트를 1차원의 후보군 리스트로 만듬
        for cnt in mid_result:
            alter += cnt
        # 반복횟수가 가장 큰 조합을 찾아냄
        max_v = 0
        for j in alter:
            if j == alter[0]:
                max_v = alter.count(j)
            else:
                if alter.count(j) > max_v:
                    max_v = alter.count(j)
        # 그 반복횟수가 2이상이면 그 반복횟수만큼 반복된 조합을 찾아내서 답에 추가
        for z in alter:
            if alter.count(z) == max_v and max_v >= 2:
                answer.append(z)
    # 중복제거와 정렬을 위한 set -> list -> sort
    answer = set(answer)
    answer = sorted(list(answer))
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

result = solution(orders, course)
print(result)