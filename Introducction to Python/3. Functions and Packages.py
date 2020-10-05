Use print() in combination with type() to print out the type of var1.
Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
Use int() to convert var2 to an integer. Store the output as out2.

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

Use the upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
Print out place and place_up. Did both change?
Print out the number of o's on the variable place by calling count() on place and passing the letter 'o' as an input to the method.
We're talking about the variable place, not the word "place"!

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
Call count() on areas to find out how many times 9.50 appears in the list.
Again, simply print out this number.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))


# Print out how often 9.50 appears in areas
print(areas.count(9.5))

Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
Print out areas
Use the reverse() method to reverse the order of the elements in areas.
Print out areas once more.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

Import the math package. Now you can access the constant pi with math.pi.
Calculate the circumference of the circle and store it in C.
Calculate the area of the circle and store it in A.

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r **2

# Build printout

Perform a selective import from the math package where you only import the radians function.
Calculate the distance travelled by the Moon over 12 degrees of its orbit.
Assign the result to dist. You can calculate this as r * phi, where r is the radius and phi is the angle in radians.
To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)
