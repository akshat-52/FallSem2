n=int(input("Enter the number of items for Dictionary : "))
d={}
for i in range(n):
    key=int(input("Enter the key of the item : "))
    value=input("Enter the value of the item : ")
    d[key]=value
d1=d.copy()
for x,y in d1.items():
    check=y
    for j in d:
        if check==d[j]:
            d.pop(check)
print("The Dictionary : ",d)