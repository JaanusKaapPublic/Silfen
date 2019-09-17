from ManagerFunctions import ManagerFunctions
from ManagerTypes import ManagerTypes
from ManagerVariables import ManagerVariables

class FuzzSetupManager:
	functions = None
	types = None
	variables = None

	logicVarGenerator = None
	logicFuncGenerator = None
	logicHelperGenerator = None

	def __init__(self):
		self.newVsOldVar = 0.5
		self.newVsOldPointerVar = 0.5
		self.optionalAsNull = 0.5
		self.wrongType = 0.1
