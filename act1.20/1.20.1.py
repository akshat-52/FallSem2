list_of_cars=[]
print("Enter the car name of your choice: ")
a=1
for i in range(0,10):
    a=str(a)
    txt= "Car " + a + " : " 
    n=input(txt).capitalize()
    list_of_cars.append(n)
    a=int(a)
    a+=1
print("List of Cars without sorting (as given by user):")
print(list_of_cars,"\n")
print("List of Cars in ascending order:")
list_of_cars.sort()
print(list_of_cars,"\n")
print("List of Cars in descending order:")
list_of_cars.sort(reverse=True)
print(list_of_cars)