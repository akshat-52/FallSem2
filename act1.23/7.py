d={}
n=int(input("Enter the number of items you want to enter in the dictionary :"))
for i in range(n):
    key=int(input("Please enter the key for item {}".format(i+1)))
    value=int(input("Please enter the value for item {}".format(i+1)))
    d[key]=value
print("The Dictionary is : ",d)
key_product=1
value_product=1
for j in d:
    key_product=key_product*j
    value_product=value_product*d[j]
print("The Product of Keys : ",key_product)
print("The Product of Values : ",value_product)
print("Net Multiplication of items : ",key_product*value_product)