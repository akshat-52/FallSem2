college_list=[]
college_tuple=()
col=int(input("Enter the number of colleges you want to tuple : "))
print("Enter name of College : ")
i=1
while i<=col:
    n=input("Name {} :".format(i))
    if n not in college_list:
        college_list.append(n)
    else:
        print("This is already entered !! Try another name")
        continue
    college_tuple=tuple(college_list)
    print(college_tuple)
    i+=1 