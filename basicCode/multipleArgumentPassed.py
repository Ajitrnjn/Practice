def mult_arg(a,*b):
    x=a
    # print(b)
    for i in b:
        x = x + i
    print("sum of the number is :",x)

#mult_arg(5,7,8,9,10)

a=int(input("Enter a  "))
x = input("enter the value :")
print(x)

x = x.split(",")
print(type(x),type(x[0]))

list_int=[]
for k in x:
    print(k)
    list_int.append(int(k))
    print(list_int)

if len(list_int)>=3:
    mult_arg(a, list_int[0], list_int[1], list_int[2])



