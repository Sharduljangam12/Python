class ElectricCar:
    def __init__(self, brand, model, battery):
        self.__brand = brand        # private variable
        self.model = model
        self.battery = battery

    # Getter using custom method (your style)
    def get_brand(self):
        return self.__brand + "!"   # Add "!" to brand

    # Setter method to update brand
    def set_brand(self, new_brand):
        if new_brand != "":
            self.__brand = new_brand
        else:
            print("Brand name cannot be empty")

# Creating object
my_tesla = ElectricCar("Tesla", "Model S", "85kW/h")

# Using getter
print(my_tesla.get_brand())    # Output: Tesla!

# Using setter
my_tesla.set_brand("Toyota")
print(my_tesla.get_brand())    # Output: Toyota!

# Trying to set an empty brand
my_tesla.set_brand("")         # Output: Brand name cannot be empty
