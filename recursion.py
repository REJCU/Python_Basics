"""
Write a recursive function that prints all of the numbers from a given input down to 0.
"""

# def going_down(x):
#     # if (x>0):
#     #     result = going_down(x - 1) + 1 
#     #     print(result)
#     # else:
#     #     result = 0 
#     # return result
#     print(x)
#     if x == 0:
#          return 
#     else:
#          result = going_down(x - 1)
#     return result

# going_down(100)


"""
Write a recursive function that displays all of the letters in a string. 
(Each function call displays one letter.)
"""

# def make_letter_string(x):
     # print(x)
    # if x == '':
    #     return x 
    # else:
    #     print(x[0])
    #     make_letter_string(x[1:])

# user_submitt = str(input("Word: "))
# make_letter_string("Hello")

"""
Write a program that prints a string from the outside in, using recursion.
E.g. if the string to print is "Programming", 
your program should print: "P g r n o i g m r m a".
"""

# def outside_in(x):
#     print(x)
#     if x == '':
#        return  
#     else:
#         print(x[0], x[-1],end=" ")
#         outside_in(x[1:-1])
        
# outside_in("Programming")


"""
Write a recursive function to determine if a string 
is a palindrome 
(e.g. hannah is a palindrome, but han is not).
"""
 
# def is_palindrone(x):
#     if x == '':
#         return 
#     else:
#         is_palindrone(x, 0, len(x) - 1) 

# is_palindrone("momo")