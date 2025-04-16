
# class Teacher:
#     subject = "math"
#     def nameOfTeacher(self):
#         print('Ben')
#     @staticmethod
#     def staticMethod(sub):
#         Teacher.subject = sub

# techr = Teacher()
# print("Before ",Teacher.__dict__)
# techr.staticMethod("English")
# print("After ",Teacher.__dict__)

# class Student:
#     school ="CMS"
#     def __init__(self,name):
#         self.name = name
#     # instance method
#     #  @property
#     def callName(self,school):
#         self.__class__.school = school
#         print(f"Name : {self.name} , School : {self.school} .")
#         # self.stic()
#         # self.showSchool()
#         # self.
#     @staticmethod
#     def stic():
#         print("Welcome to School")
#         Student.showSchool()
#         # Student.callName() cannot call an intance method
#         print(Student.school)
#         techr.nameOfTeacher()
#     @classmethod 
#     def showSchool(cls):
#         print(cls.school)
#         # cls.showSchool()
#         # cls.stic()
#         # Student.stic()
#         # cls.callName()
# stud = Student("Moiz")
# stud2 = Student("Awab")
# stud.callName("Church Mission School")
# stud2.callName("Church Mission School")
# stud.stic()
# stud.showSchool()
# # stud.school = "CMS Govt School"
# print("class",Student.__dict__)
# print("object",stud.__dict__)
# print("object",stud2.__dict__)

# # Student.callName()
# Student.stic()
# Student.showSchool()

#Inheritance
class Car:
    company ="Ferrari"
    def __init__(self,name,color):
        self.name = name
        self.color = color
    #instance method
    def specification(self):
        print(f" Name : {self.name} , Color : {self.color}")
    @classmethod
    def clsMethod(cls):
        print(f"Company : {cls.company}")
    @staticmethod
    def companyMessage(model,color):
        print(f"Dear Friends, Our Company {Car.company} luanches a new Ferrari with that {model} and {color}")


class NewCar(Car):
    def __init__(self, name, color,feature):
        super().__init__(name, color)
        self.feature = feature
    def specification(self):
        print(f"Name : {self.name} , Color : {self.color} , Features :{self.feature}")
    @classmethod
    def clsMethod(cls):
        print(f"Company : {cls.company}")
    @staticmethod
    def companyMessage(name,color,feature):
        print(f"Dear Friends, Our Company {Car.company} luanches a new Ferrari , {name} with {color} color and {feature} ")

newCar = NewCar("Roma Spider","White","Kholi Chhat")
print(newCar.company)
newCar.specification()
newCar.clsMethod()
newCar.companyMessage(newCar.name,newCar.color,newCar.feature)


#Encapsulation
class ATM:
    __bank = "W11"
    def __init__(self,name,pin):
        self._name = name
        self.__pin = pin
    def __showpin(self):
        print("Access Denied")
    @classmethod
    def _showCompany(cls):
        print(cls.__bank)
    @classmethod
    def update_name(cls,bankname):
        cls.__bank = bankname
    @staticmethod 
    def __message(name):
        print(f"Hello Sir {name}, Welcome to our {ATM.__bank} bank")
    @staticmethod
    def update_bank(name):
        ATM.__bank = name

ourAtm = ATM("Sam",1234)
# ourAtm.__showpin()
ourAtm._showCompany()
# ourAtm.__message(ourAtm._name)
print(ourAtm._name)
# print(ourAtm.__bank)
# print(ourAtm.__pin)
print(ourAtm._ATM__pin)
ourAtm.update_name("W12")
ourAtm._showCompany()
ourAtm.update_name("W13")
ourAtm._showCompany()

class MiniATM(ATM):

    def __init__(self, name, pin):
        super().__init__(name, pin)
        self.__pin = pin

miniAtm = MiniATM("Ben",5678)
print(miniAtm.__dict__)

from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,name):
        super().__init__()
        self.name = name
    @abstractmethod
    def start(self):
        pass

# vich = Vehicle()
# vich.start()

print(Vehicle.__dict__)
class Car(Vehicle):
    def __init__(self,name,name2):
        super().__init__(name)
        self.name = name2
    def start(self):
        print("start")
    def end(self):
        print("end")


car = Car("Ferrari","Roma")
car.start()
print(car.name)

# same worj with normal class

# print("\n Normal Class \n")
# class Electronics:
#     def __init__(self,name):
#         self.name = name
        
    
#     def electOn(self):
#         pass

# class Charger(Electronics):
#     def __init__(self, name,name2):
#         super().__init__(name)
#         self.name = name2

# charg = Charger("Apple","Samsung")
# print(charg.__dict__)
# print(charg.name)
# charg.electOn()
