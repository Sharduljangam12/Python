from functools import reduce#library

def main():
 Data = [11,14,20,23,18,16,15,20]
 print("Data from input list :",Data)

 FData = list(filter(lambda No : (No % 2 == 0),Data))#Inbuilt function]
 print("Data after filter activity :",FData)

 MData = list(map(lambda No: No+1,FData))
 print("Data after map activity:",MData)

#15,21,19,17,21
#0+15 =15
#15 + 21 = 36
#36 +19 =51
#51 + 17 =72
#72 + 21=93
 RData = reduce( lambda A,B : A+B
,MData)
 print("Data after reduce activity is :",RData)

if __name__ == "__main__":#starter 
 main()