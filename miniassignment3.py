a=int(input("Enter a:"))
b=int(input("Enter b:"))
# 1
print(a+b)
print(a-b)
print(a*b)
# 2
if a%b==0:
    print("DIvisible")
else:
    print("Not Divisible")
# 3
if a%b==0 and b%2==0:
    print("Both Even")
else:
    print("NOt both Even")