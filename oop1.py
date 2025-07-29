
class Demo:
    Data1 = 11
    Data2 = 21

    def __init__(self, A,B):
        print("Inside constructor")self.No1 = A
        self.No2 = B



obj1 = Demo(5,10)

obj2 = Demo(15,20)

print("Value of No1 from obj1 : ",obj1.No1)
#incomplete