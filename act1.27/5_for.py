number_tuple=()
number_list=[]
for i in range(100,200):
    if i%2==0:
        number_list.append(i)
        number_tuple=tuple(number_list)
        print(number_tuple)