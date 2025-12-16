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
    # 
    

""" Print the square of numbers between a given range. Ask the user for a lower number and a higher number, then print all of the squares of the numbers in that range (inclusive).
Error-check the second number to make sure it is higher than the first. """

low_num = int(input("Low Number: "))
high_num = int(input("High Number: "))

while low_num > high_num:
    low_num = int(input("Try again: "))
else:
    # y = low_num * low_num
    for x in range(high_num):
        print(x*low_num)
    # print(x)
