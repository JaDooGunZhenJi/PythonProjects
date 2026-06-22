import random
import time
from pathlib import Path

FILE_PATH = Path(__file__).parent / "best_record.txt"

class ReactionGame:

    def __init__(self):
        self.best_record = None

    def save(self):
        with open(FILE_PATH, "w", encoding = "utf-8") as file:
            file.write(f"{self.best_record}")
            print("저장 완료!")
            pass
    
    def load(self):
        try:
            with open(FILE_PATH, "r", encoding = "utf-8") as file:
                self.best_record = float(file.readline(). strip())
            print(f"불러오기 완료! 최고기록: {self.best_record}")
        except FileNotFoundError:
            print("저장된거 없음")

    def play(self):
        print("\n신호 뜨면 엔터")
        input("준비되면 엔터")

        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)

        print("\n지금!")

        start = time.time()
        input()
        end = time.time()

        reaction_time = end - start

        if reaction_time < 0.1:
            print("다시")
        else:
            print(f"반응 속도 : {reaction_time:.3f}초")

            if self.best_record is None or reaction_time < self.    best_record:
                self.best_record = reaction_time
                print("최고 기록!")
            else:
                print(f"최고기록은 {self.best_record:.3f}초임")

