num1 =float(input("enter the first number"))
operator=input(["+","-","*","/","%"])
num2 = float(input("enter the second number"))
if operator == "+":
     print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator == "/":
    if num2 == 0:
        print(0)
    else:
        print(num1/num2)
elif operator =="%":
    print(num1%num2)
else:
    print("Invalid operator")
