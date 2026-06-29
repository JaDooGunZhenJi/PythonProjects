import json
from datetime import date
from pathlib import Path

FILEPATH = Path(__file__).parent / "healthrecord.json"

health = {}

def load_health():
    global health
    if FILEPATH.exists():
        with open(FILEPATH, "r", encoding="utf-8") as file:
            data = json.load(file)
           
            if all(isinstance(v, dict) for v in data.values()):  # 옛날 구조(값이 dict가 아닌 경우)면 무시하고 새로 시작함
                health = data
            else:
                print("구버전 데이터 형식이라 초기화함.")
                health = {}

def save_health():
    with open(FILEPATH, "w", encoding="utf-8") as file:
        json.dump(health, file, ensure_ascii=False, indent=2)

def save_text_log():
    today = str(date.today())
    if today not in health:
        print("오늘 입력된 기록이 없음.")
        return
    with open(Path(__file__).parent / "healthlog.txt", "a", encoding="utf-8") as file:
        file.write(f"\n날짜: {today}\n____________\n")
        for name, record in health[today].items():
            file.write(f"{name} = {record['무게']}, 횟수 = {record['횟수']}\n")

def chastchoise():
    today = str(date.today())
    record = health.get(today, {})  # 오늘 기록이 있으면 가져오고, 없으면 새로 시작

    banch = input("벤치 무게(순서대로) = ")
    record["벤치"] = {"무게": banch, "횟수": int(input("횟수: "))}

    upchast = input("윗가슴 무게 = ")
    record["윗가슴"] = {"무게": upchast, "횟수": int(input("횟수: "))}

    middlec = input("가운데 무게 = ")
    record["가운데"] = {"무게": middlec, "횟수": int(input("횟수: "))}

    tricepsc = input("삼두 무게 = ")
    record["삼두"] = {"무게": tricepsc, "횟수": int(input("횟수: "))}

    adbc = int(input("복근 횟수 = "))
    record["복근"] = {"무게": "-", "횟수": adbc}  # 무게 없는 운동은 "-"로 표시

    health[today] = record


def backchoise():
    today = str(date.today())
    record2 = health.get(today, {})

    latb = input("랫풀다운 무게 = ")
    record2["랫풀다운"] = {"무게": latb, "횟수": int(input("횟수: "))}

    tbarrowb = input("바벨로우 무게 = ")
    record2["바벨로우"] = {"무게": tbarrowb, "횟수": int(input("횟수: "))}

    seatedb = input("시티드로우 무게 = ")
    record2["시티드로우"] = {"무게": seatedb, "횟수": int(input("횟수: "))}

    onearmb = input("원암로우 무게 = ")
    record2["원암로우"] = {"무게": onearmb, "횟수": int(input("횟수: "))}

    reardeltb = input("후면 삼각근 무게 = ")
    record2["후면 삼각근"] = {"무게": reardeltb, "횟수": int(input("횟수: "))}

    sholderb = input("측면 어깨 무게 = ")
    record2["측면어깨"] = {"무게": sholderb, "횟수": int(input("횟수: "))}

    health[today] = record2   


def legchoise():
    today = str(date.today())
    record3 = health.get(today, {})

    squatl = input("스쿼트 무게 = ")
    record3["스쿼트"] = {"무게": squatl, "횟수": int(input("횟수: "))}

    legPl = input("레그프레스 무게 = ")
    record3["레그프레스"] = {"무게": legPl, "횟수": int(input("횟수: "))}

    legEl = input("레그익스 무게 = ")
    record3["레그익스"] = {"무게": legEl, "횟수": int(input("횟수: "))}

    legCl = input("레그컬 무게 = ")
    record3["레그컬"] = {"무게": legCl, "횟수": int(input("횟수: "))}

    hipTl = input("힙쓰러스트 무게 = ")
    record3["힙쓰러스트"] = {"무게": hipTl, "횟수": int(input("횟수: "))}

    abdl = input("어브덕터 무게 = ")
    record3["어브덕터"] = {"무게": abdl, "횟수": int(input("횟수: "))}

    health[today] = record3  

while True:
    n = int(input("1.입력(가슴날) 2.입력(등날) 3.입력(하체날) 4.저장 5.종료\n선택: "))

    if n == 1:
        chastchoise()

    elif n == 2:
        backchoise()

    elif n == 3:
        legchoise()

    elif n == 4:
        save_health()       # JSON 파일에 데이터 저장 (다음에 불러올 수 있게)
        save_text_log()      # 텍스트 로그에 구분선 있게 기록
        print("저장됌.")

    elif n == 5:
        break