Define the lambda function echo_word using the variables word1 and echo. Replicate what the original function definition for echo_word() does above.
Call echo_word() with the string argument 'hey' and the value 5, in that order. Assign the call to result.

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 *echo)

# Call echo_word: result
result = echo_word("hey", 5)

# Print result
print(result)

In the map() call, pass a lambda function that concatenates the string '!!!' to a string item; also pass the list of strings, spells. Assign the resulting map object to shout_spells.
Convert shout_spells to a list and print out the list.

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + "!!!",  spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)

In the filter() call, pass a lambda function and the list of strings, fellowship. The lambda function should check if the number of characters in a string member is greater than 6; use the len() function to do this. Assign the resulting filter object to result.
Convert result to a list and print out the list.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member)> 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)

Import the reduce function from the functools module.
In the reduce() call, pass a lambda function that takes two string arguments item1 and item2 and concatenates them; also pass the list of strings, stark.
Assign the result to result. 
The first argument to reduce() should be the lambda function and the second argument is the list stark.

# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2 : item1 + item2, stark)

# Print the result
print(result)

Initialize the variables echo_word and shout_words to empty strings.
Add the keywords try and except in the appropriate locations for the exception handling block.
Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
Concatenate the string '!!!' to echo_word. Assign the result to shout_words.

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""
    

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + "!!!"
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")

Complete the if statement by checking if the value of echo is less than 0.
In the body of the if statement, add a raise statement that raises a ValueError with message 'echo must be greater than or equal to 0' when the value supplied by the user to echo is less than 0.

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)

In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text'].
The lambda function should check if the first 2 characters in a tweet x are 'RT'. 
Assign the resulting filter object to result. To get the first 2 characters in a tweet x, use x[0:2].
To check equality, use a Boolean filter with ==.

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

Add a try block so that when the function is called with the correct arguments, it processes the DataFrame and returns a dictionary of results.
Add an except block so that when the function is called incorrectly, it displays the following error message: 'The DataFrame does not have a ' + col_name + ' column.'
Convert result to a list and print out the list.

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

If col_name is not a column in the DataFrame df, raise a ValueError 'The DataFrame does not have a ' + col_name + ' column.'.
Call your new function count_entries() to analyze the 'lang' column of tweets_df. Store the result in result1.
Print result1. This has been done for you, so hit 'Submit Answer' to check out the result. In the next exercise, you'll see that it raises the necessary ValueErrors.

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, "lang")

# Print result1
print(result1)

