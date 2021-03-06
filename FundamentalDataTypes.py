Create a list called baby_names with the names 'Ximena', 'Aliza', 'Ayden', and 'Calvin'.
Use the .extend() method on baby_names to add 'Rowen' and 'Sandeep' and print the list.
Use the .index() method to find the position of 'Aliza' in the list. Save the result as position.
Use the .pop() method with position to remove 'Aliza' from the list.
Print the baby_names list. This has been done for you, so hit 'Submit Answer' to see the results!

# Create a list containing the names: baby_names
baby_names = ["Ximena", "Aliza", "Ayden", "Calvin"]

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(["Rowen", "Sandeep"])

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index("Aliza")

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)

Create an empty list called baby_names.
Use a for loop to iterate over each row of records appending the name, found in the fourth element of row, to baby_names.
Print each name in baby_names in alphabetical order. To do this:
Use the sorted() function as part of a for loop to iterate over the sorted names, printing each one.

# Create the empty list: baby_names
baby_names = []

# Loop over records
for row in records:
    # Add the name to the list
    baby_names.append(row[3])

# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)

Use the zip() function to pair up girl_names and boy_names into a variable called pairs.
Use a for loop to loop through pairs, using enumerate() to keep track of your position. Unpack pairs into the variables idx and pair.
Inside the for loop:
Unpack pair into the variables girl_name and boy_name.
Print the rank, girl name, and boy name, in that order. The rank is contained in idx.

# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))

Create a variable named normal and set it equal to 'simple'.
Create a variable named error and set it equal 'trailing comma',.
Print the type of the normal and error variables.

# Create the normal variable: normal
normal = "simple"

# Create the mistaken variable: error
error = "trailing comma",

# Print the types of the variables
print(type(normal))
print(type(error))

Combine all the names in baby_names_2011 and baby_names_2014 by computing their union. Store the result as all_names.
Print the number of names that occur in all_names. You can use the len() function to compute the number of names in all_names.
Find all the names that occur in both baby_names_2011 and baby_names_2014 by computing their intersection. Store the result as overlapping_names.
Print the number of names that occur in overlapping_names.

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))

Create an empty set called baby_names_2011. You can do this using set().
Use a for loop to iterate over each row in records:
If the first column of each row in records is '2011', add its fourth column to baby_names_2011. Remember that Python is 0-indexed!
Find the difference between baby_names_2011 and baby_names_2014. Store the result as differences.
Print the differences. This has been done for you, so hit 'Submit Answer' to see the result!

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
     if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)

Create an empty dictionary called names_by_rank.
Loop over female_baby_names_2012.items(), unpacking it into the variables rank and name.
Inside the loop, add each name to the names_by_rank dictionary using the rank as the key.
Sort the names_by_rank dictionary keys in descending order, select the first ten items. Print each item.

# Create an empty dictionary: names_by_rank
names_by_rank = {}

# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name

# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])

Safely print rank 7 from the names dictionary.
Safely print the type of rank 100 from the names dictionary.
Safely print rank 105 from the names dictionary or 'Not Found' if 105 is not found.

# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get("100")))

# Safely print rank 105 from the names dictionary or 'Not Found'
try:
    print(rank(105))
except:
    print("Not Found")

Print the keys of the boy_names dictionary.
Print the keys of the boy_names dictionary for the year 2013.
Loop over the boy_names dictionary.
Inside the loop, safely print the year and the third ranked name. Print 'Unknown' if the third ranked name is not found.

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, "Unknown"))

Assign the names_2011 dictionary as the value to the 2011 key of the boy_names dictionary.
Update the 2012 key in the boy_names dictionary with the following data in a list of tuples: (1, 'Casey'), (2, 'Aiden').
Loop over the boy_names dictionary.
Inside the for loop, sort the data for each year of boy_names by descending rank and take the first result which will be the lowest ranked name.
Safely print the year and least popular name or 'Not Available' if it is not found. Take advantage of the .get() method.

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1,'Casey'), (2,'Aiden')])

# Loop over the years in the boy_names dictionary
for year in boy_names:
    # sort the data for each year by descending rank and get the lowest one
    lowest_ranked = sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked, 'Not Available'))
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
