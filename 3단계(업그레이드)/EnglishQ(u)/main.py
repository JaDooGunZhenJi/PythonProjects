from english import WordBook


book = WordBook()
book.load_word()

while True:
    print("1. 단어 추가")
    print("2. 단어 검색")
    print("3. 단어 목록 보기")
    print("4. 단어 삭제")
    print("5. 랜덤 퀴즈")
    print("6. 저장")
    print("7. 종료")

    try:
        number = int(input("번호 입력: "))
    except ValueError:
        print("숫자만 입력하셈")
        continue

    if number == 1:
        book.add_word()
        
    elif number == 2:
        book.search_word()
        
    elif number == 3:
        book.list_word()
        
    elif number == 4:
        book.del_word()
        
    elif number == 5:
        book.random_word()
        
    elif number == 6:
        book.save_word()
        
    elif number == 7:
        break
    else:
        print("1~7번까지 입력하셈")