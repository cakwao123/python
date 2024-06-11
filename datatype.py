#Datatype

number = 78  #Int
num = 45.09  #Float
greeting = "How are you doing" #str
IsProgrammingIntresting =True  #bool

devices = ["laptop","computer","tablet","phone"]  #List
browser =("opera","firefox","safari","brave") #Tuple the list is ordered
counties = {"kenya","uganda","tanzania"} # set
employee = {
    "firstname" : "jane",
    "age" : 29,
    "nationality" : "kenyan",
    "emailaddress" : "jane2gmail.com"
} # Dictionary

print(IsProgrammingIntresting)
print(num)
print(counties)
print(employee["firstname"])
# Determine a datatype
print(type(counties))
print(type(employee))
# Typecasting is the process of converting one datatype to another

print(int(num))
print(float(number))