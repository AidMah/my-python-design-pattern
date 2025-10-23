class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class Cat:
	"""Another pet object to be returned"""

	def speak(self):
		return "Meow!"

	def __str__(self):
		return "Cat"
	
	


class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Dog Food!"


class CatFactory:
	"""Concrete Factory for Cat"""

	def get_pet(self):
		"""Returns a Cat object"""
		return Cat()

	def get_food(self):
		"""Returns a Cat Food object"""
		return "Cat Food!"


class PetStore:
	""" PetStore houses our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """

		self._pet_factory = pet_factory


	def show_pet(self):
		""" Utility method to display the details of the objects retured by the DogFactory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


#Create a Concrete Factory
factory = DogFactory()
 # Debug or demonstration
print(factory.get_pet().speak()) 

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()

print("\n" + "="*50)
print("Now let's try with a Cat Factory!")
print("="*50)

#Create a Cat Factory
cat_factory = CatFactory()
print(cat_factory.get_pet().speak())  # Debug demonstration

#Create a pet store with Cat Factory
cat_shop = PetStore(cat_factory)

#Show the cat details
cat_shop.show_pet()

