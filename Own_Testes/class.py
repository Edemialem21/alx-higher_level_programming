def hi(obj):
    print("Hi, I am " + obj.name + "and manfactured in " + obj.year+ "!")
class Robot:
    say_hi = hi #it is the method it is called like this, x.say_hi()
    def __init__(self): # __init__ is a method called after an instance has been created 
        print("__init__ has been executed")
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    yy = y
    print(y == yy)
    print(y == x)
    x.name = "marvin"
    x.year = "1983"
    y.name = "caliban"
    # the instance possess dictionaries __dict__ which they use to store
    # their attribute and their corresponding values
    print(x.__dict__)
    print(Robot.__dict__)
# hi is a function which takes object as an argument, this object has an attribute "name"
hi(x)
Robot.say_hi(x)  #binding the function "hi" to a class attribute "say_hi" 


# method is just a function which id defined inside a class
# the first parameter is used a referance to the calling instance
# the parameter is usually called self.
# self - corresponds to the Robot object x.
# methode differ from a function  only in two aspects:
    # 1. it belongs to a class, and id defined within a class
    # 2. the first parameter in method is self.

class Car:
    def __init__(self, name=None):
        self.name = name
    def heyy(self):
        if self.name:
            print("hi my name is " + self.name)
        else:
            print("Hi, I am a brand car without a name")
x = Car()
x.heyy()
y = Car("Age_brand")
y.heyy()


# Data abstraction, Data Encapsualtion and Information hiding
    # Encapsulation - bundling of data with the methods that operate on the data
        # encapsulation via methods doesn't mean that the data is hidden, but using the method is recommended to access and seeing the data 
    # Data Hiding - some internal data are hidden, so that that can't be accidentally changed.
    # Data Abstraction = Data Encapsulation + Data HIding
        # getter -  methoda used for the case encapsulation, this methods do not change the value it just return the values
        # setter - the methods used for changing the values of attribute
def set_name(self, name):
    self.name = name
def get_name(self, name):
    return self.name
x.set_name("mozilla")
x.heyy()
y.set_name(x.get_name)
y.heyy()
