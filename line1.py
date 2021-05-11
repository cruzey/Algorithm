# def solution(inputString):
#     tmp = 0
#     # check = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}

#     for_matching = []
   
#     for i in range(len(inputString)):
#         if inputString[i] == '(' or inputString[i] == '<' or inputString[i] == '[' or inputString[i] == '{':
#             for_matching.append(inputString[i])
#             tmp = for_matching[-1]
#             print(tmp)

#         if i == 0:
#             if inputString[i] == ')' or inputString[i] == '>' or inputString[i] == ']' or inputString[i] == '}': 
#                 return 0

#         if tmp == 0:
#             if inputString[i] == ')' or inputString[i] == '>' or inputString[i] == ']' or inputString[i] == '}': 
#                 return -i
#         else:
#             if inputString[i] == ')' or inputString[i] == '>' or inputString[i] == ']' or inputString[i] == '}':    
#                 if tmp == '(' and inputString[i] == ')':
#                     for_matching.pop()
#                     tmp = for_matching[-1]
#                 elif tmp == '{' and inputString[i] == '}':
#                     for_matching.pop()
#                     tmp = for_matching[-1]
#                 elif tmp == '[' and inputString[i] == ']':
#                     for_matching.pop()
#                     tmp = for_matching[-1]
#                 elif tmp == '<' and inputString[i] == '>':
#                     for_matching.pop()
#                     tmp = for_matching[-1]
#                 else:
#                     return -i
#     return -i   


# input1 = input()
# result = solution(input1)
# print(result)


def solution(array):
    answer = []
    cnt = 0
    
    for i in range(len(array)):
        tmp = array[i]
        if max(array) == tmp:
            answer.append(-1)
            
        else:
            for a in range(i, -1, -1):
                cnt = cnt + 2
                if array[a] > tmp:
                    answer.append(a)
                    break
                else:
                    array[a+cnt] > tmp:
                    answer.append(a + cnt)
                    break
            for b in range(i, len(array)):
                if array[b] > tmp:
                    answer.append(b)
                    break

    return answer