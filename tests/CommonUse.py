import random

SIZE_OF_SECRET_CODE = 4


def generate_wrong_answer(secret_code: dict) -> dict:
    answer = dict()

    for item in secret_code.items():
        if item[1] != 6:
            answer[item[0]] = item[1] + 1
        else:
            answer[item[0]] = item[1] - 1

    return answer


def mixed_up_answer(secret_code: dict) -> dict:
    answer = dict()
    index = 0
    while index < SIZE_OF_SECRET_CODE - 1:
        answer[index] = secret_code[index + 1]
        index += 1
    answer[SIZE_OF_SECRET_CODE - 1] = secret_code[0]
    return answer


def generate_secret_code() -> dict:
    secret_code = dict()
    for number in range(0, 4):
        secret_code[number] = random.randint(1, 6)
    return secret_code


def print_secret_code(secret_code: dict) -> None:
    for digit in secret_code.values():
        print(digit, end="")


def convert_dict_secret_code_to_string(secret_code: dict) -> str:
    digits = ''
    for digit in secret_code.values():
        digits += f'{digit}'
    return digits
