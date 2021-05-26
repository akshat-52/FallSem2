f = open("D:\\demo\course.txt")
print(f.read())
print("******************************************")

g = open("D:\\demo\myinfo.txt")
print(g.read())
print("******************************************")

h = open("D:\\demo\myinfo.txt")
print(h.read(4))
print("******************************************")

i = open("D:\\demo\myinfo.txt")
print(i.read(4))
print(i.read(5))
print(i.read(5))
i.close()
print("******************************************")

a = open("D:\\demo\states.txt")
print(a.readline())
f.close()
print("******************************************")

dem = open("D:\\demo\states.txt")
print(dem.readline())
print(dem.readline())
print(dem.readline())
f.close()
print("******************************************")

dem1 = open("D:\demo\states.txt")
for x in dem1:
    print(x)
f.close()
print("******************************************")

dem2 = open("D:\\demo\states.txt")
print(dem2.readline())
print(dem2.readline())
dem2.close()
print(dem2.readline())