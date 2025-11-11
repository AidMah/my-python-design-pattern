import copy

class Prototype:
    
    def __init__(self):
        self._objects = {} # Registry to hold prototypes, key is Name, value is Object
        
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj # Store the object in the registry with key as Name
        
    def unregister_object(self, name):
        """Unregister an object"""
        # Remove the object from the registry by key which is Name
        del self._objects[name]
        
    def clone(self, name, **attr): #c1 = prototype.clone('skylark', color='Blue')
        """Clone a registered object and update its attributes"""
        # Deep copy the prototype object from the registry
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
        
class Car:
    def __init__(self, name="Skylark", color="Red", options="Ex"):
        """
        Flexible Car class that accepts inputs
        
        Args:
            name (str): The model name of the car
            color (str): The color of the car
            options (str): The options/features of the car
        """
        self.name = name
        self.color = color
        self.options = options
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
        
# Example 1: Create default car
c = Car()
print("Default Car:", c)

# Example 2: Create custom cars with different inputs
ferrari = Car(name="Ferrari 488", color="Red", options="Sport Package")
print("Ferrari:", ferrari)

tesla = Car(name="Tesla Model S", color="Blue", options="Autopilot")
print("Tesla:", tesla)

toyota = Car(name="Toyota Camry", color="Silver", options="Standard")
print("Toyota:", toyota)

# Register prototypes
prototype = Prototype()
prototype.register_object('skylark', c)
prototype.register_object('ferrari', ferrari)
prototype.register_object('tesla', tesla)

# Clone and modify
print("\n=== Cloning Examples ===")

# Clone skylark with modifications
c1 = prototype.clone('skylark', color='Blue')
c2 = prototype.clone('skylark', color='Brown')
print("Cloned Skylark (Blue):", c1)
print("Cloned Skylark (Brown):", c2)

# Clone ferrari with different color
ferrari_clone = prototype.clone('ferrari', color='Yellow', options='Racing Package')
print("Cloned Ferrari (Modified):", ferrari_clone)

# Clone tesla as-is
tesla_clone = prototype.clone('tesla')
print("Cloned Tesla (Same):", tesla_clone)

# Verify original objects are unchanged
print("\n=== Original Objects (Unchanged) ===")
print("Original Skylark:", c)
print("Original Ferrari:", ferrari)
print("Original Tesla:", tesla)
