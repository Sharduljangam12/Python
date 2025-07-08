# 3. Given a tuple of numbers, find the sum of all even numbers.
#numbers = (10, 15, 22, 33, 40)
# Expected Output: 72
numbers = (10, 15, 22, 33, 40)
sum_even = 0

for num in numbers:
    if num %  2 == 0:
        sum_even += num

print(sum_even)
