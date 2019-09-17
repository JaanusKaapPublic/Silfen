class DefParameter:
	paramType = None
	paramIn = None
	paramOut = None
	paramOptional = None

	paramName = None
	paramOriginalType = None

	def __init__(self, paramType, paramIn, paramOut, paramOptional, paramName = None, paramOriginalType = None):
		self.paramType = paramType
		self.paramIn = paramIn
		self.paramOut = paramOut
		self.paramOptional = paramOptional
		self.paramName = paramName
		self.paramOriginalType = paramOriginalType