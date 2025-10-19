class Pet:

	"""A simple pet class"""

	def __init__(self, name):
		self._name = name
		self._sound = "Silence"

	def __eq__(self, other):
		if isinstance(other, Pet):
			return (self._sound) == (other._sound)
		return NotImplemented

	def __str__(self):
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
	
class Pig (Pet):

	"""A simple Pig class"""

	def __init__(self, name):
		Pet.__init__(self, name)
		self._sound = "Oink!"

def get_pet(pet="dog"):

	"""The factory method"""

#Your code to create and add a pig goes here
	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"),pig=Pig("Piggy"))

	return pets[pet]

def get_pig():
    pig = get_pet("pig")
    print(pig.speak())  # Debug or demonstration
    return pig
    return Pet("Unknown")



d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())

p= get_pet("pig")
print(p.speak())







