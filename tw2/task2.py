# creating a function that prints a new blank line
def new_line():
    print('')


# a function that prints three new lines
def three_lines():
    # using for loop to repeatedly call the function
    # variable line keeps track of how many lines printed
    for line in range(3):
        new_line()


# a function that prints three new three-lines
def nine_lines():
    # using for loop to repeatedly call the function
    # variable line keeps track of how many lines printed
    for line in range(3):
        three_lines()


# a function that prints new 25 empty lines
def clear_screen():
    # printing the 1st line
    new_line()

    # printing the lines 2-7
    for line in range(2):
        three_lines()

    # printing the lines 8-25
    for line in range(2):
        nine_lines()


clear_screen()