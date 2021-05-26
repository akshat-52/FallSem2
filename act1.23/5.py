akshat_dict={'Name':'Akshat Kumar', 'Registration Number':"20MIS0183", 'Computer':99, 'Mathematics':95, 'Result':'PASS'}
print(akshat_dict)
check=input("Enter the key you want to check in the dictionary : " )
if check in akshat_dict:
    print("The key",check, "exists in the dictionary.")
else:
    print("Sorry",check, "doesn't exists in the dictionary.")