class Subject(object): #Represents what is being 'observed'

	def __init__(self):
		self._observers = [] # This where references to all the observers are being kept
							 # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

	def attach(self, observer):
		if observer not in self._observers: #If the observer is not already in the observers list
			self._observers.append(observer) # append the observer to the list

	def detach(self, observer): #Simply remove the observer
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		for observer in self._observers: # For all the observers in the list
			if modifier != observer: # Don't notify the observer who is actually updating the temperature 
				observer.update(self) # Alert the observers!

class Core(Subject): #Inherits from the Subject class

	def __init__(self, name=""):
		Subject.__init__(self) #Call the constructor of the Subject class to initialize the list of observers self._observers = [] in the Subject class
		self._name = name #Set the name of the core
		self._temp = 0 #Initialize the temperature of the core

	@property #Getter that gets the core temperature
	def temp(self):
		return self._temp

	@temp.setter #Setter that sets the core temperature
	def temp(self, temp):
		self._temp = temp
		self.notify() #Notify the observers whenever somebody changes the core temperature

	def __str__(self):
		return "{} has Temperature {}".format(self._name, self._temp)

class TempViewer:

	def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
		print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))

#Let's create our subjects
c1 = Core("Core 1") #Create a core named "Core 1" 
c2 = Core("Core 2")
c3 = Core("Core 3")

#Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

#Let's attach our observers to the first core
c1.attach(v1) #Attach the first observer to the first core by inserting it into the list of observers in the first core
c2.attach(v2) #Attach the second observer to the second core
c3.attach(v2) #Attach the second observer to the third core

#Let's change the temperature of our first core
c1.temp = 80
print(c1)
''''''
c2.temp = 90
c3.temp = 110

