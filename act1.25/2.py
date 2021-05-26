def vowels_count(string):
    vowels=['a','e','i','o','u']
    vc=0
    for i in string:
        if i in vowels:
            vc+=1
    print("The number of vowels character in a given string : ",vc)

def numeric_count(string):
    nc=0
    for i in string:
        if i.isdigit():
            nc+=1
    print("The number of numeric digits in a given string : ",nc)

inp=input("Enter a String : ")
vowels_count(inp)
numeric_count(inp)