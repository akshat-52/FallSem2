def addition(a,b):
    n=a+b
    print("Sum : ",n)
def subtraction(a,b):
    n=a-b
    print("Diffrence : ",n)
def multiplication(a,b):
    n=a*b
    print("Product : ",n)
def division(a,b):
    n=a/b
    print("Quotient : ",n)
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
print("""
Choice 1 - SUM
Choice 2 - DIFFERENCE
Choice 3 - PRODUCT
Choice 4 - QUOTIENT
 """)
choice=int(input("Enter the number of your choice : "))
if choice==1:
    addition(num1,num2)
elif choice==2:
    subtraction(num1,num2)
elif choice==3:
    multiplication(num1,num2)
elif choice==4:
    division(num1,num2)
else:
    print("Invalid Choice !!! Please choose 1/2/3/4 only .")