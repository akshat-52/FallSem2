d={}
n=int(input("Enter the Number of items you want to add in the dictionary : "))
for i in range(n):
    key=int(input("Please enter the key for item {}".format(i+1)))
    value=int(input("Please enter the value for item {}".format(i+1)))
    d[key]=value
print("The Dictionary is : ",d)
l=list(d.values())
print(l)
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("The Maximum value in the Dictionary : ",max) 
print("The Minimum value in the Dictionary : ",min)