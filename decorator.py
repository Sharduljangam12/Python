
def sub(A,B): # 0x100
    print(A-B)
    
def SmartSub(fptr):#Decorator # 0x200
    def Inner(A,B):#0x300
        if A < B:
            A,B = B,A
        return fptr(A,B)
    return Inner#return 0x300

sub = SmartSub(sub) #SmartSub(0x100)``


def main():#0x400
    No1 = int(input("Enter 1st no"))
    No2 = int(input("Enter 2nd no"))

    sub(No1,No2) #0x300(1990,1992)

if __name__ == "__main__":
    main()