d={}
n=int(input("Enter the number of items needed : "))
for i in range(n):
    key=int(input("Enter the Key : "))
    value=int(input("Enter the value : "))
    d[key]=value
print("Dictionary before sorting : ",d)
l=list(d.items())
l.sort()
d=dict(l)
print("The Dictionary sorted in ascending order :",d)
l.sort(reverse=True)
d=dict(l)
print("The Dictionary sorted in descending order :",d)