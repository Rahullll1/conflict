#single inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Create an object of Dog
dog = Dog()
dog.sound()  # Inherited from Animal
dog.bark()   # Defined in Dog
#multiple inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Bird:
    def fly(self):
        print("Bird flies")

class Sparrow(Animal, Bird):
    pass

# Create an object of Sparrow
sparrow = Sparrow()
sparrow.sound()  # Inherited from Animal
sparrow.fly()    # Inherited from Bird
#multilevel inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Puppy(Dog):
    def cute(self):
        print("Puppy is cute")

# Create an object of Puppy
puppy = Puppy()
puppy.sound()  # Inherited from Animal
puppy.bark()   # Inherited from Dog
puppy.cute()   # Defined in Puppy
#hierarchial 
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

dog.sound()  # Inherited from Animal
dog.bark()

cat.sound()  # Inherited from Animal
cat.meow()
#hybrid
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Bird(Animal):
    def fly(self):
        print("Bird flies")

class Fish(Animal):
    def swim(self):
        print("Fish swims")

class Penguin(Bird, Fish):
    def walk(self):
        print("Penguin walks")

# Create an object of Penguin
penguin = Penguin()
penguin.sound()  # Inherited from Animal
penguin.fly()    # Inherited from Bird
penguin.swim()   # Inherited from Fish
penguin.walk()   # Defined in Penguin
