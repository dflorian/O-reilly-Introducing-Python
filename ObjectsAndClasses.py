#! python3
# 10.1
class Thing():
	pass

Example = Thing()
print(Example)

# 10.2
class Thing2():
	letters = 'abc'

print(Thing2.letters)

#10.3
class Thing3():
	def __init__(self):
		self.letters = 'xyz'

#print(Thing3.letters) => error
print(Thing3().letters)

#10.4
class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

Element('Hydrogen', 'H', 1)

#10.5
dic_hydrogen = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dic_hydrogen)

#10.6
class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

	def dump(self):
		print(self.name + ", " + self.symbol + ", " + str(self.number))

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()

#10.7
print(hydrogen)
class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

	def __str__(self):
		return(self.name + ", " + self.symbol + ", " + str(self.number))

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)

#10.8
class Element():
	def __init__(self, name, symbol, number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number

	@property
	def name(self):
		return self.__name

	@property
	def symbol(self):
		return self.__symbol

	@property
	def number(self):
		return self.__number
	
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.number)

#10.9
class Bear():
	def eats(self):
		return 'berries'

class Rabbit():
	def eats(self):
		return 'clover'

class Octothorpe():
	def eats(self):
		return 'campers'

print(Bear().eats())
print(Rabbit().eats())
print(Octothorpe().eats())

#10.10
class Laser():
	def does(self):
		return 'disintegrate'

class Claw():
	def does(self):
		return 'crush'

class SmartPhone():
	def does(self):
		return 'ring'

class Robot():
	def __init__(self):
		self.laser = Laser()
		self.claw = Claw()
		self.smartphone = SmartPhone()

	def does(self):
		print('''Ready! I have a laser to %s, \
a claw to %s and a smartphone to %s!''' % (
			self.laser.does(),
			self.claw.does(),
			self.smartphone.does()))

Robot().does()