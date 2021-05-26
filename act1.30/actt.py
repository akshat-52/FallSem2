f=open("D:\\demo\\numbers_list.txt","a")
for x in range(1,11):
    a=int(input("Enter number to file {}: ".format(x)))
    f.write(str(a))
    f.write("\n")
f.close()    

f=open("D:\\demo\\numbers_list.txt")    
print(f.read())
f.close()

f=open("D:\\demo\\numbers_list.txt","r")
for x in f:
    if(x%2==0):
        f1=open("even_numbers_file.txt")
        f1.write(x)
print(f.read())