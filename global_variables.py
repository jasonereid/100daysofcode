# global vs local variables

# global variables are defined outside any functions, and can be called to be used in a function
# using the global keyword will set a variable as global inside a function

def my_Funct():
    global x
    x = "this is a global function"

my_Funct()

print(x)

# an example of using non-global variables
# you can see that the variable does not carry its value beyond the scope of the Function

y = "not the same as it is in my_Funct2"
print(y)
def my_Funct2():
    y = "local only, not global"
    print(y)
    
my_Funct2()
print(y)
