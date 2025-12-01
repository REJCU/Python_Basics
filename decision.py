""" 
Write a progrma to check if someone can vote. 
They need to be over 18 or over and be enrolled to vote. 
You could two versions - one with nested ifs and one with the "and" operator. 
"""


user_age = int(input("Age: "))
enrolled_to_vote = input("Enrolled: ")


""" Nested if's """
# if user_age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")       


""" "AND" """

if user_age >= 18 and enrolled_to_vote == "yes":
    print("You can vote")
else:
    print("You cannot vote")