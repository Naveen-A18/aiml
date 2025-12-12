import math
n = int(input("enter th number"))
root = math.sqrt(n)
if (root*root == n):
    print("its is perfect squre")
else:
    print("its not perfect squre")
print(n**0.5)

#for true or false

num = 64
num2 = 65 
sqrt1 = num**0.5
sqrt2 = num2**0.5

print(sqrt1 * sqrt1 == num)
print(sqrt2 * sqrt2 == num2)