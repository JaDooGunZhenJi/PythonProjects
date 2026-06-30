import json
from datetime import date
from pathlib import Path
import matplotlib.pyplot as plt

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

def get_last_record(name):
    for day in sorted(health.keys(), reverse=True):
        if name in health[day]:
            return health[day][name]                            # if, json, Path, date, exists(),isinstance(), items(), keys(), values(), for, sorted(),dump(),pop()return,get(),
    return None

def save_text_log():
    today = str(date.today())
    if today not in health:
        print("오늘 입력된 기록이 없음.")
        return
    with open(Path(__file__).parent / "healthlog.txt", "a", encoding="utf-8") as file:
        file.write(f"\n날짜: {today}\n____________\n")
        for name, record in health[today].items():
            file.write(f"{name} = {record['무게']}, 횟수 = {record['횟수']}\n")

def input_exercise(record, name, today):
    """운동 하나 입력받기. -1이면 취소 신호(None) 반환, 정상이면 record 반환"""
    last = get_last_record(name)
    if last:
        print(f"지난번: {last['무게']}kg, {last['횟수']}회")

    weight = input(f"{name} 무게 = ")
    if weight == "-1":
        health[today] = record
        print("입력을 취소하고 메뉴로 돌아갑니다.")
        return None  # 취소 신호

    record[name] = {"무게": weight, "횟수": int(input("횟수: "))}
    return record

def chastchoise():
    today = str(date.today())
    record = health.get(today, {})

    for name in ["벤치", "윗가슴", "가운데", "삼두"]:
        result = input_exercise(record, name, today)
        if result is None:
            return
        record = result

    adbc_input = input("복근 횟수 = ")
    if adbc_input == "-1":
        health[today] = record
        print("입력을 취소하고 메뉴로 돌아갑니다.")
        return
    record["복근"] = {"무게": "-", "횟수": int(adbc_input)}

    health[today] = record
    
def backchoise():
    today = str(date.today())
    record2 = health.get(today, {})

    for name in ["랫풀다운", "바벨로우", "원암로우", "후면 삼각근", "측면어깨", "이두"]:
        result = input_exercise(record2, name, today)
        if result is None:
            return
        record2 = result

    health[today] = record2


def legchoise():
    today = str(date.today())
    record3 = health.get(today, {})

    for name in ["스쿼트", "레그프레스", "레그익스", "레그컬", "힙쓰러스트", "어브덕터"]:
        result = input_exercise(record3, name, today)
        if result is None:
            return
        record3 = result

    health[today] = record3
    health[today] = record3


load_health()

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