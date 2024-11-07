# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

class math:
    
    def __init__(self, input, a, an, m, x, b):
        self.input = input
        self.a = a  #lower bound
        self.an= an #upper bound
        self.x = x
        self.b = b
        self.m = m

    def int_check(input):   #PART ONE CONDITIONS
        if "." in input:
            print(f"{(float(input)):.1f} is a float.")
            return True

        elif "-" in input:
            num = int(input)
            print(f"{num} is an integer.")
            return True

        elif input.isdigit():
            print(f"{input} is an integer.")
            return True

        else:
            print("ERROR: Numeric Values Only!")
            return False
        
    def x_bounds(input):    #PART TWO CONDITIONS
            if "." == input:
                return False
            
            elif "-" in input: 
                num = input.strip("-")
                return num.isdigit() #if value is alphabet characters - return false
            
            elif input.isdigit():
                return True
            
            else:
                return False
    def f_bounds(input):    #PART TWO CONDITIONS
        try:
            float(input)
            return True
        except ValueError:
            return False
        
    def linear(a, an, m, b):
        while a <= an:
            y = m * (an - a) + b
            print(f"y({a}) = {y}")
            a += 1

       
        
            

#PROGRAM START

#PART ONE
print("Type 'quit' or 'exit' to stop the program.")
print("Type 'continue' to process to the next part.")

while True:
    user_input = input("Please enter an numeric value: ")

    if "quit" == user_input.lower() or "exit" == user_input.lower():
        quit()
    if "continue" == user_input.lower():
        break
    math.int_check(user_input)

    
#PART TWO
print("*" * 75)
print("PART TWO")
print("*" * 75)

linear_dict = {"a": "", "an": "", "m":"","b":""}
print("Type 'quit' or 'exit' to stop the program.")
continue_loop = True

while continue_loop == True:
    for key in linear_dict.keys():
        if key == "a" or key == "an":
            while True:
                user_input = input(f"Please input a valid numeric value for '{key}': ")
                if "quit" == user_input.lower() or "exit" == user_input.lower():
                    quit()
                math.x_bounds(user_input)
                is_integer = math.x_bounds(user_input)

                if is_integer == True:
                    linear_dict[key] = int(user_input)
                    break
                else:
                    print("For 'a' , and 'an' variables, please only input integers!")
                    

        elif key == "m" or key == "b":
            while True:
                user_input = input(f"Please input a valid numeric value for '{key}': ")
                if "quit" == user_input.lower() or "exit" == user_input.lower():
                    quit()
                math.f_bounds(user_input)
                is_digit = math.f_bounds(user_input)

                if is_digit == True:
                    linear_dict[key] = float(user_input)
                    break
                else:
                    print("Please enter only numeric values!")

        
    if linear_dict["a"] > linear_dict["an"]:
        print("Please re-enter your values - 'an' must be greater than 'a'.")
        continue

    math.linear(linear_dict["a"],linear_dict["an"],linear_dict["m"],linear_dict["b"])    

    user_continue = input("Would you like to continue with another calculation?\nPress any key to break, otherwise press 'Y':\t")

    if user_continue.lower() == "y":
        continue_loop = True
    else:
        break
    
        



        




# Point-slope y = mx + b




# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list




# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null