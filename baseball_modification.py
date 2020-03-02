import random


END_COMMAND = '0'
ANSWER_LENGTH = 3


def strike(COMPUTER_ANSWER, USER_ANSWER):
    strike = 0

    if COMPUTER_ANSWER[0] == USER_ANSWER[0]:  # 각각 같은자리 값 비교, 스트라이크면 1추가
        strike = strike + 1

    if COMPUTER_ANSWER[1] == USER_ANSWER[1]:
        strike = strike + 1

    if COMPUTER_ANSWER[2] == USER_ANSWER[2]:
        strike = strike + 1

    return strike


def ball(COMPUTER_ANSWER, USER_ANSWER):
    ball = 0
    
    if COMPUTER_ANSWER[0] == USER_ANSWER[1] or COMPUTER_ANSWER[0] == USER_ANSWER[2]:  # 각각 다른자리 값 비교, 볼이면 1추가
        ball = ball + 1

    if COMPUTER_ANSWER[1] == USER_ANSWER[0] or COMPUTER_ANSWER[1] == USER_ANSWER[2]:
        ball = ball + 1

    if COMPUTER_ANSWER[2] == USER_ANSWER[0] or COMPUTER_ANSWER[2] == USER_ANSWER[1]:
        ball = ball + 1

    return ball



COMPUTER_ANSWER = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)  # 1~9중 랜덤으로 3개 선택(중복x)
print(COMPUTER_ANSWER)



while True:
    USER_ANSWER = str(input("숫자를 입력하세요: "))  # 사용자에게 입력받아 문자열로 변경

    if USER_ANSWER == END_COMMAND:  # 0을 입력받으면 종료
        print("종료")
        break

    if len(USER_ANSWER) != ANSWER_LENGTH:  # 입력한 숫자가 3개가 아니면 다시입력
        print("WARNING : 3개의 숫자를 입력해주세요")


    else:
        strike_ = strike(COMPUTER_ANSWER, USER_ANSWER)
        ball_ = ball(COMPUTER_ANSWER, USER_ANSWER)

        print("스트라이크:", strike_, " ball:", ball_)

        if strike_ == 3:
            print("삼진 아웃!!!")
            break
