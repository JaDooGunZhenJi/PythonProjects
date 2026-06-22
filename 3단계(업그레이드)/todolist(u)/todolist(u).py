import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "todolist.json"

todos = []
done_todos = []

def load_todo():
    global todos
    try:
        with open(FILE_PATH, "r", encoding = "utf-8") as file:
            todos = json.load(file)
        print("불러오기 완!")
    except FileNotFoundError:
        print("저장된거 없음")

def save_todo():
    with open(FILE_PATH, "w", encoding = "utf-8") as file:
        json.dump(todos, file, ensure_ascii = False, indent = 2)
    print("저장완")
        

def add_todo():

    content = input("할것: ")
    deadline = input("마감일 (예: 2026-06-07) : ")
    todos.append({"내용": content, "마감일": deadline})
    print("추가완")

    
    
def list_todo():
    if len(todos) == 0:
        print("할거 없음")
    else:
        for i, todo in enumerate(todos, start = 1):
            print(f"{i}. {todo["내용"]} (마감: {todo["마감일"]})")

        print(f"총 {len(todos)}개")


def ok_todo():
    b = int(input("만약 했으면 번호 치셈: "))

    if 1 <= b <= len(todos):
        done = todos.pop(b - 1)
        done_todos.append(done)

        print("완료 처리함.")

    else:
        print("번호가 없음")
    


def confirm_todo():
     if len(done_todos) <= 0:
        print("완료한건 없음.")

     else:
         for i, todo in enumerate(done_todos, start = 1):
            print(f"{i}.{todo["내용"]} (마감: {todo["마감일"]})")

    

def delete_todo():
    c = int(input(f"지우고싶은거 번호쓰셈 --> {todos}"))

    if 1 <= c <= len(todos):
        del todos[c - 1]
        print("삭제 완료함")

    else:
        print("없는 번호임")

load_todo()

    

while True:

    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 완료")
    print("4. 완료된 일 보기")
    print("5. 할 일 삭제")
    print("6. 저장")
    print("7. 종료")

    try:
        d = int(input("번호 선택하셈: "))
    except ValueError:
        print("다시 하시오.")
        continue

    if d == 1:
         add_todo()

    elif d == 2:
         list_todo()

    elif d == 3:
         ok_todo()
    
    elif d == 4:
         confirm_todo()

    elif d == 5:
         delete_todo()

    elif d == 6:
        save_todo()

    elif d == 7:
        break

    else:
        print("1~7번까지 입력하셈")
