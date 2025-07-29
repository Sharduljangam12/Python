from addcommand import Addition


def main():
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum
    
def main():
    print("Enter the number of elements that you want to enter in list")
    size = int(input())

    Arr = list()

    print("Enter the elements : ")

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

    Result("Enter elements are : ",Arr)
    Result = Addition(Arr)
    print("Summation of all elements : ",Result)

if __name__ == "__main__":
    main()
    #practice each and every mentioned mentioned in documentation and code all o
    