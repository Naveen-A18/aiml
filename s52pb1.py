# Write a program to find the greatest of four numbers entered by the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if a > b and a > c and a > d:
    print("a is greatest")
elif b > c and b > d:
    print("b is greatest")
elif c > d:
    print("c is greatest")
else:
    print("d is greatest")
