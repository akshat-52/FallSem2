
country_list=["India","Austria","Canada","Italy","Japan","France","Germany","Switzerland","Sweden","Denmark","Egypt","Algeria","Burma","Madagascar","Sri Lanka"]
print(country_list)
c='yes'
while c == "yes":
    val = int(input("\n Enter the index value to be removed :"))
    if country_list[val] in country_list:
        print(country_list[val],"Removed")
        country_list.pop(val)
        print(country_list)
    else:
        print("The given index is out of the range.")
        print("Enter a correct index value")
        continue
    c=input("Do you like to remove another company (yes/no) : ")
print("List after removing the countries from the list")
print(country_list)