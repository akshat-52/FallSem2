student_dict={ 
    "Name": "Akshat",
    "Reg No":"20MIS0183",
    "Mathematics":100,
    "Science":95,
    "Computer":99,
    "Result": "PASS"
 }
print("\nInitial Dictionary")
print(student_dict)

student_dict.update({"Mathematics":24})
student_dict.update({"Result":"FAIL"})

print("\nDictionary after using update()")
print(student_dict)

print("\nRemoving the Computer from the list")
student_dict.pop("Computer")
print("Dictionary after using pop()")
print(student_dict)

print("\nDictionary after using popitem()")
student_dict.popitem()
print(student_dict)

print("\nDictionary after deleting name")
del student_dict["Name"]
print(student_dict)

print("\nDictionary after using clear()")
student_dict.clear()
print(student_dict)

student_dict={ 
    "Name": "Akshat",
    "Reg No":"20MIS0183",
    "Mathematics":100,
    "Science":95,
    "Computer":99,
    "Result": "PASS"
 }
 
print("\nRecreating the Dictionary")
print(student_dict)

print("\nCopying Student Dictionary using copy()")
student_dict1=student_dict.copy()
print("New Dictionary")
print(student_dict1)
print("\nCopying Student Dictionary using dict()")
student_dict2=dict(student_dict)
print("New Dictionary")
print(student_dict2)