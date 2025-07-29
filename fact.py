#Factorial

i = 1
fact = 1

def Factorial(No):
    global i
    global fact

    if(No >= 1):
       fact = fact + No
       No = No - 1
       Factorial(No)


    return fact

def main():
    print("Enter the number:")
    sol = int(input())

    Ret = Factorial(sol)

    print("Factorial is : ",Ret)

if __name__ == "__main__":#starter 
 main()