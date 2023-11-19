import os

def load_data():
    data = {}
    if os.path.exists("grades.txt"):
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                student_name = parts[0]
                subject = parts[1]
                grade = float(parts[2])
                if student_name not in data:
                    data[student_name] = {}
                data[student_name][subject] = grade
    return data

def save_data(data):
    with open("grades.txt", "w") as file:
        for student_name, subjects in data.items():
            for subject, grade in subjects.items():
                file.write(f"{student_name},{subject},{grade}\n")

def print_grades(data):
    print("\n====== 학생 성적 ======")
    for student_name, subjects in data.items():
        total_grade = 0
        num_subjects = len(subjects)
        for grade in subjects.values():
            total_grade += grade
        avg_grade = total_grade / num_subjects if num_subjects > 0 else 0
        print(f"{student_name}: {subjects}, 평균 성적: {avg_grade:.2f}")

def input_grade(data):
    student_name = input("학생 이름을 입력하세요: ")
    subject = input("과목을 입력하세요: ")
    try:
        grade = float(input("성적을 입력하세요: "))
    except ValueError:
        print("잘못된 성적 입력입니다. 숫자를 입력하세요.")
        return

    if student_name not in data:
        data[student_name] = {}

    data[student_name][subject] = grade
    print("성적이 입력되었습니다.")

def modify_grade(data):
    student_name = input("성적을 수정할 학생 이름을 입력하세요: ")
    if student_name not in data:
        print("해당하는 학생이 존재하지 않습니다.")
        return

    subject = input("수정할 과목을 입력하세요: ")
    if subject not in data[student_name]:
        print("해당하는 과목이 존재하지 않습니다.")
        return

    try:
        new_grade = float(input("새로운 성적을 입력하세요: "))
    except ValueError:
        print("잘못된 성적 입력입니다. 숫자를 입력하세요.")
        return

    data[student_name][subject] = new_grade
    print("성적이 수정되었습니다.")

def main():
    data = load_data()

    while True:
        print("\n====== 성적 관리 시스템 메뉴 ======")
        print("1. 학생 성적 출력")
        print("2. 성적 입력")
        print("3. 성적 수정")
        print("4. 성적 저장")
        print("5. 성적 불러오기")
        print("0. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            print_grades(data)
        elif choice == "2":
            input_grade(data)
        elif choice == "3":
            modify_grade(data)
        elif choice == "4":
            save_data(data)
            print("성적이 저장되었습니다.")
        elif choice == "5":
            data = load_data()
            print("성적이 불러와졌습니다.")
        elif choice == "0":
            save_data(data)
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()