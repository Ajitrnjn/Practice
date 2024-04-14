# Start of class

class computer:
    def component(self):
        print("16 GB", "1 TB")


comp1 = computer()

computer.component(comp1)
comp1.component()  # calling method(function) , component pass as object then component check itself belongs to which class then pass in method


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name


student = Student("Ajeet", 27)
student.set_name("Raj")
student1 = Student("Ajeet", 27)
print(student.name, student.age)
print(student1.name, student1.age)
if student == student1:
    print("Both are same")
else:
    print("both are different")
