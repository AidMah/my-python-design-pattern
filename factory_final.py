class Pet:

    """A simple pet class"""

    def __init__(self, name):
        self._name = name
        self._sound = "Silence"

    def __eq__(self, other):
        """
        Magic method for equality comparison (==)
        Compares two Pet objects based on their sound, not their name
        Example: Dog("Rex") == Dog("Max") returns True (both bark "Woof!")
        """
        if isinstance(other, Pet):  # Check if 'other' is also a Pet object
            return (self._sound) == (other._sound)  # Compare sounds
        return NotImplemented  # Let Python handle comparison with non-Pet objects

    def __str__(self):
        """
        Magic method for string representation
        Defines how the object appears when printed or converted to string
        Returns format: "Name | Sound" (e.g., "Hope | Woof!")
        """
        return '{} | {}'.format(self._name, self._sound)

    def speak(self):
        return self._sound

class Dog(Pet):

    def __init__(self, name):
        Pet.__init__(self, name)
        self._sound = "Woof!"

class Cat(Pet):

    """A simple cat class"""

    def __init__(self, name):
        Pet.__init__(self, name)
        self._sound = "Meow!"
    
class Pig(Pet):

    """A simple Pig class"""

    def __init__(self, name):
        Pet.__init__(self, name)
        self._sound = "Oink!"

def get_pet(pet="dog"):

    """The factory method"""

    # Your code to create and add a pig goes here
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"), pig=Pig("Piggy"))

    return pets[pet]

def get_pig():
    pig = get_pet("pig")
    print(f"get_pig() function says: {pig.speak()}")  # Debug or demonstration
    return pig


d = get_pet("dog")
print(d.speak())
print(d)

c = get_pet("cat")

print(c)
print(c.speak())

p = get_pet("pig")
print(p.speak())
p2 = get_pig()