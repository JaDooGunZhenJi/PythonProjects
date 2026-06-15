todos = []
done_todos = []

try:
    with open("todolist.txt", "r", encoding = "utf-8") as file:
        for line in file:
            todos.append(line.strip())
except FileNotFoundError:
    pass

def save_todo():
    with open("todolist.txt", "w", encoding = "utf-8") as file:
        for todo in todos:
            file.write(todo + "\n")
    print("저장완료")

def add_todo():

    a = input("할것: ")
    todos.append(a)

    
    

def list_todo():
    if len(todos) == 0:
        print("할거 없음")
    else:
        for i, todo in enumerate(todos, start = 1):
            print(f"{i}. {todo}")

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
            print(f"{i}.{done_todos}")

    

def delete_todo():
    c = int(input(f"지우고싶은거 번호쓰셈 --> {todos}"))

    if 1 <= c <= len(todos):
        del todos[c - 1]
        print("삭제 완료함")

    else:
        print("없는 번호임")

    

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
        print("번호 입력하셈")
