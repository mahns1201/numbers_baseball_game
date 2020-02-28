import random

'''
def convert(list):                      #리스트를 int형으로 반환해서 할까하다가...
    s = [str(i) for i in list]
    res = int("".join(s))

    return(res)
'''

strike = 0              #기본 strike, ball은 0으로 지정
ball = 0

Qu = random.sample(['1','2','3','4','5','6','7','8','9'], 3)          #1~9중 랜덤으로 3개 선택(중복x)
#print(Qu)  <- 정답                                                    # 문자열로  리스트에 저장

while True:
    Ans = str(input("숫자를 입력하세요: "))         #사용자에게 입력받아 문자열로 변경

    if Ans == "0":                                 #0을 입력받으면 종료
        print("종료")
        break

    if len(Ans) != 3:                            #입력한 숫자가 3개가 아니면 다시입력
        print("WARNING : 3개의 숫자를 입력해주세요")


    else:
        if Qu[0] == Ans[0]:             #각각 같은자리 값 비교, 스트라이크면 1추가
            strike = strike + 1

        if Qu[1] == Ans[1]:
            strike = strike + 1

        if Qu[2] == Ans[2]:
            strike = strike + 1

        if Qu[0] == Ans[1] or Qu[0] == Ans[2]:              #각각 다른자리 값 비교, 볼이면 1추가
            ball = ball + 1

        if Qu[1] == Ans[0] or Qu[1] == Ans[2]:
            ball = ball + 1

        if Qu[2] == Ans[0] or Qu[2] == Ans[1]:
            ball = ball + 1

        print("스트라이크:", strike, " ball:", ball)

        if strike == 3:
            print("삼진 아웃!!!")
            break

        strike = 0          #strike, ball 초기화
        ball = 0
