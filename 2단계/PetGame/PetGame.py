from pathlib import Path

FILE_PATH = Path(__file__).parent / "Pet.txt"

class Pet:

    def __init__(self):
        self.name = "" # 이름 입력
        self.age = 1 # 나이 확인
        self.happy = 100 # 행복도 확인
        self.health= 100 # 건강 확인
        self.hungry = 50 

    def save(self):
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            file.write(f" 이름은 {self.name}\n")
            file.write(f"나이는 {self.age}\n")
            file.write(f"행복도는 {self.happy}\n")
            file.write(f" 건강 점수는 {self.health}\n")
            file.write(f"배고픔은 {self.hungry}\n")

        print("저장 완료!")

    def load(self):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                self.name = file.readline().replace(" 이름은 ", "").strip()
                self.age = int(file.readline().replace("나이는 ", "").strip())
                self.happy = int(file.readline().replace("행복도는 ", "").strip())
                self.health = int(file.readline().replace(" 건강 점수는 ", "").strip())
                self.hungry = int(file.readline().replace("배고픔은 ", "").strip())

            print("불러오기 완료!")
        except FileNotFoundError:
            print("저장된 펫이 없습니다.")


    def feed(self): #배고품
        print("1. 치즈피자")
        print("2. 불닭너구리")
        print("3. 치킨마요덮밥")

        number = int(input("먹이고 싶은거 : "))

        if number == 1:
            self.hungry -= 10
            print(f"{self.name}한테 치즈피자를 먹였어요! 그만 먹어 돼지야")
        elif number == 2:
            self.hungry -= 10
            print(f"{self.name}한테 불닭너구리를 먹였어요! 그만 먹어 돼지야")
        elif number == 3:
            self.hungry -= 10
            print(f"{self.name}한테 치킨마요덮밥을 먹였어요! 그만 먹어 돼지야")
        else:
            print("1~3번만 입력해!")

    def play(self): #건강 하락
        print("1. 게임하기")
        print("2. 쇼츠보기")
        print("3. 유튜브보기")

        number2 = int(input("하고싶은거 : "))

        if number2 == 1:
            self.health -= 10
            self.happy -= 10
            print(f"{self.name}가 게임했습니다.")
            print("건강하고 행복도가 10점 떨어졌습니다.")

        elif number2 == 2:
            self.health -= 10
            self.happy -= 10
            print(f"{self.name}가 쇼츠를 봤습니다.")
            print("건강하고 행복도가 10점 떨어졌습니다.")

        elif number2 == 3:
            self.health -= 10
            self.happy -= 10
            print(f"{self.name}가 유튜브를 봤습니다.")
            print("건강하고 행복도가 10점 떨어졌습니다.")
        
        else:
            print("1~3번만 입력해!")

        
    def act(self): # 행복도 상승
        print("1. 명상하기")
        print("2. 낮잠자기")
        print("3. 책읽기")

        number3 = int(input("하고싶은거: "))

        if number3 == 1:
            self.happy += 10
            print(f"{self.name}가 명상을 했습니다.!")
            print("행복도가 10점 올랐습니다!")

        elif number3 == 2:
            self.happy += 10
            print(f"{self.name}가 낮잠을 잤습니다.!")
            print("행복도가 10점 올랐습니다!")

        elif number3 == 3:
            self.happy += 10
            print(f"{self.name}가 책을 읽었습니다.!")
            print("행복도가 10점 올랐습니다!")

        else:
            print("1~3번만 입력해!")
        

    def wannado(self):
        print("1. 노래부르기")
        print("2. 수영하기")
        print("3. 등산하기")
        print("4. 스키타기")

        number4 = int(input("하고싶은거: "))

        if number4 == 1:
            self.health += 1
            print(f"{self.name}가 노래를 불렀습니다.!")
            print("건강이 1점 올랐습니다!")

        elif number4 == 2:
            self.health += 10
            print(f"{self.name}가 수영을 했습니다.!")
            print("건강이 10점 올랐습니다!")

        elif number4 == 3:
            self.health += 10
            print(f"{self.name}가 등산을 했습니다.!")
            print("건강이 10점 올랐습니다!")

        elif number4 == 4:
            self.health += 10
            print(f"{self.name}가 스키를 탔습니다.!")
            print("건강이 10점 올랐습니다!")

        else:
            print("1~4번만 입력해!")
    


    def next_day(self):
        print("1. 내일로 넘어가기")

        number5 = int(input("내일로 넘어가고싶으면 1번 누르세용 : "))

        if number5 == 1:
            self.health -= 10
            self.happy -= 10
            print(f"{self.name}가 늦게 자버렸습니다.!")
            print("건강이랑 행복도가 10점씩 떨어졌습니다.")

        else:
            print("1번만 입력해!")
        

    def status(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"배고픔 : {self.hungry}")
        print(f"행복도 : {self.happy}")
        print(f"건강 : {self.health}")
    
pet = Pet()
