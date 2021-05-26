set1={"AKSHAT",18,"VIT","CSE1011"}
print(set1)
set2=set1.copy()
print(set2)
print("\n")

set3={"APPLE", "BANANA", "CHERRY", "WATERMELON", "PAPAYA"}
print(set3)
set4={"LEMON","BANANA","APPLE","CHERRY","TOMATO"}
print(set4)
set5=set3.difference(set4)
print(set5)
print("\n")

set6={1, 2, 3, 4, 5}
print(set6)
set7={1, 5, 6, 7, 8, 9, 10}
print(set7)
set8=set6.intersection(set7)
print(set8)
print("\n")

set9={10, 20, 30, 40, 50}
print(set9)
set10={30, 50, 60, 70, 80}
print(set10)
set9.intersection_update(set10)
print(set9)
print("\n")

set11={"A","B","C","D","E","F"}
print(set11)
set12={"G","H","I","J","K","L"}
print(set12)
set13=set11.isdisjoint(set12)
print(set13)
print("\n")

set14={"VIT","IIT","SRM","BITS","LPU"}
print(set14)
set15={"VIT"}
print(set15)
set16=set14.issuperset(set15)
print(set16)
print("\n")

set17={}