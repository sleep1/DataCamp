Import the pandas module under the alias pd.
Load the CSV "credit_records.csv" into a DataFrame called credit_records.
Display the first five rows of credit_records using the .head() method.

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())

Use the .info() method to inspect the DataFrame credit_records

#Use .info() to inspect the DataFrame credit_records
print(credit_records.info())

Select the column item from credit_records using brackets and string notation.
Select the column item from credit_records using dot notation.

# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)

Correct the code so that it runs without errors.# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records["location"]

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)

Inspect the DataFrame mpr using info().

# Use info() to inspect mpr
print(mpr.info())

Correct the mistakes in the code so that it runs without errors.

# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr['Dog Name']

# Select column "Missing?" from mpr
is_missing = mpr['Missing?']

# Display the columns

The variable height_inches represents the height of a suspect. Is height_inches greater than 70 inches?

# Is height_inches greater than 70 inches?
print(height_inches > 70)

The variable plate1 represents a license plate number of a suspect. Is it equal to FRQ123?

# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

The variable fur_color represents the color of Bayes' fur. Check that fur_color is not equal to "brown".

# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")

Select the dogs where Age is greater than 2.
Select the dogs whose Status is equal to Still Missing.
Select all dogs whose Dog Breed is not equal to Poodle.

# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == "Still Missing"]
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr["Dog Breed"] != "Poodle"]
print(not_poodle)

Select rows of credit_records such that the column location is equal to 'Pet Paradise'.

# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)
