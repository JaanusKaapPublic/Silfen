class DefFunction:
	library = None
	function = None
	retType = None
	parameters = None

	def __init__(self, library, function, retType, parameters = []):
		self.library = library
		self.function = function
		self.retType = retType
		self.parameters = parameters

	def addParameter(self, parameter):
		self.parameters.append(parameter)