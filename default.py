
def Area(Radius, PI = 3.14):#default
    Result =  PI * Radius * Radius
    return Result 

Ans = Area(10.7)#positional
print("Area of circle is : ",Ans)


Ans = Area(10.7,7.20)#positoinal
print("Area of circle is : ",Ans)


Ans = Area(Radius = 10.7)#keyword
print("Area of circle is : ",Ans)