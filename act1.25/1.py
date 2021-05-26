def list_sort(f_list):
    print("Hello Programmers !! Welcome to my program")
    print("You have to make choice between 1 or 2")
    print("<<< Choice 1 to sort elements in Ascending order >>>")
    print("<<< Choice 2 to sort elements in Descending order")
    choice=int(input("Enter your choice (1 or 2) : "))
    if choice==1:
        print("<<< List Before Sorting >>>")
        print(f_list)
        print("<<< List in Ascending Order >>>")
        f_list.sort()
        print(f_list)
    elif choice==2:
        print("<<< List Before Sorting >>>")
        print(f_list)
        print("<<< List in Descending Order >>>")
        f_list.sort(reverse=True)
        print(f_list)
    else:
        print("<<< Please Choose between 1 and 2 only !!! >>>")

element_list=[]
limit=int(input("Enter number of elements needed to arrange : "))
i=1
while i<=limit:
    n=int(input("Enter Value {} : ".format(i)))
    if n not in element_list:
        element_list.append(n)
    else:
        print("<<< This value is already in the list !!!!>>>")
        print("<<< Try Another Number !!! >>>")
        continue
    i=i+1
print("<<< List Created Successfully >>>")
print("<<< List of Numbers >>>")
print(element_list)