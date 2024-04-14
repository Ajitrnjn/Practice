# from studentDetails.address_details import Address
# from studentDetails.student_details import Student
from pythonProject.studentDetails.address_details import Address
from pythonProject.studentDetails.student_details import Student

if __name__ == "__main__":
    area = input("Enter area name: ")
    pinCode = input("Enter pincode: ")
    district = input("Enter district: ")
    state = input("Enter state: ")
    address = Address(area, pinCode, district, state)
    address1 = Address(area="Hsr", pincode="560102", district="Bengaluru",
                       state=" Karnatka ")
    print(vars(address1))
    student = Student("Ajit", 27, 1, "Mr. Munna Kumar", " Mrs. Manju Devi ", address)
    #print(student.address.district)
    print(vars(student))
    print(vars(student.address))
