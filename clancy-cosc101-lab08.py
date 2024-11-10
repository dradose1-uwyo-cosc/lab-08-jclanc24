
# John Clancy
# UWYO COSC 1010
# Submission Date: 11/8/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# None - mostly referred to lecture notes and powerpoints.


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

class math:
    
    def __init__(self, input, a, an, m, b, c):
        self.input = input
        self.a = a  #lower bound
        self.an= an #upper bound
        self.b = b
        self.m = m
        self.c = c

    def int_check(input):   #PART ONE CONDITIONS
        try:
            int(input)
            print(f"{input} is an integer.")
            return True
        except ValueError:
            print(f"{input} is not an integer.")
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
            y = m * (a) + b
            print(f"y({a}) = {y}")
            a += 1

    def quadratic_root(a,b,c):  #PART THREE CONDITIONS
        qroot_numer = (b ** 2) - (4 *a *c)

        if qroot_numer >= 0:
            return (qroot_numer ** 0.5)
        else:
            qroot_numer = "null"
            return qroot_numer

    def quadratic_solution(a,b,input):  #PART THREE CONDITIONS
        if input == "null":
            return "Solution: null"
        else:
            input = float(input)
            add = (-b + input) / (2 * a)
            sub = (-b - input) / (2 * a)
            solution = (f"Solution: {add:.1f}\nSolution: {sub:.1f}")
            return solution
        

       
        
            

#PROGRAM START

#PART ONE
print("*" * 75)
print("PART ONE - TRY INT OR FLOAT TYPES")
print("*" * 75)
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
print("PART TWO - POINT SLOPE FORMULA")
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


#PART THREE


print("*" * 75)
print("PART THREE - QUADRATIC FORMULA")
print("*" * 75)
print("Type 'quit' or 'exit' to stop the program.")

quadratic_dict = {"a":"","b":"","c":""}

while continue_loop == True:
    for key in quadratic_dict.keys():
        while True:
            user_input = input(f"Please enter the value for '{key}': ")
            if "quit" == user_input.lower() or "exit" == user_input.lower():
                    quit()
            is_digit = math.f_bounds(user_input)
            if is_digit == True:
                quadratic_dict[key] = float(user_input)
                break
            else:
                print("Please enter a valid numeric number!")

    qroot = math.quadratic_root(quadratic_dict["a"], quadratic_dict["b"], quadratic_dict["c"])
    quadratic_sol = math.quadratic_solution(quadratic_dict["a"],quadratic_dict["b"], qroot)

    print(quadratic_sol)

    user_continue = input("Would you like to continue with another calculation?\nPress any key to break, otherwise press 'Y':\t")

    if user_continue.lower() == "y":
        continue_loop = True
    else:
        break    


















# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
