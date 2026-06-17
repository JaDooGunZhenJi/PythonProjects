books = []

try:
    with open("booklist.txt", "r", encoding = "utf-8") as file:
        for book in books:
            print(f"책: {book["title"]} / 날짜: {book["day"]}")
except FileNotFoundError:
    pass

def save_books():
    with open("booklist.txt", "w", encoding = "utf-8") as file:
        for book in books:
            file.write(book + "\n")

while True:

    print("1. 책 추가")
    print("2. 책 목록 보기")
    print("3. 책 검색")
    print("4. 책 삭제")
    print("5. 종료")


    try:
        number = int(input("넘버 선택하시오!"))
    except ValueError:
        print("숫자만")
        continue
    
    if number == 1:
        title = input("책 이름: ")
        books.append(title)

        day = input("읽은날짜: ")
        books.append(day)

        save_books()

    elif number == 2:
        if len(books) == 0:
            print("책 등록 안함 등록하삼")
        else:
            for book in books:
                print(book)

    elif number == 3:
        search = input("책 이름: ")

        if search in books:
            print(f"{search}있음")

        else:
            print("다시  하시오")

    elif number == 4:
        x = input("삭제할 책 이름: ")
        if x in books:
            books.remove(x)
            print(f"{x} 삭제 완료")
        else:
            print("삭제 오류 다시 시도")

        save_books()

    elif number == 5:
        break

    else:
        print("1~5번까지만 입력해라 좋은말 할때")


        
    

