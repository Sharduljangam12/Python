#Types of fuction arguments
# 1 : Positional arguments
# 2 : Keyword arguments
# 3 : Default arguments
# 4 : Variable number of arguments


def Information(Name, Age, Salary):
    print("Name is: ",Name)
    print("Age is:",Age)
    print("Salary is:",Salary)


Information("Amit",42,90000)

Information("Pooja",27,70000)

Information(Age = 31,Salary = 700000,Name = "Sagar")