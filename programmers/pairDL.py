from collections import deque

def solution(words):
    if len(words) % 2 == 1:
        return 0

    words = list(words)
    tmp = deque()
    while words:
        print(words)
        for i in range(len(words)):
            print(f"i는 {i}")
            if len(tmp) == 0:
                tmp.append(words[i])
                print(tmp)
            else:
                tmp.append(words[i])
                print(tmp)
                if tmp[0] == tmp[1]:
                    words.remove(tmp[0])
                    words.remove(tmp[0])
                    tmp.clear()
                    break
                else:
                    tmp.popleft()
                    print(tmp)
                    
        print(len(tmp))
        if len(tmp) >= 1:
            return 0
        
    return 1

words = "baabac"
result = solution(words)
print(result)

# words = "baabaa"
# words = list(words)
# print(words)


