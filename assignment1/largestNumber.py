# 1. Write a program that ask for three numbers and prints 
# the largest using a function.
def largest(numbers):
    large=numbers[0]
    for num in numbers:
        if num>large:
            large=num
    print("Largest number is:",large)

a=int(input("Enter number-a:"))
b=int(input("Enter number-b:"))
c=int(input("Enter number-c:"))
numbers=[a,b,c]
largest(numbers)