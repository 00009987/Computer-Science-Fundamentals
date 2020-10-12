# TEACHING WEEK 2

"""
Example 1: Define a function that takes an argument.
Call the function. Identify what code is the argument
and what code is the parameter.
"""

def example1(name, not_robot=True):
    # usage of argument
    if not_robot:
        print(f'{name} is not a robot')

    # usage of parameter
    print(f"User's name is {name}")


print("")

"""
Example 2: Call your function from Example 1 three times with
different kinds of arguments: a value, a variable, and an 
expression. Identify which kind of argument is which.
"""


def example2():
    
    # parameter and argument
    example1(False, True)

    # number-type parameter
    example1(10101001101)
    
    # string-type parameter
    example1("this is a string")


print("")

"""
Example 3: Create a function with a local variable.
Show what happens when you try to use that variable 
outside the function. Explain the results.
"""

example3_variable = 'Welcome to CSF'

def example3():
    print(f'The local variable says "{example3_variable}"')


print("")

"""
Example 4: Create a function that takes an argument.
Give the function parameter a unique name.
Show what happens when you try to use that parameter 
name outside the function. Explain the results.
"""

example4_variable = 'hi'

def example4(example4_variable):

    # When trying to use the existing parameter name as
    # the function's argument, function's argument will
    # shadow the existing variable "example4_variable"
    # from outer space, but if the type is specified it
    # still can be used properly

    print(f'I just wanted to say {example4_variable}')


print("")

"""
Example 5: Show what happens when a variable defined outside 
a function has the same name as a local variable inside a 
function. Explain what happens to the value of each variable 
as the program runs.
"""

example5_variable = 'hello'


def example5():
    example5_variable = 'world'

    # When creating a local variable inside a function with
    # the same name as the outer space, the former one shadows
    # the latter one.

    print(example5_variable)


example5()                  # print -> world
print(example5_variable)    # print -> hello