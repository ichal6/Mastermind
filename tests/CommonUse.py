import random


def generate_wrong_answer(secret_code: dict) -> dict:
    answer = dict()

    for item in secret_code.items():
        if item[1] != 6:
            answer[item[0]] = item[1] + 1
        else:
            answer[item[0]] = item[1] - 1

    return answer


def generate_secret_code() -> dict:
    secret_code = dict()
    for number in range(0, 4):
        secret_code[number] = random.randint(1, 6)
    return secret_code


def print_secret_code(secret_code: dict) -> None:
    for digit in secret_code.values():
        print(digit, end="")
