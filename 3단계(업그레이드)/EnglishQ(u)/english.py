import json
from pathlib import Path
import random
import requests

FILEPATH = Path(__file__).parent / "English.txt"


class WordBook:
        
        def __init__(self):
            self.words = {}


        def get_definition(self,word):
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
                return meaning
            else:
                return None

        def load_word(self):
            try:
                with open(FILEPATH, "r", encoding = "utf-8") as file:
                    self.words = json.load(file)
                print("불러오기 완료")
            except FileNotFoundError:
                print("저장된거 없음.")
        def save_word(self):
            with open(FILEPATH, "w", encoding = "utf-8") as file:
                json.dump(self.words, file, ensure_ascii = False, indent = 3)
            print("저장완료")
        
        def add_word(self):
            
            word = input("단어 입력 : ")

            eng_def = self.get_definition(word)
            if eng_def:
                print(f"영어 뜻: {eng_def}")
            else:
                print("사전에서 못 찾음, 직접 입력해야 해요")

            mean = input("한글 뜻 입력 : ")
            self.words[word] = mean
            
            print("추가 완료!")

        def search_word(self):
            search = input("검색: ")
            if search in self.words:
                print(f"{search}")
            else:
                print("해당 단어 찾지 못함.")

        def list_word(self):
            if self.words:
            
                print(f"단어 목록: {self.words}")
            else:
                print("등록된 단어가 없음.")

        def del_word(self):
            d = input("삭제 할 단어 : ")
            if d in self.words:
                del self.words[d] 
                print(f"{d} 삭제 완료")
            else:
                print("단어 찾지 못함.")


        def random_word(self):
            
            while True:
                word = random.choice(list(self.words.keys()))

                answer = input(f"{word}뜻: ")

                if answer == self.words[word]:
                    print("정답")
                    break
                else:
                    print("다시")

class WrongBook:

        def __init__(self):
            self.words = {}
            self.wrong = {}

        def unanswer_word(self):
            if len(self.wrong) == 0:
                print("오답 없음")
            else:
                for eng, kor in self.wrong.items():
                    print(f"{eng} : {kor}")

            


