from encapsulation import Student

if __name__ == "__main__":
    student = Student("Ajeet", 2)
    print("Inside different pacakge")
    print(student._name, student.roll)
