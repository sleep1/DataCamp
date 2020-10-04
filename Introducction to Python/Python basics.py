/Above the print(7 + 10), add the comment
# Addition

# Division
print(5 / 8)

# Addition
print(7 + 10)

Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 100×1.1=110
100×1.1=110 dollars, and after two years it's 100×1.1×1.1=121. 
Add code to calculate how much money you end up with after 7 years, and print the result.

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * (1.1**7))

Create a variable savings with the value 100.
Check out this variable by typing print(savings) in the script.

# Create a variable savings
savings = 100

# Print out savings
print(savings)

Create a variable growth_multiplier, equal to 1.1.
Create a variable, result, equal to the amount of money you saved after 7 years.
Print out the value of result.

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print(result)

Create a new string, desc, with the value "compound interest".
Create a new boolean, profitable, with the value True.

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

Calculate the product of savings and growth_multiplier. Store the result in year1.
What do you think the resulting type will be? Find out by printing out the type of year1.
Calculate the sum of desc and desc and store the result in a new variable doubledesc.
Print out doubledesc. Did you expect this?

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

Hit Run Code to run the code. Try to understand the error message.
Fix the code such that the printout runs without errors; use the function str() to convert the variables to strings.
Convert the variable pi_string to a float and store this float as a new variable, pi_float.

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(str(pi_string))
