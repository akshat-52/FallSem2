tuple1=('Akshat','20MIS0183','M.Tech Integrated','Software Engineering')
print(tuple1)
print(type(tuple1))

tuple2=(100,90,85,99,94)
print(tuple2)
print(type(tuple2))

print("Tuple1[0]: ",tuple1[0])
print("Tuple2[-1]: ",tuple2[-1])
print("Tuple2[0:4]: ",tuple2[0:4])

tuple3=(1.11,3.57,7.99,8.56)
print("Tuple3[1]: ",tuple3[1])

data_tuple=("AKSHAT","CHIRAG","KIRUTHIK")
print(data_tuple[0])
print(data_tuple[1])
print(data_tuple[2])
data_tuple[1]=3.14

tupl=("MATHS","PHYSICS","COMPUTER")
print("THE ORIGINAL TUPLE")
print(tupl)
print("\n")
a=list(tupl)
print("TUPLE AS A LIST")
print(a)
print("\n")
a[1]="HISTORY"
tupl=tuple(a)
print("TUPLE AFTER CHANGING ELEMENT")
print(tupl)

