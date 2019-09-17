from DefVariable import DefVariable
import random

class ManagerVariables:
	setup = None
	variablesByTypes = None
	variablesByTypesInited = None
	variablesByIds = None

	nextId = 0

	def __init__(self, setup):
		self.clear()
		self.setup = setup
		setup.variables = self

	def clear(self):
		self.variablesByTypes = {}
		self.variablesByIds = {}
		self.nextId = 0


	def getNevVar(self, type, name = None):
		varObj = DefVariable(self.nextId, type, name)
		self.addVar(varObj)
		self.nextId += 1
		return varObj

	def addVar(self, variable):
		if variable.varType.name not in self.variablesByTypes:
			self.variablesByTypes[variable.varType.name] = []
		self.variablesByIds[variable.varId] = variable
		self.variablesByTypes[variable.varType.name].append(variable)

	def getVar(self, id):
		if id not in self.variablesByIds:
			return None
		return self.variablesByIds[id]

	def hasByType(self, type):
		if not isinstance(type, basestring):
			type = type.name
		return (type in self.variablesByTypes)

	def getByType(self, type):
		if not isinstance(type, basestring):
			type = type.name
		if type not in self.variablesByTypes:
			return None
		return self.variablesByTypes[type]

	def getRandomByType(self, type):
		if not isinstance(type, basestring):
			type = type.name
		if type not in self.variablesByTypes:
			return None
		return random.choice(self.variablesByTypes[type])

	def hasByTypeInited(self, type):
		if not isinstance(type, basestring):
			type = type.name
		if type not in self.variablesByTypes:
			return False
		for var in self.variablesByTypes[type]:
			if var.initialized:
				return True
		return False

	def getByTypeInited(self, type):
		if not isinstance(type, basestring):
			type = type.name
		if type not in self.variablesByTypes:
			return None
		result = []
		for var in self.variablesByTypes[type]:
			if var.initialized:
				result.append(var)
		return result

	def getRandomByTypeInited(self, type):
		if not isinstance(type, basestring):
			type = type.name
		if type not in self.variablesByTypes:
			return None
		result = []
		for var in self.variablesByTypes[type]:
			if var.initialized:
				result.append(var)
		return random.choice(result)


