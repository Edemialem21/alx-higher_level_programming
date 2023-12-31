#  object-oriented programming
# involves programming using objects. represtnt real world object.
# an object has a state, a behaviour and an identity
# examples: student circle button bank account
# behaviour of an object- defined by the methods of aan objeect
# behaviours - actions, to invoke or call a method on an object is to ask the object to performn an action .
# str.charAt(2), 

# Identity of an object - what makes an object uniqe


# Jenny's lectures in oop.
# why we need oop?
# for the case of large project we have to use oop 
# there is no data security in procedural because data is easily shared unsecurely
# oop is used to model real world problem.
# everything in the real worldl is considered as an  object.
# everything in python is an object of the built in class.
# 

#  object orinted programming
# youtube starting 
#  - intractor
#  -- editor
#  -- social media marketer
    # Instractor ####
# - is a considered as object as blueprint
# and all the persons hired as instractors is considered as object
# 

# as ablueprint ---  an instractor has
#                -NAME, ADDRESS ----VARIAVLES
#                - LAPTOP BOOK  ---- ATTRIBUTE


#               ----an instractor does 
#           def teach()  -- METHODS WHICH ARE NOT FREE FLOATING LIKE FUNCTIONS 
#            statements
#             def prepareQuiz()   --- METHODS WHICH DOES ANY INSTRACTORS.

# examples --- house design is considered as class as pluprint
#           using this design as blueprint we can build more than one home- which is considered as object in python.
# we can considered class as user defined data types. justi like built in data types which are considered as class.
# syntax

class Instractor:
    def __init__(self, name, address):  # init method is used to initialize while create an object
        self.name= name
        self.address= address  # initializing the second attribute
        print("creationg an object")
instractor_1 = Instractor('edemialem', 'Addis ')
instractor_2 = Instractor('getachew', 'markls')
print(type(instractor_1))

# how to initialize methods
# instractor_1.name = "edemialem"
# instractor_1.address = "aa"
# print(instractor_1.name)
# instractor_2.name= 'getachew'
# print(instrac)