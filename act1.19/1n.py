country_list=["India","Austria","Canada","Italy","Japan","France","Germany","Switzerland","Sweden","Denmark","Egypt","Algeria","Burma","Madagascar","Sri Lanka"]
print(country_list)
c='yes'
while c == "yes":
    val = input("\n Enter the country name to be removed:").capitalize()
    if val in country_list:
        country_list.remove(val)
        print("Country Removed")
    else:
        print("The given country is not in the list")
        print("Enter a country in the list to remove")
        continue
    c=input("Do you like to remove another country (yes/no) : ")
print("List after removing the countries")
print(country_list)