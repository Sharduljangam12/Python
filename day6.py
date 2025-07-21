#This is a Grading System made with if-elif-else assign grades based on the score
x = int(input("Enter the Marks of Student : "))
if x >= 90:
    print("O")
elif x >= 75:
    print("A")
elif x >= 60:
    print("B")
elif x >= 45:
    print("C")
elif x >= 35:
    print("D")
else:
    print("Fail")