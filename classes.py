"""
Create classes and client code for each of the following items. 
For each one, think about what internal attributes it might have 
and what methods might be useful.

    computer
    building
    car
    phone
    clothing item
"""

# class Computer:

#     sticks = []

#     def __init__(self, ram, gpu, ssd):
#         self.ram = ram
#         self.gpu = gpu
#         self.ssd = ssd

#     def add_ram(self, stick):
#         self.sticks.append(stick)


# e = Computer("ddr4","luna","1tb")

# print(e.gpu)
# e.add_ram("ddr5")
# print(e.sticks)
# swap_ssd = input("Swap to: ")
# e.change_ssd("hdd")


class Product:
    products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ...]

    on_sale_products = []

    def __init__(self, product, price, on_sale):
        self.product = str
        self.price = int
        self.on_sale = on_sale
    
    def print_sales(self):
        with open("product_list.txt", "r") as r:
            r = r.read()
            print(r)

    

e = Product("Toy", 350, True)
e.print_sales()
