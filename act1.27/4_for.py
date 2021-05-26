college_list=[]
college_tuple=()
num=int(input("Enter the number of Engeering Colleges you want to add in Tuple : "))
for i in range(1,num+1):
    col=input("Enter the name of college {} : ".format(i))
    if col not in college_list:
        college_list.append(col)
        college_tuple=tuple(college_list)
        print(college_tuple)
    