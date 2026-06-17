contacts = {}

try:
     with open("contact.txt", "r", encoding = "utf-8") as file:
          for line in file:
               name, phone = line.strip(). split(",")
               contacts[name] = phone
except FileNotFoundError:
     pass
               

def save_contacts():
     with open("contact.txt", "w", encoding = "utf-8") as file:
          for name, phone in contacts.items():
               file.write(f"{name},{phone}\n")


def add_contact():
        name = input("이름: ")
        phone = input("전화번호: ")
 
        contacts[name] = phone

        save_contacts()
        pass

def show_contact():
        print(f"your contacts --> {contacts}")

        
        pass

def find_contact():
        n = input("Name: ")
        if n in contacts:
            print(f"{n} --> {contacts[n]}")
        else:   
            print("없음")

        
        pass

def delete_contact():
        d = input("Your name: ")

        if d in contacts:
            del contacts[d]
            print("삭제완료")
        else:
            print("다시 시도해")

            save_contacts()
        pass

def h_contact():
     length = len(contacts)
     print(f"연락처 개수는! {length}개야")


while True:

    print("1. 연락처 추가")
    print("2. 연락처 조회")
    print("3. 연락처 검색")
    print("4. 연락처 삭제")
    print("5. 연락처 개수")
    print("6. 종료")

    try:
        number = int(input("Select your number: "))
    except ValueError:
        print("숫자만 입력하세요.")
        continue

    if number == 1:
        add_contact()

    elif number == 2:
        show_contact()

    elif number == 3:
        find_contact()

    elif number == 4:
        delete_contact()

    elif number == 5:
        h_contact()

    elif number == 6:
         break

    else:
        print("다시 번호 입력해")
