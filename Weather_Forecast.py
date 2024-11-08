# 1. Exceptional Weather Forecast
# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather 
# forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
user_input = (input("Please enter the temperature in Fahrenheit: "))

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

def temp_converter(fahrenheit):
   try: #Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?
        fahrenheit = float(user_input)
        celsius = (fahrenheit - 32) * 5/9
   except ValueError: 
        print("Error: Please enter a numerical value.")

# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
   else:
        print(f'{user_input} degrees Fahrenheit is {celsius} degrees Celsius')
          
# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.
   finally:
        print(f'Thank you for using our Weather Forecast Application!')

temp_converter(user_input) 

