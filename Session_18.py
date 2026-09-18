#Right Triangle of Stars
#Right Triangle of Stars
"""n = 5   # Step 1: Assign 5 to variable 'n'. 
        # This means the triangle will have 5 rows.
# Step 2: Loop from 1 to n (inclusive).
for i in range(1, n+1):    #i=1,i=2,i=3,i=4,i=5
    # When n=5 → i takes values: 1, 2, 3, 4, 5
        
        # Step 3: "  " * (n-i) → adds spaces before stars to shift them to the right
        # Step 4: "* " * i → prints stars, count increases with each row      
    print("  " * (n-i) + "* " * i)"""

# Simple Triangle Pattern
"""rows = 6  # Sets the total number of rows for the triangle pattern.
for i in range(1, rows):  # Loop from 1 to rows-1 (i = 1 to 5) i=1, i=2, i=3, i=4, i=5
    spaces = rows - i - 1   #6-1-1=4, 6-2-1=3,6-3-1=2, 6-4-1=1, 6-5-1=0    # Calculate number of spaces before the stars for current row
    stars = 2 * i - 1       #2*1-1=1  2*2-1=3 2*3-1=6-1=5, 2*4-1=7, 2*5-1=9        # Calculate number of stars for current row (odd numbers: 1, 3, 5, ...)
    print(" " * spaces + "*" * stars)"""  # Print spaces followed by stars on the same line
        # " " * spaces: adds leading spaces to center the triangle
        # "*" * stars: prints the required number of stars for the row"""
        
"""rows = 6
# The variable `rows` is set to 6, which determines the number of rows in the triangle pattern.
for i in range(1, rows):
    # Outer loop iterates from 1 to `rows - 1` (i.e., 1 to 5).
    # Each iteration corresponds to one row of the triangle.

    for j in range(rows - i - 1):
        # Inner loop 1: Prints spaces before the stars in each row.
        # The number of spaces decreases as `i` increases.
        # For example:
        #   - When `i = 1`, `rows - i - 1 = 4` spaces are printed.
        #   - When `i = 2`, `rows - i - 1 = 3` spaces are printed.
        print(" ", end=" ")
        # Prints a single space (`" "`) without moving to the next line (`end=" "`).

    for j in range(2 * i - 1):
        # Inner loop 2: Prints stars (`*`) in each row.
        # The number of stars increases as `i` increases.
        # For example:
        #   - When `i = 1`, `2 * i - 1 = 1` star is printed.
        #   - When `i = 2`, `2 * i - 1 = 3` stars are printed.
        print("*", end=" ")
        # Prints a single star (`*`) without moving to the next line (`end=" "`).

    print()"""
    # Moves to the next line after printing all spaces and stars for the current row.

#Inverted Pyramid
"""n = 5   # Assign the number of rows for the triangle. Here, n = 5.
# Loop starts from n down to 1 with step -1.
# So, i will take values: 5, 4, 3, 2, 1
for i in range(n, 0, -1):   #5, 0, -1
    # The + operator joins spaces and stars in one string for each row.
    print(" " * (n-i) + "* " * i)"""

#Diamond Pattern
"""n = 5  # Number of rows for the upper half of the diamond
# Upper half of the diamond (including the middle row)
for i in range(1, n+1):  # Loop from 1 to n (1 to 5)
    print(" "*(n-i) + "* " * i)  
    # " "*(n-i): Prints spaces to center the stars
    # "* " * i: Prints i stars with a space after eac
# Lower half of the diamond (excluding the middle row)
for i in range(n-1, 0, -1):  # Loop from n-1 down to 1 (4 to 1)
    print(" "*(n-i) + "* " * i)"""
    # " "*(n-i): Prints spaces to center the stars
    # "* " * i: Prints i stars with

#Right Triangle Star Pattern (Top-Right)
"""for i in range(1, 6): #i=1, i=2
    for j in range(1, 6):
        if  j>= i: #1>=1, 2>=1,3>=1,4>=1,5>=1
                    #1>=2, 2>=2 
            print("*", end="")
        else:
            print(" ", end="")
    print()"""
    
#hollow square pattern pattern
# Outer loop: Controls the rows, running from i = 1 to 5 (range stops before 6)
"""for i in range(1, 6):
    # Inner loop: Controls the columns within each row, running from j = 1 to 5
    for j in range(1, 6):
        if i == 1 or j == 1 or i == 5 or j == 5:
            # Print an asterisk followed by a space, keeping the cursor on the same line
            print("*", end=" ")
        else:
        # For interior cells, print two spaces to keep alignment without a border
            print(" ", end=" ")
    # After finishing all columns for row 'i', print an empty line to move to the next row
    print()"""

# This program prints a right-angled triangle pattern of numbers.
for i in range(1, 6):     # This is the outer loop. It will run 5 times, with 'i' taking values from 1 to 5.
                            # This loop controls the number of rows to be printed.
    for j in range(1, i + 1):  # This is the inner loop. It depends on the value of 'i' from the outer loop.
                                # For each row 'i', it will run 'i' times, with 'j' taking values from 1 up to 'i'.
                                # This loop is responsible for printing the numbers in each row.
        print(j, end=" ")    # This prints the current value of 'j' followed by a space instead of a new line.
                            # This keeps the numbers for a single row on the same line.
    print()    

