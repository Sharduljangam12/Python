import multiprocessing

def EvenDisplay(No):
    print("listof even numbers :")
    x = 2
    for i in range(No):
        print(x)
        x = x+2

def OddDisplay(No):
    print("list of odd numbers :")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2

def main():
    print("Enter number : ")
    Value = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay,args = (Value))
    p2 = multiprocessing.Process(target= OddDisplay,args = (Value
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ))