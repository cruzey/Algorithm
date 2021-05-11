def solution(s):
    arr = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
    
    result = ""
    tmp = ""
    for word in s:
        print(word)
        if word.isalpha() == True:
            tmp += word
            print(tmp)
            for key, value in arr.items():
                if tmp == value:
                    result += key
                    tmp = ""
        else:
            result += word

        
    return int(result)

a1 = "onetwothreefourfivesixseven"

result = solution(a1)
print(result)

