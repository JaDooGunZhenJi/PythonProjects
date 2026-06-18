import os

print(os.getcwd())
from PetGame import Pet

pet = Pet()

print("1. 새 게임 하기")
print("2. 이어서 하기")

start = int(input(">"))

if start == 1:
    pet.name = input("이름: ")
    
elif start == 2:
    pet.load()
    
else:
    print("다시 입력.")


print("1. 밥 주기")
print("2. 놀기")
print("3. 여가 활동 하기")
print("4. 운동하기")
print("5. 상태 보기")
print("6. 내일로~")
print("7. 저장")
print("8. 불러오기")
print("9. 종료")


while True:
    try:
        number = int(input("번호 :"))

    except ValueError:
        print("1~9번까지만 입력.")
        continue


    if number == 1:
        pet.feed()
    elif number == 2:
        pet.play()
    elif number == 3:
        pet.act()
    elif number == 4:
        pet.wannado()
    elif number == 5:
        pet.status()
    elif number == 6:
        pet.next_day()
    elif number == 7:
        pet.save()
    elif number == 8:
        pet.load()
    elif number == 9:
        break

    else:
        print("1~9번까지만 입력하셈")

    
        

    
