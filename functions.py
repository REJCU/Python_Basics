"""
Write a function that calculates which of two products is cheaper based on a quantity and price. 
The function will take 4 parameters - the quantity and price of each product, and output either "First" or "Second".
"""
# first_total = 0 
# second_total = 0 

# def main():
#     get_product_info()
#     compare_product_info(first_product_price, first_product_quality, second_product_price,second_product_quality)


# def get_product_info():
#     first_product_quality = input("1 - Quality: ")
#     first_product_price = input("1 - Price: ")
#     second_product_quality = input("2 - quality")
#     second_product_price = input("2 - Price: ")
#     return first_product_price, first_product_quality, second_product_price,second_product_quality

# def compare_product_info(first_product_price, first_product_quality, second_product_price,second_product_quality):
#     if first_product_price > second_product_price:
#         first_total = first_total + 1
#     else:
#         second_total = second_total + 1 
#     print(first_total, second_total)

    
# main()

def compare_product_prices(quantity1, price1, quantity2, price2):
    """
    Calculates which of two products is cheaper based on price and quantity.

    Args:
        quantity1 (float): The quantity (e.g., weight, number of units) of the first product.
        price1 (float): The total price of the first product.
        quantity2 (float): The quantity of the second product.
        price2 (float): The total price of the second product.

    Returns:
        str: "First" if the first product is cheaper, "Second" if the second 
             is cheaper, or "Tie" if the unit prices are equal.
    """
    
#     # Check for invalid quantities (must be positive)
#     if quantity1 <= 0 or quantity2 <= 0:
#         return "Error: Quantities must be greater than zero."

#     # 1. Calculate the unit price for the first product
#     unit_price_1 = price1 / quantity1
    
#     # 2. Calculate the unit price for the second product
#     unit_price_2 = price2 / quantity2
    
#     # 3. Compare the unit prices
#     if unit_price_1 < unit_price_2:
#         return "First"
#     elif unit_price_2 < unit_price_1:
#         return "Second"
#     else:
#         return "Tie"

# # --- Examples ---

# # Example 1: Comparing two different sizes of cereal
# # Product 1: 500g for $4.00
# # Product 2: 750g for $5.25 (Cheaper unit price: $5.25 / 750g = $0.007/g)
# # Unit Price 1: 4.00 / 500 = 0.008
# # Unit Price 2: 5.25 / 750 = 0.007
# result1 = compare_product_prices(500, 4.00, 750, 5.25)
# print(f"Product 1 (500g/$4.00) vs Product 2 (750g/$5.25): {result1}")

# # Example 2: Comparing items where the first one is cheaper
# # Product 1: 12-pack for $6.00 (Cheaper: $0.50/unit)
# # Product 2: 8-pack for $5.00 ($0.625/unit)
# result2 = compare_product_prices(12, 6.00, 8, 5.00)
# print(f"Product 1 (12/$6.00) vs Product 2 (8/$5.00): {result2}")

# # Example 3: A tie (same unit price)
# # Product 1: 2 units for $10.00 ($5.00/unit)
# # Product 2: 4 units for $20.00 ($5.00/unit)
# result3 = compare_product_prices(2, 10.00, 4, 20.00)
# print(f"Product 1 (2/$10.00) vs Product 2 (4/$20.00): {result3}")

"""
Use an appropriate function... Timmy Timer wants to know how long he has been doing something in minutes and seconds, but his timepiece only shows total seconds. 
He wants you to help him calculate the total time in minutes and seconds.
Example: He inputs 134 and the program shows something like: 2 minutes and 14 seconds
"""
timmy_time = float(input("Time: "))

def seconds_to_minutes():
    minutes = (timmy_time // 60) 
    seconds = timmy_time % 60
    print(f"{minutes} minutes and {round(seconds)} seconds")

seconds_to_minutes()

"""
How it Works
    Integer Division (//):
        134//60=2
        This gives you the whole number of minutes (2).

    Modulo Operator (%):
        134%60=14
        This gives you the remainder, which is the number of seconds left over (14).
"""