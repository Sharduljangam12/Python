CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No: No+1
Add = lambda A,B : A+B

#Task : Name of function
#
def filterX(Task,Elements):
 Result = []

 
 for no in Elements:
  Ret = Task(no)

  if(Ret == True):
   Result.append(no)

 return Result

def mapX(Task,Elements):
 Result = []
 
 for no in Elements:
  Ret = Task(no)
  Result.append(Ret)

def reduceX(Task,Elements):
 Sum = 0

 for no in Elements:
  Sum = Task(Sum,no)
  
  return Sum


def main():
 Data = [11,14,20,23,18,16,15,20]
 print("Data from input list :",Data)

 FData = list(filterX(CheckEven,Data))#Inbuilt function]
 print("Data after filter activity :",FData)

 MData = list(mapX(Increase ,FData))
 print("Data after map activity:",MData)

 RData = reduceX(Add,MData)
 print("Data after reduce activity is :",RData)

if __name__ == "__main__":#starter 
 main()