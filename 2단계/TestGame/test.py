import random
from pathlib import Path

correct_tests = {}
wrong_tests = {}
tests = {}

FILEPATH = Path(__file__).parent / "test.txt"


def fetch_math_questions(amount=3):
    operators = ["+", "-", "*"]

    for _ in range(amount):
        a = random.randint(20, 100)
        b = random.randint(20, 100)
        op = random.choice(operators)

        question = f"{a} {op} {b} 는?"

        if op == "+":
            answer = a + b
        elif op == "-":
            answer = a - b
        else:
            answer = a * b

        tests[question] = str(answer)

    print(f"{amount}개의 문제를 생성했습니다.")


def load_test():
    if not FILEPATH.exists():
        print("저장된 문제 파일이 없습니다.")
        return
    with open(FILEPATH, "r", encoding="utf-8") as file:
        for line in file:
            q, a = line.strip().split("__", 1)
            tests[q] = a
    print("불러오기 완료")


def save_test():
    with open(FILEPATH, "w", encoding="utf-8") as file:
        for q, a in correct_tests.items():
            file.write(f"{q}__{a}\n")
    print("저장 완료")


def random_test():
    if not tests:
        print("문제가 없음.")
        return

    question = random.choice(list(tests.keys()))
    answer = tests[question]

    user_answer = input(f"{question} ")

    if user_answer == answer:
        print("정답")
        correct_tests[question] = tests.pop(question)
    else:
        print(f"틀림 (정답: {answer})")
        wrong_tests[question] = tests.pop(question)



def correct_test():
    print(f"내가 맞은 문제들: {correct_tests}")


def wrong_test():
    print(f"내가 틀린 문제들 : {wrong_tests}")


def main():
    while True:
        print("\n1. 문제 풀기")
        print("2. 틀린 문제 확인")
        print("3. 맞는 문제 확인")
        print("4. 저장")
        print("5. 종료")
        print("6. 새 문제 생성")

        try:
            N = int(input("번호 입력: "))
        except ValueError:
            print("숫자만 입력")
            continue

        if N == 1:
            random_test()
        elif N == 2:
            wrong_test()
        elif N == 3:
            correct_test()
        elif N == 4:
            save_test()
        elif N == 5:
            break
        elif N == 6:
            fetch_math_questions(5)
        else:
            print("1~6번까지 입력.")


if __name__ == "__main__":
    main()