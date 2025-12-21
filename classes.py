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

class Computer:

    sticks = []

    def __init__(self, ram, gpu, ssd):
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd

    def add_ram(self, stick):
        self.sticks.append(stick)

e = Computer("ddr4","luna","1tb")

print(e.gpu)
e.add_ram("ddr5")
print(e.sticks)


