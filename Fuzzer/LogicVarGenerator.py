from random import random
from MarkupGeneratorBase import *
from VarTypes.DefVarTypePtr import DefVarTypePtr
from VarTypes.DefVarTypeInt import DefVarTypeInt
from VarTypes.DefVarTypeBuffer import DefVarTypeBuffer
from VarTypes.DefVarTypeStruct import DefVarTypeStruct
from VarTypes.DefVarTypeHandle import DefVarTypeHandle

class LogicVarGenerator:
	setup = None

	def __init__(self, setup):
		self.setup = setup
		setup.logicVarGenerator = self

	def getOutputVar(self, type):
		if self.setup.variables.hasByType(type):
			if self.setup.newVsOldVar > random():
				return ([], self.setup.variables.getRandomByType(type))

		pointedType = type.pointedType
		if self.setup.variables.hasByType(pointedType):
			if self.setup.newVsOldPointerVar > random():
				pointedObj = self.setup.variables.getRandomByType(pointedType)
				varObj = self.setup.variables.getNevVar(type)
				return ([MarkupAllocate(varObj.varId, type.size), MarkupPutPtr(varObj.varId, pointedObj.varId, 0)], varObj)

		pointedObj = self.setup.variables.getNevVar(pointedType)
		varObj = self.setup.variables.getNevVar(type)
		return ([MarkupAllocate(pointedObj.varId, pointedType.size), MarkupAllocate(varObj.varId, type.size), MarkupPutPtr(varObj.varId, pointedObj.varId, 0)], varObj)


	def getReturnVar(self, type):
		if self.setup.variables.hasByType(type):
			if self.setup.newVsOldVar > random():
				return ([], self.setup.variables.getRandomByType(type))
		varObj = self.setup.variables.getNevVar(type)
		return ([MarkupAllocate(varObj.varId, type.size)], varObj)

	def getInputVar(self, type, varObj = None):
		newCodeBlocks = []

		if varObj is None and self.setup.wrongType > random():
			return self.getInputVar(self.setup.types.getRandom(), varObj)

		if self.setup.variables.hasByTypeInited(type):
			if self.setup.newVsOldVar > random():
				if varObj is None:
					return ([], self.setup.variables.getRandomByTypeInited(type))
				else:
					oldVar = self.setup.variables.getRandomByTypeInited(type)
					return ([MarkupCopyContent(varObj.varId, oldVar.varId, 0, type.size)], self.setup.variables.getRandomByTypeInited(type))

		if isinstance(type, DefVarTypePtr):
			(codeblocks, pointedObj) = self.getInputVar(type.pointedType)
			if varObj is None:
				varObj = self.setup.variables.getNevVar(type)
				newCodeBlocks.append(MarkupAllocate(varObj.varId, type.size))
			newCodeBlocks.append(MarkupPutPtr(varObj.varId, pointedObj.varId, 0))
			varObj.initialized = True
			return (codeblocks + newCodeBlocks, varObj)

		if isinstance(type, DefVarTypeStruct):
			newCodeBlocks = []
			if varObj is None:
				varObj = self.setup.variables.getNevVar(type)
				newCodeBlocks.append(MarkupAllocate(varObj.varId, type.size))
			offset = 0
			for element in varObj.varType.elements:
				subVarObj = self.setup.variables.getNevVar(element.type)
				newCodeBlocks.append(MarkupPointVar(subVarObj.varId, varObj.varId, offset))
				(codeblocks, tmp) = self.getInputVar(subVarObj.varType, subVarObj)
				newCodeBlocks += codeblocks
				offset += element.type.size
			varObj.initialized = True
			return (newCodeBlocks, varObj)

		if isinstance(type, DefVarTypeInt) or isinstance(type, DefVarTypeBuffer):
			if varObj is None:
				varObj = self.setup.variables.getNevVar(type)
				newCodeBlocks.append(MarkupAllocate(varObj.varId, type.size))
			newCodeBlocks.append(MarkupPutBuffer(varObj.varId, 0, type.generateValue()))
			varObj.initialized = True
			return (newCodeBlocks, varObj)

		if isinstance(type, DefVarTypeHandle):
			(code, varObj) = self.setup.logicHelperGenerator.generateHandle(type)
			varObj.initialized = True
			return (code, varObj)

