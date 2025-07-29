
def main():
        
    try: #exception block
        print("enter first number :")
        No1 = int(input())

        print("enter second number:")
        No2 = int(input())

        Ans = No1 / No2
            
    except ZeroDivisionError as zobj:
        print("e=Exception occured",zobj)

    except ValueError as vobj:
        print("Exception occured : ",vobj)

    except Exception as eobj:
        print("Excetion occured ",eobj)

#the out is not accurate check with the codddddddddddddddddddddddddddde of class
    print("Division is : ",Ans)

if __name__ == "__main__":
    main()