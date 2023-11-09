# OOP
""" class PlayerCharacter:
    # Class Object Attribute (Something that won't change) 
    membership = True
    def __init__(self, name="Anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")
    
    @classmethod #Class methods that can be run without instanciating
    def adding_things(cls, num1, num2): #cls for class
        return cls("Teddy", num1 + num2)
    
    @staticmethod 
    def adding_things(num1, num2):
        return ("Teddy", num1 + num2)

#player1 = PlayerCharacter("Tom", 19)
player3 = PlayerCharacter.adding_things(2,3)
print(player3.age) """

# 121. Exercise: Cats everywhere
""" # Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat("Mjau", 12)
Cat2 = Cat("Garfield", 15)
Cat3 = Cat("Kitty", 26)


# 2 Create a function that finds the oldest cat
def oldestCat(*cats):
    return max(cats)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldestCat(Cat1.age, Cat2.age, Cat3.age)} years old.")
 """


# 125. Encapsulation
# 4 pillars of OOP
# Encapsulation is binding of data and functions.

# 126. Abstraction - Hiding of information and giving access 
# only to what is needed or what we are interested in. 

# 127. Private vs Public variables. 
# use "_" (underscore) to mark a private variable. 

# 128. Inheritance.
"""class User():
    def sign_in(self):
        print("logged in")
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacking with the power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
archer1.attack()
wizard1.attack()"""

# 134. Dunder Methods
'''class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Yoyo",
            "has_pets": False
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5
    
    def __call__(self):
        return("yes?")
    
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])'''

# 134. Exercise: Extending List
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1)

