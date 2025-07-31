#Write a function to count vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0 
    for char in s:
        if char in vowels:
            count += 1
    return count

num_vowels = input("Enter the String to count vowels: ")
vowel_count = count_vowels(num_vowels)
print("Number of vowels:", vowel_count)