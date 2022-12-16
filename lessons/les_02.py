class Laptop:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.memory = self.Memory()
        self.cpu = cpu

    def print_details(self):
        print(self.brand, self.memory.size, self.cpu)

    class Memory:
        def __init__(self):
            self.size = '8gb'

# eight_gb = Memory()
hp_laptop = Laptop('HP', 'i7 Processor')
hp_laptop.memory.size = '4gb'
hp_laptop.print_details()

dell_laptop = Laptop('Dell', 'i5')
dell_laptop.print_details()

print(id(hp_laptop.memory))
print(id(dell_laptop.memory))
