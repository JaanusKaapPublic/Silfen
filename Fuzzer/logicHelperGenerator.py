import random
from MarkupGeneratorBase import *

class logicHelperGenerator:
	setup = None

	def __init__(self, setup):
		self.setup = setup
		setup.logicHelperGenerator = self

	def generateHandle(self, type):
		(newCodeBlocks, varObj) = self.setup.logicVarGenerator.getReturnVar(type)
		if type.name == "HWND":
			newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getWindow", varObj.varId, varObj.varType.size, []))
			return (newCodeBlocks, varObj)
		else:
			op = random.randint(0, 7)
			if op == 0:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getProcess", varObj.varId, varObj.varType.size, []))
			elif op == 1:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getThread", varObj.varId, varObj.varType.size, []))
			elif op == 2:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getAccessToken", varObj.varId, varObj.varType.size, []))
			elif op == 3:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getEvent", varObj.varId, varObj.varType.size, []))
			elif op == 4:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getMutex", varObj.varId, varObj.varType.size, []))
			elif op == 5:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getPipeRead", varObj.varId, varObj.varType.size, []))
			elif op == 6:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getPipeWrite", varObj.varId, varObj.varType.size, []))
			elif op == 7:
				newCodeBlocks.append(MarkupCallFunc("HelperDll.dll", "getFile", varObj.varId, varObj.varType.size, []))
			return (newCodeBlocks, varObj)