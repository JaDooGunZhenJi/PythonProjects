from ReactionGame import ReactionGame

game = ReactionGame()

print("1. 새로 시작")
print("2. 이어서 시작")
start = input(">")

if start == "1":
    pass
elif start == "2":
    game.load()
else:
    print("새로 시작함")

while True:
    print("\n1. 게임하기")
    print("2. 최고 기록 보기")
    print("3. 저장")
    print("4. 종료")

    try:
        number = int(input("번호입력:"))
    except ValueError:
        print("1~4번까지만 입력하셈..")
        continue

    if number == 1:
        game.play()
    elif number == 2:
        if game.best_record is None:
            print("아직 기록이 없음.")
        else:
            print(f"최고 기록: {game.best_record: .3f}초")
    elif number == 3:
        game.save()
    elif number == 4:
        break
    else:
        print("1번부터 4번까지 입력")
