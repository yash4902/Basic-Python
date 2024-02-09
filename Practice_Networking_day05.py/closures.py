# def functionA():
#     print ("Outer Function")
#     def functionB():
#         print("Inner Function")
#     functionB()
# functionA()


# def functionA(name):
#     print("Outer function")
#     def functionB():
#         print("Inner function")
#         print("Hello {}".format(name))
#     functionB()
# functionA("Python")



# def function(name):
#     name = "New Name"
#     def functionB():
#         print(name)
#     return functionB

# myfunction = function("My name")
# myfunction()



def functionA():
    counter = 0 
    def functionB():
        nonlocal counter
        counter += 1
        return counter 
    return functionB

myfunction = functionA()

retval = myfunction()

retval = 0
n = int(input("Enter the number how many times you want to print: "))
for i in range(n):
    retval += 1
    print("Counter: ",retval)