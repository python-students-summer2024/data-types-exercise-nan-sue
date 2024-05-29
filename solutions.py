"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    question_of_sales = input("What's the projected amount of total sales? ")
    number_of_sales = float(question_of_sales)
    profit = number_of_sales * 0.23
    two_decimal = format(profit, '.2f')
    output_message = "Profit: $" + str(two_decimal)
    print(output_message)


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    number_1 = input("Enter number #1: ")
    number_2 = input("Enter number #2: ")
    quotient = int(number_1) // int(number_2)
    remainder = int(number_1) % int(number_2)
    output_message = number_2 + " goes into " + number_1 + " a total of " + str(quotient) + " times with a remainder of " + str(remainder)
    print(output_message)

calculate_quotient_and_remainder()


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles_driven = input("Miles driven: ")
    gas_used = input("Gas used(gallons): ")
    calculation_of_miles_per_gallon = int(miles_driven) / int(gas_used)
    two_decimal = format(calculation_of_miles_per_gallon, '.2f')
    output_message = "Miles per gallon: " + str(two_decimal)
    print(output_message)

calculate_miles_per_gallon()


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price_1 = float(input("Enter price #1: "))
    price_2 = float(input("Enter price #2: "))
    price_3 = float(input("Enter price #3: "))
    format_1 = format (price_1, '>10,.2f')
    format_2 = format (price_2, '>10,.2f')
    format_3 = format (price_3, '>10,.2f')
    output_1 = "Price #1: $ " + format_1
    output_2 = "Price #2: $ " + format_2
    output_3 = "Price #3: $ " + format_3
    print("\nHere are your prices!\n")
    print(output_1)
    print(output_2)
    print(output_3)
align_text()


