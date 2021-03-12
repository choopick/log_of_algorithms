from random import randint


def generate_numbers():
    numbers = set()
    while len(numbers) != 3:
        numbers.add(randint(0,9))
    numbers = list(numbers)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers 


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    cnt = 0
    
    while len(new_guess) != 3:
        inputNumber = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess)+1)))
        new_guess.append(inputNumber)
        cnt += 1

        if new_guess[len(new_guess)-1] > 9 or new_guess[len(new_guess)-1] < 0:
            del new_guess[len(new_guess)-1]
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            cnt -= 1
        elif new_guess[cnt-1] == new_guess[cnt-2] and cnt >= 2:
            del new_guess[cnt-1]
            print("중복되는 숫자입니다. 다시 입력하세요")
            cnt -= 1

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for num in range(3):
        if guess[num] == solution[num]:
            strike_count += 1
        elif guess[num] in solution:
            ball_count += 1

    return strike_count, ball_count
    
# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
s = str()
b = str()

while True:
    s, b = get_score(take_guess(),ANSWER)

    print(f"{s}S {b}B")
    tries += 1

    if  s == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
