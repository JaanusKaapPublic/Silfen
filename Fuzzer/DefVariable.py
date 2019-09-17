class DefVariable:
	varId = None
	varType = None
	initialized = False

	varName = None

	def __init__(self, varId, varType, varName = None):
		self.varId = varId
		self.varType = varType
		self.varName = varName

	def initialize(self):
		self.initialized = True
