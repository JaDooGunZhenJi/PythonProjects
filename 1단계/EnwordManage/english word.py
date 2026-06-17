
import random

words = {}

try:
    with open("english.txt", "r", encoding = "utf-8") as file:
        for line in file:
            e,m = line.strip().split()
            words[e] = m

except FileNotFoundError:
    print("해당 파일을 찾을 수 없음.....")

def save_word():
    with open("english.txt", "w", encoding = "utf-8") as file:
        for e, m in words.items():
            file.write(f"{e} {m}\n")
        print("저장완료!")

def add_word():
    e = input("영어단어 쓰시오 : ")
    m = input("뜻을 쓰시오 : ")

    words[e] = m
    print("단어 추가 완료!")

def search_word():
    search = input("검색할 단어 : ")

    if search in words:
        print(f"단어:{search} : {words[search]}")
    else:
        print("등록된 단어가 없습니다.")

def L_word():
    
    if len(words) == 0:
        print("추가된 단어가 없음. ")
    else:
        print(f"너가 추가한 단어들 : {words}")

def del_word():
    delete = input("삭제 할 단어 입력: ")

    if delete in words:
        del words[delete]

    else:
        print("단어가 존재하지 않음.")

def random_word():
    while True:
        word = random.choice(list(words.keys()))

        answer = input(f"{word}뜻 : ")
    
        if answer == words[word]:
            print("정답! ")
            break

        else:
            print("틀렸음 다시.")


while True:
        print("1. 단어 추가","\n2. 단어 검색","\n3. 단어 목록 보기","\n4. 단어 삭제","\n5. 랜덤 퀴즈","\n6. 저장","\n7. 종료")

        try:
            number = int(input("번호 입력하시오..:"))
        except ValueError:
            print("1~7번까지만 입력")

        if  number == 1:
            add_word()

        elif number == 2:
            search_word()

        elif number == 3:
            L_word()

        elif number == 4:
            del_word()

        elif number == 5:
            random_word()

        elif number == 6:
            save_word()

        elif number == 7:
            break

        else:
            print("1~7번까지 입력하셈")