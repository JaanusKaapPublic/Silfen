from random import randint

class DefVarTypeBuffer:
	name = None
	size = None
	maxLength = 0x20
	isStr = False
	isWStr = False
	validInputs = None

	def __init__(self, name, maxLength = 0x20, isStr = False, isWStr = False, validInputs = None):
		self.name = name
		self.size = maxLength
		self.maxLength = maxLength
		self.isStr = isStr
		self.isWStr = isWStr
		self.validInputs = validInputs

	def generateValue(self, validValueProb = 1):
		if self.validInputs is not None:
			if validValueProb > random():
				return self.generateValidValue()
		return self.generateRandomValue()

	def generateRandomValue(self):
		result = ""
		size = randint(2, self.maxLength)
		if self.isStr:
			size -= 1
		elif self.isWStr:
			size -= 2
			size = int(size/2)

		for x in xrange(size):
			if self.isStr:
				result += chr(randint(0, 128))
			elif self.isWStr:
				result += chr(randint(0, 128)) + "\x00"
			else:
				result += chr(randint(0, 255))

		if self.isStr:
			result += "\x00"
		if self.isWStr:
			result += "\x00\x00"

		return result

	def generateValidValue(self):
		value = choice(self.validInputs)
		return pack("<" + self.generationData[self.size][0], value)