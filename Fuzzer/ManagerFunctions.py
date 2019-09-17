from DefParameter import DefParameter
from DefFunction import DefFunction
from random import choice, randint

class ManagerFunctions:
	level = 1
	setup = None
	funcs = None


	def __init__(self, setup):
		self.funcs = {}
		self.setup = setup
		setup.functions = self

	def add(self, func):
		self.funcs[func.function] = func

	def get(self, name = None):
		if name is None:
			return self.funcs[choice(self.funcs.keys())]
		else:
			if name not in self.funcs:
				return None
		return self.funcs[name]

	def load(self, data):
		for type in data:
			self.loadSingleFunc(type, data[type])

	def loadSingleFunc(self, name, func):
		if 'level' in func and func['level'] > self.level:
			return True
		if 'disabled' in func and func['disabled']:
			return True

		retType = self.setup.types.get(func['retVal'])
		params = []
		for param in func['params']:
			if param['type'] == "?":
				if param['out'] or randint(0, 1) == 1:
					param['type'] = 'pint64'
				else:
					param['type'] = 'int64'
			paramType = self.setup.types.get(param['type'])
			if paramType is None:
				raise Exception("Could not load function '%s' because it contains parameter type '%s'" % (name, param['type']))
			params.append(DefParameter(paramType, param['in'], param['out'], param['optional'], paramName = param['name'], paramOriginalType = param['type']))
		self.add(DefFunction(func['lib'], name, retType, params))
		return True

	def remove(self, funcName):
		if funcName in self.funcs:
			del self.funcs[funcName]
