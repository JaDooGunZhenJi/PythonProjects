import json
from pathlib import Path

books = []

def add_book():
    title = input("제목 : ")
    date = input("읽은 날짜 : ")

    book = {
        "title" : title,
        "date" : date
    }

    books.append(book)

def show_book():
    if len(books) == 0:
        print("등록된 책이 없습니다.")
        return
    for book in books:
        print("__" * 10)
        print(f"책 이름 : {book["title"]}")
        print(f"읽은 날짜 : {book["date"]}")
        

def search_book():
    search = input("책 이름 : ")

    found = False

    for book in books:
        if book["title"] == search:
            print("검색 성공함!")
            print(book)
            found = True

    if not found:
        print("책 등록 안함.")

def delete_book():
    delete = input("삭제할 책 이름 : ")

    for book in books:
        if book["title"] == delete:
            books.remove(book)
            print("삭제 완")
            return
        
    print("책 없음")

FILE_PATH = Path(__file__).parent / "booklist2.json"

def load_book():
    global books

    try:
        with open(FILE_PATH, "r", encoding = "utf-8") as file:
            books = json.load(file)

        print("불러오기 성공")
    except FileNotFoundError:
        print("저장할 파일이 없음.")

def save_book():
    with open(FILE_PATH, "w", encoding = "utf-8") as file:
        json.dump(books,file, ensure_ascii = False, indent = 4)
            
        print("저장 성공")

while True:
    print("책 관리 프로그램")
    print("1. 책 추가")
    print("2. 책 목록")
    print("3. 책 검색")
    print("4. 책 삭제")
    print("5. 책 저장")
    print("6. 책 불러오기")
    print("7. 종료")
    try:
        n = int(input("번호 입력: "))
    except ValueError:
        print("숫자만 입력.")
        continue

    if n == 1:
        add_book()
    elif n == 2:
        show_book()
    elif n == 3:
        search_book()
    elif n == 4:
        delete_book()
    elif n == 5:
        save_book()
    elif n == 6:
        load_book()
    elif n == 7:
        break
    else:
        print("1~7번까지만 입력")
