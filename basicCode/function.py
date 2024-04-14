# def add(x,y):
#     x = int(input("Enter the value of x :"))
#     y = int(input("Enter the value of y:"))
#     c=x+y
#     # print(c)
#     return c
#
#
# result = add(5,4)
# print("sum of two number is : ",result)


# call by value and call by reference

# def update(x):
#     x=int(input("enter the value :"))
#     print(x)
#
# update(20)


def update(lst):
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x",lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst",lst)

