class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.__name} ({self.__age} tuoi)"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grades = []

    def add_grade(self, score):
        if 0 <= score <= 10:
            self.__grades.append(score)
        else:
            print("Diem khong hop le (0-10).")

    def average(self):
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0

    def classify(self):
        avg = self.average()
        if avg >= 8: return "Gioi"
        elif avg >= 6.5: return "Kha"
        elif avg >= 5: return "Trung binh"
        else: return "Yeu"

    def __str__(self):
        return f"[{self.__student_id}] {super().__str__()} - Diem TB: {self.average():.2f} ({self.classify()})"

    def get_id(self):
        return self.__student_id


class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for s in self.students:
            if s.get_id() == student_id:
                self.students.remove(s)
                return True
        return False

    def find_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())

    def sort_students(self):
        self.students.sort(key=lambda s: s.average(), reverse=True)

    def show_all(self):
        print(f"\nDanh sach lop {self.class_name}:")
        if not self.students:
            print("Chua co sinh vien nao.")
        for s in self.students:
            print(s)


def average_procedural(grades):
    return sum(grades) / len(grades) if grades else 0


def main():
    classroom = Classroom("Python OOP")

    while True:
        print("\n===== MENU QUAN LY SINH VIEN =====")
        print("1. Them sinh vien")
        print("2. Nhap diem cho sinh vien")
        print("3. Hien thi danh sach sinh vien")
        print("4. Sap xep theo diem trung binh")
        print("5. Tim sinh vien gioi nhat")
        print("6. Xoa sinh vien theo ma so")
        print("7. So sanh Procedural vs OOP (trung binh)")
        print("0. Thoat")

        choice = input("Chon: ")

        if choice == "1":
            name = input("Nhap ten: ")
            age = int(input("Nhap tuoi: "))
            sid = input("Nhap ma SV: ")
            sv = Student(name, age, sid)
            classroom.add_student(sv)
            print("Da them sinh vien.")

        elif choice == "2":
            if not classroom.students:
                print("Chua co sinh vien nao.")
                continue
            for i, sv in enumerate(classroom.students):
                print(f"{i+1}. {sv}")
            idx = int(input("Chon sinh vien de nhap diem: ")) - 1
            if 0 <= idx < len(classroom.students):
                score = float(input("Nhap diem: "))
                classroom.students[idx].add_grade(score)
                print("Da them diem.")
            else:
                print("Khong hop le.")

        elif choice == "3":
            classroom.show_all()

        elif choice == "4":
            classroom.sort_students()
            print("Da sap xep theo diem TB.")
            classroom.show_all()

        elif choice == "5":
            top = classroom.find_top_student()
            if top:
                print("\nSinh vien gioi nhat:")
                print(top)
            else:
                print("Chua co sinh vien.")

        elif choice == "6":
            sid = input("Nhap ma SV can xoa: ")
            if classroom.remove_student(sid):
                print("Da xoa sinh vien.")
            else:
                print("Khong tim thay sinh vien.")

        elif choice == "7":
            if not classroom.students:
                print("Chua co sinh vien nao.")
            else:
                sv = classroom.students[0]
                print("\nSo sanh Procedural vs OOP voi SV dau tien:")
                print("Procedural:", average_procedural([7, 8, 9]))
                print("OOP:", sv.average())

        elif choice == "0":
            print("Thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le, vui long nhap lai.")


if __name__ == "__main__":
    main()
