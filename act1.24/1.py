def list_num(function_processing_numbers):
    pos=0
    neg=0
    odd=0
    eve=0
    for n1 in function_processing_numbers:
        if n1<0:
            neg=neg+n1
        else:
            pos=pos+n1
    for n2 in function_processing_numbers:
        if n2%2==0:
            eve=eve+n2
        else:
            odd=odd+n2
    
    print("Sum of all Positive Numbers : ",pos)
    print("Sum of all Negative Numbers : ",neg)
    print("Sum of all Odd Numbers : ",odd)
    print("Sum of all Even Numbers : ",eve) 

limit=int(input("Enter number of terms required : "))
list_numbers=[]
print("Enter {} values".format(limit))
i=1
while i<=limit:
    n=int(input("Enter Value {} : ".format(i)))
    if n not in list_numbers:
        list_numbers.append(n)
    else:
        print("You have already entered this value")
        print("Try Another Value")
        continue
    i+=1
list_num(list_numbers)