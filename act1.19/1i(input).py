country_list=["India","Austria","Canada","Italy","Japan","France","Germany","Switerland","Sweden","Denmark"]
print("Current list before adding 5 countries name: ")
print(country_list,"\n")
a=1
while a<=5:
    a=str(a)
    txt="Enter name of the Country "+ a +" :"
    n=input(txt).capitalize()
    if n not in country_list:
        country_list.append(n)
    else:
        print("Please enter another country's name. This already exists in the list !!!!")
        a=int(a)
        continue
    a=int(a)
    a+=1
print("\n")
print("List after adding 5 countries name.")
print(country_list)