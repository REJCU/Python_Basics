"""  
Write a menu-driven program that loops until the user quits. The options are (G)et name, (U)ppercase, (L)owercase, (Q)uit.
The program should start by asking the user for their name before the menu, but they can (G)et a new name. 
U/L print the name in either uppercase or lowercase.
"""

"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""
# name = input("Name: ")
# menu = "(G)et name, \n(U)ppercase,\n(L)owercase,\n(Q)uit" 
# print(menu)
# 
# choice = str(input("choice: "))
# while choice != "q":
    # if choice == "g":
        # name = input("name")
        # print(f"Your new name{name}")
    # elif choice == "u":
        # print(name.upper())
    # elif choice == "l":
        # name == name.lower()
        # print(name)
    # else:
        # print("Choose again")
    # print(menu)
    # choice = input("choice: ")
# print(name)
    
    

""" Print the square of numbers between a given range. Ask the user for a lower number and a higher number, then print all of the squares of the numbers in that range (inclusive).
Error-check the second number to make sure it is higher than the first. """

# low_num = int(input("Low Number: "))
# high_num = int(input("High Number: "))

# while low_num > high_num:
#     low_num = int(input("Try again: "))
# else:
#     for x in range(high_num):
#         print(x*low_num)


""" 
Print a "progress bar" based on a percentage (number). E.g. 50% would print something like: |*****-----|, 10% would print |*---------|
"""
# BAR = "---------"
# LOAD = "*"

# percentage = float(input("Percentage: "))

# if percentage <= 0:
#     for x in range(1):
#         print(BAR)
# else:
#     print

# def generate_progress_bar(percentage, length=10, filled_char='*', empty_char='-'):
#     """
#     Generates a string representing a progress bar.

#     Args:
#         percentage (int/float): The completion percentage (0 to 100).
#         length (int): The total number of characters in the bar (default is 10).
#         filled_char (str): The character to use for the completed portion.
#         empty_char (str): The character to use for the remaining portion.

#     Returns:
#         str: The progress bar string.
#     """
#     # 1. Calculate the number of filled characters
#     # Ensure percentage is between 0 and 100
#     percentage = max(0, min(100, percentage))
    
#     # Calculate the number of filled characters, rounded to the nearest integer
#     filled_count = round((percentage / 100) * length)
    
#     # 2. Calculate the number of empty characters
#     empty_count = length - filled_count
    
#     # 3. Construct the bar using string multiplication and concatenation
#     bar = f"|{filled_char * filled_count}{empty_char * empty_count}|"
    
#     return bar

# # --- Examples ---

# # Example 1: 50%
# bar_50 = generate_progress_bar(50)
# print(f"50%: {bar_50}")

# # Example 2: 10%
# bar_10 = generate_progress_bar(10)
# print(f"10%: {bar_10}")

# # Example 3: 95%
# bar_95 = generate_progress_bar(95)
# print(f"95%: {bar_95}")

# # Example 4: A longer bar (20 characters) at 67%
# bar_long = generate_progress_bar(67, length=20, filled_char='#', empty_char='.')
# print(f"67% (Length 20): {bar_long}")

""" 
Caffeinated Cameron has started SpecialTea Cofftea (he thinks the name is clever, but others find it confusing). 
This startup's new innovation is a funky menu where customers enter: "T" for.. Tea (get it? ;) or "C" for coffee, until they enter "Q" for quit. 
Any different inputs result in "Error".At the end of their caffeination session (when they quit), 
the program shows them how much they owe: Each T costs $2.10, Coffees are $3.45.
"""
amount_owing = 0
tea = 2.10
coffee = 3

menu = "(T)ea, \n(C)offee,\n(Q)uit" 
print(menu)
print(round(amount_owing, 2))

choice = str(input("choice: "))
while choice != "q":
    if choice == "t":
        amount_owing = amount_owing + tea
        print(round(amount_owing, 2))
    elif choice == "c":
        amount_owing = amount_owing + coffee
        print(round(amount_owing, 2))
    else:
        print("Error")
    print(menu)
    choice = input("choice: ")
print(f"${round(amount_owing, 2)}")


