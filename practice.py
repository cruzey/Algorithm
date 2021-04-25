# #  남자 : 키 * 키 * 22
# #  여자 : 키 * 키 * 21


# def std_weight(height, gender):
#     if gender == "남자":
#         flag = 22
#     else:
#         flag = 21

#     height_m = height/100
    
#     return height_m * height_m * flag


# gender = input("성별을 입력하시오(남자/여자) : ")
# height = int(input("키를 입력하시오 : "))

# std_weight = round(std_weight(height, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight))
# # print(height_m, type(height_m))

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for i in range(1, 51):
#     print("대기번호 : " + str(i).zfill(3))

# class House:
#     num = 0
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         House.num += 1
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("{} {} {} {} {}"\
#         .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

#     def numofhouse():
#         print("총 {}대의 매물이 있습니다.".format(House.num))

# a = House("강남", "아파트", "매매", "10억", "2010년")
# b = House("마포", "오피스텔", "전세", "5억", "2007년")
# c = House("송파", "빌라", "월세", "500/50", "2000년")

# listofhouse = []
# listofhouse.append(a)
# listofhouse.append(b)
# listofhouse.append(c)

# for i in listofhouse:
#     i.show_detail()

# House.numofhouse()

# input 가공하는 법 연습하기

# data = list(map(int, input(">> ").split(",")))

# print(data)
# print(type(data))

# 그리디 연습

# data = input()
# data_list = []
# data_length = len(data)
# count = 0
# result = ""

# for i in range(data_length):
#     if ord(data[i]) < 65:
#         count += ord(data[i])-ord('0')
#     else:
#         data_list.append(data[i])

# data_list = sorted(data_list)

# print(data_list)

# data_list.append(str(count))

# # for i in data_list:
# #     result += i

# # print(result)

# print(''.join(data_list))

# def main():
#     left = 0
#     right = 0
#     x = input()
#     for i in x:
#         print(i)
#         if i == "(":
#             left += 1
#         if i == ")":
#             right += 1
#     if left == right:
#         print("YES")
#     else:
#         print("NO")

# if __name__=="__main__":
#     main()

# sw마에스트로 1번

def main():
    result = []
    skill = list(input().split(" "))
    num = int(input())
    link = []
    for i in range(num):
        link.append(list(input().split(" ")))


    for i in link:
        if i[0] == "h":
            if i[1] == "f":
                result.append(i)
            else:
                if ['g', 'r'] in link:
                    result.append(["h", "g", "r"])
                if ['g', 'w'] in link:
                    result.append(["h", "g", "w"])

    for i in result:
        for j in i:
            print(j,end=" ")
        print()

if __name__=="__main__":
    main()

# sw마에스트로 2번

def main():
    p, n, h = map(int, input().split(" "))
    res = []
    for i in range(n):
        res.append(list(map(int, input().split(" "))))
        
    result = []
    
    for i in range(len(res)):
        if res[i][1] > h:
            res.remove(res[i])
        
        if res[i][0] == i:
            cnt += res[i][1]
    
    print(x)

if __name__=="__main__":
    main()

# sw마에스트로 4번

global answer
answer = []

def myfunction(graph, v, visited, n):
    if visited[v]:
        answer.append(n)
        return
    else:
        visited[v] = True
        i = v + graph[v]
        myfunction(graph, i, visited, n + 1)
        return

def main():
    n = int(input())
    
    data = list(map(int, input().split(" ")))
    
    for i in range(3):
        visited = [False] * n
        myfunction(data, i, visited, 1)
    
    print(max(answer))

if __name__=="__main__":
    main()