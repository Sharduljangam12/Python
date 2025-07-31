#Write a function to reverse a string.
'''print("Enter the String you want to reverse:- ")
string = input()
print(string[::-1])'''
def reverse_string(s):
    return s[::-1]

x = input("Enter the string you want to reverse: ")
print("Reversed:", reverse_string(x))