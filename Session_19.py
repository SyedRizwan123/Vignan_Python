#Number Triangle Pattern Program" (also called Floyd’s Triangle in mathematics).
"""n = 5          # Step 1: Set the number of rows for the pattern (triangle will have 5 rows).
num = 1   #7     # Step 2: Initialize 'num' with 1. 
            # This variable will be printed and incremented each time.
# Step 3: Outer loop → controls the number of rows (from 1 to n).
for i in range(1, n+1):  #i=1, i=2, i=3, i=4, i=5
    for j in range(i):   #i=1-> j=0; i=2->j=0,j=1; i=3->j=0,j=1,j=2;
        # Step 5: Print the current value of 'num'
                # 'end=" "' means: stay on the same line and put a space after printing
        print(num, end=" ")
        # Step 6: Increase 'num' by 1 for the next print
        num += 1    #2+1=3, 3+1=4
    print()"""



# This program prints a right-angled triangle pattern of letters.
"""for i in range(1, 6):       # This is the outer loop. It will iterate 5 times, with 'i' taking values from 1 to 5.
                            # This loop controls the number of rows to be printed.
    ch = 'A'                # Inside the outer loop, we initialize a variable 'ch' to the character 'A'
                                # at the beginning of each new row. This ensures that every row starts with 'A'.
    for j in range(1, i + 1):  # This is the inner loop. It depends on the current value of 'i'.
                                # For each row 'i', it will run 'i' times, with 'j' from 1 up to 'i'.
                                # This loop is responsible for printing the characters in each row.
        print(ch, end=' ')  # This prints the current character 'ch' followed by a space.
                                    # The 'end=' argument prevents a new line, keeping the characters on the same line.
        ch = chr(ord(ch) + 1)  # This is the key line for character manipulation.
                                # 1. 'ord(ch)' gets the ASCII (or Unicode) value of the current character 'ch'.
                                # 2. We add 1 to this value to get the next character's ASCII value.
                                # 3. 'chr()' converts this new ASCII value back into a character.
                                # This effectively moves to the next letter of the alphabet (A -> B, B -> C, etc.).
    print()"""  # After the inner loop completes (i.e., after printing all characters for the current row),

# Alphabet Triangle Pattern Program
"""ch = ord('A')  # Initialize 'ch' with the ASCII value of 'A'
for i in range(1, 6):         # Outer loop for rows (1 to 5)
    for j in range(1, i+1):   # Inner loop for columns in each row
        print(chr(ch), end=' ')  # Print the character
        ch += 1                  # Move to next character (ASCII value)
    print()"""                      # New line after each row

# Calculator
# Prompt the user to enter an operator
operator = input("Enter an operator (sum, sub, multi): ").strip().lower()
# Perform the operation based on the operator
if operator == "sum":   #sub==sum
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    z = x + y
    print(f"The sum of {x} and {y} is {z}")

elif operator == "sub":   #sub==sub
    x = int(input("Enter the first value: "))  #10
    y = int(input("Enter the second value: "))  #5
    z = x - y  #10-5=5
    print(f"The difference between {x} and {y} is {z}")
elif operator == "multi":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    z = x * y
    print(f"The product of {x} and {y} is {z}")
elif operator == "div":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    z = x/y
    print(f"The product of {x} and {y} is {z}")
else:
    print("Invalid operator. Please enter 'sum', 'sub', 'multi', or 'div'.")
