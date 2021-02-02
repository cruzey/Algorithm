# 사용자로부터 n개의 영단어를 입력받아 그중 하나의 영단어를 문제로 하여 퀴즈를 푸는 게임

from random import *

def quiz2():
    chance = 10 #기회
    set_question = input("영단어를 3개 입력하시오 (,로 구분) : ")

    numofquestion = set_question.split(",")

    question = sample(numofquestion, 1) #인풋중 하나만 고르기
    question = question[0] #원소가 하나뿐인 리스트이지만 자료형을 스트링으로 변환하기 위하여
    # print(question)

    # 자리수 만큼 밑줄 표시
    for i in range(len(question)):
        print("_ ", end="")
    print()

    answer_list = [] #문제와 답을 비교하기 위한 리스트
    for j in range(10):
        answer = input("알파벳을 입력하시오 ({}번 남음): ".format(10-j))
        answer = str(answer)
        if answer in question:
            answer_list.append(answer)
            print("correct")
        else:
            print("wrong")


        # print(answer_list)
        for i in range(len(question)):
            if question[i] in answer_list: #문제의 스펠링이 리스트안에 있으면 스펠링 표시
                print(question[i] + " ", end="")
            else:
                print("_ ", end="")
        print()

    # 비교를 위한 set으로 변경
        set_question = set(question)
        set_answe_list = set(answer_list)

        if set_answe_list == set_question:
            print("도전에 성공하셨습니다.")
            return question

    print("도전에 실패하셨습니다.")
    return question


a = quiz2()