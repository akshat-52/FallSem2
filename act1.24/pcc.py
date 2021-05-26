def my_first_function():
    print("\n This is my first function")
my_first_function()

def my_function(frnd_name):
    print(frnd_name + " is my friend")

my_function("Chirag")
my_function("Kiruthik")
my_function("Khushi")

def my_funct2(fname, lname):
    print(fname + " " + lname)
my_funct2("AKSHAT", "KUMAR")

def funct3(country = "India"):
    print("I am from " + country)
funct3("Sri Lanka")
funct3("Norway")
funct3()
funct3("Brazil")

def my_function(subjects):
     for x in subjects:
         print(x)
subjects = ["Science", "Mathematics", "Chemistry"]
my_function(subjects)

def cube_of_number(x):
    return x*x*x
print(cube_of_number(2))
print(cube_of_number(3))
print(cube_of_number(10))

def add_sub(option,n1,n2):
    if(option==1):
        return(n1-n2)
    else:
        return(n1+n2)
print(add_sub(1,9,6))
print(add_sub(11,9,6))
print(add_sub(1,2,3))
print(add_sub(2,2,3))

def akshat():
    pass