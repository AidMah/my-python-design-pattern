class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        # return '{} | {} | {}'.format(self.model, self.tires, self.engine)
        return f"{self.model} | {self.tires} | {self.engine}"
    
class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None 
        
    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """
    def __init__(self):
        super().__init__()
        
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self,tires="Regular tires"):
        self.car.tires = "Regular tires"

    def add_engine(self):    
        self.car.engine = "Turbo engine"

class FerrariBuilder(Builder):
    """Another Concrete Builder for Ferrari cars"""
    def __init__(self):
        super().__init__()
        
    def add_model(self):
        self.car.model = "Ferrari 488"

    def add_tires(self):
        self.car.tires = "Performance racing tires"

    def add_engine(self):    
        self.car.engine = "V8 Twin-Turbo engine"


class ToyotaBuilder(Builder):
    """Another Concrete Builder for Toyota cars"""
    def __init__(self):
        super().__init__()
        
    def add_model(self):
        self.car.model = "Toyota Camry"

    def add_tires(self):
        self.car.tires = "All-season tires"

    def add_engine(self):    
        self.car.engine = "4-cylinder Hybrid engine"

class FerrariF80Builder(Builder):
    """Specific Concrete Builder for Ferrari F80"""
    def __init__(self):
        super().__init__()
        
    def add_model(self):
        self.car.model = "Ferrari F80"

    def add_tires(self):
        self.car.tires = "Michelin Pilot Sport Cup 2 R"

    def add_engine(self):    
        self.car.engine = "V6 Hybrid 1200hp"


class FlexibleFerrariBuilder(Builder):
    """Flexible Ferrari Builder - can build different Ferrari models"""
    def __init__(self, model="Ferrari 488", tires="Performance racing tires", engine="V8 Twin-Turbo engine"):
        super().__init__()
        self.ferrari_model = model
        self.ferrari_tires = tires
        self.ferrari_engine = engine
        
    def add_model(self):
        self.car.model = self.ferrari_model

    def add_tires(self):
        self.car.tires = self.ferrari_tires

    def add_engine(self):    
        self.car.engine = self.ferrari_engine


class Director():
    """Director"""
    def __init__(self, builder):
        self._builder = builder 
       
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()
        
    def get_car(self):
        return self._builder.car





# Example usage with different builders
print("=== Building Different Cars ===")

# Build a Skylark
skylark_builder = SkyLarkBuilder()
print("Before construction:", skylark_builder.car)

director = Director(skylark_builder)
director.construct_car()
skylark_car = director.get_car()
print("Skylark Car:", skylark_car)

# Build a Ferrari using the same Director but different Builder
ferrari_builder = FerrariBuilder()
director = Director(ferrari_builder)
director.construct_car()
ferrari_car = director.get_car()
print("Ferrari Car:", ferrari_car)

# Build a Toyota
toyota_builder = ToyotaBuilder()
director = Director(toyota_builder)
director.construct_car()
toyota_car = director.get_car()
print("Toyota Car:", toyota_car)

print("\n=== Building Ferrari Variations ===")

# Build Ferrari F80 using dedicated builder
ferrari_f80_builder = FerrariF80Builder()
director = Director(ferrari_f80_builder)
director.construct_car()
ferrari_f80_car = director.get_car()
print("Ferrari F80:", ferrari_f80_car)

# Build different Ferrari models using flexible builder
# Ferrari LaFerrari
laferrari_builder = FlexibleFerrariBuilder(
    model="Ferrari LaFerrari", 
    tires="Pirelli P Zero Corsa", 
    engine="V12 Hybrid 950hp"
)
director = Director(laferrari_builder)
director.construct_car()
laferrari_car = director.get_car()
print("Ferrari LaFerrari:", laferrari_car)

# Ferrari SF90
sf90_builder = FlexibleFerrariBuilder(
    model="Ferrari SF90 Stradale", 
    tires="Michelin Pilot Sport Cup 2", 
    engine="V8 Hybrid 986hp"
)
director = Director(sf90_builder)
director.construct_car()
sf90_car = director.get_car()
print("Ferrari SF90:", sf90_car)
