my_set={"Akshat","Mtech","CSE"}
print(my_set)
print("\n")

my_set1={"Akshat","20MIS0183","20MIS0183","CSE1011"}
print(my_set1)
print("\n")

my_set3={"Akshat","akshat","20MIS0183","CSE1011"}
print(my_set3)
print("\n")

set1={"PHYSICS","CHEMSITRY","MATHEMATICS","EVS"}
print(len(set1))
print("\n")

set2={"VIT","MTECH","COMPUTER"}
print(set2)
print(type(set2))
print("\n")

set3={9,3,3,4,5,6,7,8,9}
print(set3)
print(type(set3))
print("\n")

set4={True,False,False,False}
print(set4)
print(type(set4))
print("\n")

set5={"Akshat","Mtech","CSE1011",18,True,"Male","India"}
print(set5)
print(type(set5))
print("\n")

set6={"VIT","MTECH","COMPUTER"}
for x in set6:
    print(x)
set7={9,3,3,4,5,6,7,8,9}
for x in set7:
    print(x)
set8={True,False,False,False}
for x in set8:
    print(x)
set9={"Akshat","Mtech","CSE1011",18,True,"Male","India"}
for x in set9:
    print(x)
print("\n")

set10={"Akshat","Mtech","CSE1011",18,True,"Male","India","Vellore"}
print("Vellore" in set10)
print("SRM" in set10)
print("\n")

set11={"Akshat","Mtech","CSE1011",18,True,"Male","India","Vellore"}
print(set11)
set11.add("52.akkey@gmail.com")
print(set11)
print("\n")

set12={"Akshat","Mtech","CSE1011"}
print(set12)
set13={"Flipkart","TCS","Wipro","Adobe"}
set12.update(set13)
print(set12)
print("\n")

set14={"INDIA","AMERICA","CHINA","RUSSIA"}
print(set14)
lst=["JAPAN","AUSTRIA"]
print(lst)
set14.update(lst)
print(set14)
print("\n")

set15={"STARS","SUN","MOON","GALAXY"}
print(set15)
set15.remove("SUN")
print(set15)
print("\n")

set16={"AKSHAT","VIT","CSE1011"}
print(set16)
set16.discard("VIT")
print(set16)

set17={"AKSHAT","CHIRAG","KIRUTHIK"}
print(set17)
m=set17.pop()
print("Removed Item : ",m)
print(set17)