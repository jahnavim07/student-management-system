class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")


students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    marks = int(input("Enter marks: "))
    students.append(Student(name, roll, marks))
    print("Student added!")

def view_students():
    for s in students:
        s.display()

def search_student():
    roll = input("Enter roll to search: ")
    for s in students:
        if s.roll == roll:
            s.display()
            return
    print("Not found")

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
