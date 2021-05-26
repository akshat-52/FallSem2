f = open("D:\\demo\subject.txt")
for x in f :
    print(x)
f.close()
print("******************************************")

f = open("D:\\demo\subject.txt", "a")
f.write("\n")
f.write("EEE")
f.close()

f = open("D:\\demo\subject.txt")
print(f.read())
f.close()
