def swap_numbers(a,b):
    c=a
    a=b
    b=c
    print("Values inside funtion.")
    print("a=",a)
    print("b=",b)
a=20
b=5
print("Values before funvtion call : ")
print("a=",a)
print("b=",b)
swap_numbers(a,b)
print("Values after function call : ")
print("a=",a)
print("b=",b)


string="Switjerland"
print("Outside function (before calling the function) : ",string)
def test(string):
    string="I Love Switjerland"
    print("Inside function : ",string)
test(string)
print("Outside function (after calling the function) : ",string)


def list_function(sub_list):
    sub_list.append("Physics")
    print("List Items Inside The Function : ")
    print(subject_list)
subject_list=["English","Computer"]
print("List items before function call : ")
print(subject_list)
list_function(subject_list)
print("List items after function call : ")
print(subject_list)


total=0
def sum(arg1,arg2):
    total=arg1+arg2;
    print("Inside the function local - total : ",total)
sum(10,20)
print("Outside the function - global total : ",total)