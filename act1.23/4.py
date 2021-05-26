num=int(input("Enter Number of Dictionary : "))
merge_dict={}
for i in range(num):
    d={}
    num_item=int(input("Enter Number of Items in The Dictionary : "))
    for j in range(num_item):
        key=input("Enter the key : ")
        value=input("Enter the Value")
        d[key]=value
    print("The Dictionary {} : ".formaat(i+1),d)
    for k in d:
        merge_dict[k]=d[k]
print("The Concatenation of Dictionaries : ",merge_dict)