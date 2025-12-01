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
name = input("Name: ")
menu = "(G)et name, \n(U)ppercase,\n(L)owercase,\n(Q)uit" 
print(menu)

choice = str(input("choice: "))
while choice != "q":
    if choice == "g":
        name = input("name")
        print(f"Your new name{name}")
    elif choice == "u":
        print(name.upper())
    elif choice == "l":
        name == name.lower()
        print(name)
    else:
        print("Choose again")
    print(menu)
    choice = input("choice: ")
print(name)
    
    