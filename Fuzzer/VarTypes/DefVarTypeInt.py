from struct import pack
from random import randint, choice, random

class DefVarTypeInt:
	generationData = {1: ('B', 0xFF), 2: ('H', 0xFFFF), 4: ('I', 0xFFFFFFFF), 8: ('Q', 0xFFFFFFFF)}
	validInputs = None
	name = None
	size = None

	def __init__(self, name, size, validInputs = None):
		self.name = name
		self.size = size
		self.validInputs = validInputs

	def generateValue(self, validValueProb = 1):
		if self.validInputs is not None:
			if validValueProb > random():
				return self.generateValidValue()
		return self.generateRandomValue()

	def generateRandomValue(self):
		size = self.size
		while True:
			if size == 1 or randint(0, 1) == 0:
				return pack("<" + self.generationData[self.size][0], randint(0, self.generationData[size][1]))
			size = size / 2

	def generateValidValue(self):
		value = choice(self.validInputs)
		return pack("<" + self.generationData[self.size][0], value)