import csv

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        total = 0
        if len(self.grades) == 0:
            return 0
        for average in self.grades:
            total += average
        return total / len(self.grades)
        

    def to_dict(self):
        return{
            "name": self.name,
            "student_id": self.student_id,
            "grades": ",".join(str(g) for g in self.grades)
        }

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Grades: {self.grades} | Average: {self.get_average():.2f}"

    @classmethod
    def from_dict(cls, data):
        new_student = cls(data["name"], data["student_id"])

        if data["grades"] != "":
            for grade_str in data["grades"].split(","):
                new_student.add_grade(int(grade_str))
        return new_student

class GradeBook:
    def __init__(self):
        self.students = []
        self.filename = "grades.csv"

    def load_csv(self):
        try:
            with open(self.filename, mode="r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    new_student = Student.from_dict(row)
                    self.students.append(new_student)
        except FileNotFoundError:
            pass

    def save_csv(self):
        fieldnames = ["name", "student_id", "grades"]

        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for student in self.students:
                writer.writerow(student.to_dict())

    def add_student(self, student):
        self.students.append(student)

    def calculate_class_average(self):
        if len(self.students) == 0:
            return 0

        total_average = 0
        for student in self.students:
            total_average += student.get_average()
        return total_average / len(self.students)

def main():
    book = GradeBook()
    book.load_csv()

    while True:

        print("---STUDENT GRADEBOOK---")
        print("1. Add Student")
        print("2. View All")
        print("3. Class Average")
        print("4. Exit")


        option = input("Choose: ")

        if option == "1":
            name = input("Enter your name: ")
            student_id = input("Enter your student ID: ")

            new_student = Student(name, student_id)

            for i  in range(3):
                grade = int(input(f"Enter your {i+1} grade: "))
                new_student.add_grade(grade)
                
            book.add_student(new_student)
            book.save_csv()
            print("Student added successfully")

        elif option == "2":
            if len(book.students) == 0:
                print("No student in the gradebook yet.")

            else:
                for student in book.students:
                    print(student)

        elif option == "3":
            result = book.calculate_class_average()
            print(f"{result:.2f}")

        elif option == "4":
            print("Thanks for using STUDENT GRADEBOOK")
            break

        else:
            print("Invalid! Choose from 1-4")

if __name__ == "__main__":
    main()