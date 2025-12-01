""" 
Write a progrma to check if someone can vote. 
They need to be over 18 or over and be enrolled to vote. 
You could two versions - one with nested ifs and one with the "and" operator. 
"""


# user_age = int(input("Age: "))
# enrolled_to_vote = input("Enrolled: ")


# """ Nested if's """
# # if user_age >= 18:
# #     print("You can vote")
# # else:
# #     print("You cannot vote")       


# """ "AND" """

# if user_age >= 18 and enrolled_to_vote == "yes":
#     print("You can vote")
# else:
#     print("You cannot vote")
    

""" 
Write the Kebab Kalculator. The program should have base prices for small ($7.50) or large ($10) kebabs (constants)
The user should choose a size, and how many extra toppings they want: up to 2 toppings are free, 3 or more toppings are 50c each (but not counting the free ones!).
Examples:
a small kebab with 3 toppings = $8
a large kebab with 2 toppings = $10
large with 10 = $14
Ask the user for their options, then print the final price.
"""

S_KEBAB = 7.50
L_KEBAB = 10

toppings_price = 0.50

choice = input("Size: S or L: ")
quant_of_top = int(input("Quantity of Toppings: "))

if choice == "s":
    if quant_of_top >= 3:
        x = (quant_of_top - 2) * toppings_price
        print(S_KEBAB + x)
    else:
        print(S_KEBAB)

if choice == "l":
    if quant_of_top >= 3:
        x = (quant_of_top - 2) * toppings_price
        print(L_KEBAB + x)
    else:
        print(L_KEBAB)
    