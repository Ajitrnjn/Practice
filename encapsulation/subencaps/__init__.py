from encapsulation import Student

if __name__ == "__main__":
    student = Student("Ajeet", 2)
    print("Inside sub package")
    print(student._name, student.roll)
