#composition
class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower
    def start(self):
        return "Engine Started"

class Car:
    def __init__(self,name,horsepower):
        self.name = name
        self.engine = Engine(horsepower)
    def startCar(self):
        return f"{self.name} car with {self.engine.horsepower} HP : {self.engine.start()}"

myCar = Car("Ferrari",500)

print(myCar.startCar())
del myCar

#aggregation
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation (Passed as a parameter)

    def start_car(self):
        return f"{self.brand} car with {self.engine.horsepower} HP: {self.engine.start()}"

# Creating Engine object separately
engine_obj = Engine(250)

# Creating Car object and passing Engine
my_car = Car("Honda", engine_obj)

print(my_car.start_car())  # Honda car with 250 HP: Engine started

# Deleting Car object
del my_car  

# ✅ Engine still exists because it was created separately
print(engine_obj.start())  # Engine started
