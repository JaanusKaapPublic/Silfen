from random import random
from DefParameter import DefParameter
from MarkupGeneratorBase import MarkupCallFunc, MarkupCallFuncParamNum, MarkupCallFuncParamVar

class LogicFuncGenerator:
	setup = None

	def __init__(self, setup):
		self.setup = setup
		setup.logicFuncGenerator = self

	def callFunc(self, func):
		newCodeBlocks = []
		parameters = []
		(codeblocks, resultVar) = self.setup.logicVarGenerator.getReturnVar(func.retType)
		newCodeBlocks += codeblocks
		varsToSetIninted = []
		for param in func.parameters:
			if param.paramOptional and self.setup.optionalAsNull > random():
				parameters.append(MarkupCallFuncParamNum(0))
			elif not param.paramIn:
				(codeblocks, varObj) = self.setup.logicVarGenerator.getOutputVar(param.paramType)
				newCodeBlocks += codeblocks
				parameters.append(MarkupCallFuncParamVar(varObj.varId, param.paramOriginalType))
				varsToSetIninted.append(varObj)
			else:
				(codeblocks, varObj) = self.setup.logicVarGenerator.getInputVar(param.paramType)
				newCodeBlocks += codeblocks
				parameters.append(MarkupCallFuncParamVar(varObj.varId, param.paramOriginalType))

		newCodeBlocks.append(MarkupCallFunc(func.library, func.function, resultVar.varId, resultVar.varType.size, parameters))
		resultVar.initialized = True
		for varToSetIninted in varsToSetIninted:
			varToSetIninted.initialized = True
		return newCodeBlocks


