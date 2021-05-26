d1={}
d2={}
for i in range(2):
    n=int(input("Enter the number of items in dictionary : ".format(i+1)))
    for x in range(n):
        key=input("Enter the key for item {} : ".format(x+1))
        value=int(input("Enter the value for {} items {} : ".format(key,x+1)))
        if i==0:d1[key]=value
        else:d2[key]=value
print("The Dictionary {} : ".format(1),d1)
print("The Dictionary {} : ".format(2),d2)
temp=0
d_combine={}
for j in d1:
    for k in d2:
        if j==k:
            d_combine[j]=d1[j]+d2[k]
            temp+=1
print("The Combined Dictionary : ",d_combine)
if temp==0:
    print("There is not any common key in the dictionary.")
