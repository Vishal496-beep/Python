class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand + "!"
    
    def set_brand(self, value ):
          if value == "":
              print("Invalid brand")
          else: self.__brand = value
    def fuel_Type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    @staticmethod
    def general_cars():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_Type(self):
        return "Electric charge"

# my_tesla = ElectricCar("Tesla","model S","85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla,ElectricCar))


# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# my_tesla.set_brand("bmw")
# print(my_tesla.get_brand())
# my_tesla.set_brand("")
# print(my_tesla.get_brand())
# my_tesla.set_brand("bmw")
# print(my_tesla.get_brand())
# print(my_tesla.fuel_Type())
# my_car = Car("Tata", "safari")
# # my_car.model = "city"
# print(my_car.model)

# print(my_tesla.general_cars())





# my_car = Car("Toyota", "corolla")   #it created a object
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# self is the same as {this} key in js we accessattribute using it 

# my_new_car = Car("safari", "gear")
# print(my_new_car.brand)

#multiple inheritance

class Battery():
    def batter_ins(self):
        return "this is battery"
    
class Engine():
    def good_eng(self):
        return "great engine"
    
class Electriccartwo(Battery,Engine, Car):
    pass

my_new_tesla = Electriccartwo("hero", "honda")
print(my_new_tesla.good_eng())
print(my_new_tesla.batter_ins())