movies = {}


try:
    with open("movies.txt", "r", encoding="utf-8") as file:
        for line in file:
            name,score = line.strip().split(":")
            movies[name] = (score)
except FileNotFoundError:
    pass


def save_movies():
    with open("movies.txt", "w", encoding = "utf-8") as file:
        for name,score in movies.items():
            file.write(f"{name}:{score}\n")

        print("저장완료!")

def add_movies():
    name = input("영화 이름:")
    
    movies[name] = 0

    print("추가 완료! ")

def list_movies():
    print(f"영화 리스트: {movies}")


def search_movies():
    search = input("영화 : ")
    if search in movies:
        print(f"검색한 영화 :{search} ")
    else:
        print("해당 영화 찾을 수 없음.")


def score_movies():
    score = input("평점줄 영화: ")
    
    if score in movies:
        score1 = int(input("몇점?(1부터100점)"))
        if 1 <= score1 <= 100:
            movies[score] = score1
            print("평점 등록 완료!")
        else:
            print("1점 미안 안됌.")

    else:
        print("영화 없음.")


def delete_movies():
    d = input("삭제할 영화: ")

    if d in movies:
        del movies[d]
        print("삭제 완료")
    else:
        print("삭제할 영화가 존재 하지 않음.")

    

while True:
    print("1. 영화 추가")
    print("2. 영화 목록 보기")
    print("3. 영화 검색")
    print("4. 영화 평점 주기")
    print("5. 영화 삭제")
    print("6. 저장" )
    print("7. 종료")

    try:
        number = int(input("번호 선택: "))
    except ValueError:
        print("숫자만 입력하셈")
        continue

    if number == 1:
        add_movies()
    elif number == 2:
        list_movies()
    elif number == 3:
        search_movies()
    elif number == 4:
        score_movies()
    elif number == 5:
        delete_movies()
    elif number == 6:
        save_movies()
    elif number == 7:
        break
    else:
        print("1부터 7번까지 입력.")
    




