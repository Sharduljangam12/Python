#Write a function to find the largest element in an array.
'''def find_largest(arr):
    if not arr:
        return None
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
        return max_value
    
arr = [50,17,87,30,10,20]
print("Array:", arr)
print("Largeset Element in Array is: ",find_largest(arr))'''

#This is code in which the user gives the input 
def find_largest():
    arr = input("Enter the numbers separated by space: ").split()
    arr = [int(x) for x in arr]
    
    if not arr:
        print("Empty list!")
        return

    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num

    print("Largest number in the list:", max_value)

find_largest()
