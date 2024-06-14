#inbuilt function/ standard library functions

y = min(23,56,1000,5467)
print(y)
x = max( 90,2,76,14)
print("the maximum number is", x)

z = pow(2,3)
print(z)
#user defined functions
def school():
    print("emobilis")
school()# calling a function

def multiply():
    num1 = 5
    num2 = 6
    print(num1*num2)
multiply()

# parameters and arguments
def add(a,b):
    print(a+b)
add(5,6)
add(4,6)
add(20,6)
def employee(fullname,age,salary,phoneno,position):
    print(fullname,age,salary,phoneno,position)
employee("carolyne k",20,50000,115123504,"MD")
employee("Job o",23,80000,724419956,"secretary")
employee("Danvas",27,100000,713059355,"sales person")