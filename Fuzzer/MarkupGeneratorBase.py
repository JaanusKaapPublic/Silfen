class MarkupAllocate:
	dstId = None
	size = None

	name = None
	comment = None

	def __init__(self, dstId, size, name = None, comment = None):
		self.dstId = dstId
		self.size = size
		self.name = name
		self.comment = comment

class MarkupPutBuffer:
	dstId = None
	offset = None
	buffer = None

	comment = None

	def __init__(self, dstId, offset, buffer, comment = None):
		self.dstId = dstId
		self.offset = offset
		self.buffer = buffer
		self.comment = comment

class MarkupPutPtr:
	dstId = None
	ptrId = None
	offset = None

	comment = None

	def __init__(self, dstId, ptrId, offset, comment = None):
		self.dstId = dstId
		self.ptrId = ptrId
		self.offset = offset
		self.comment = comment

class MarkupPointVar:
	dstId = None
	srcId = None
	offset = None

	comment = None

	def __init__(self, dstId, srcId, offset, comment = None):
		self.dstId = dstId
		self.srcId = srcId
		self.offset = offset
		self.comment = comment

class MarkupCopyContent:
	dstId = None
	srcId = None
	offset = None
	size = None

	comment = None

	def __init__(self, dstId, srcId, offset, size, comment = None):
		self.dstId = dstId
		self.srcId = srcId
		self.offset = offset
		self.size = size
		self.comment = comment

class MarkupCallFuncParamNum:
	value = None

	def __init__(self, value):
		self.value = value

class MarkupCallFuncParamVar:
	value = None
	origType = None

	def __init__(self, value, origType = None):
		self.value = value
		self.origType = origType

class MarkupCallFunc:
	library = None
	function = None
	retVarId = None
	retVarSize = None
	parameters = None

	comment = None

	def __init__(self, library, function, retVarId, retVarSize, parameters, comment = None):
		self.library = library
		self.function = function
		self.retVarId = retVarId
		self.retVarSize = retVarSize
		self.parameters = parameters
		self.comment = comment

	def addParam(self, param):
		self.parameters.append(param)

class MarkupGeneratorBase:
	codeObjects = None

	def __init__(self):
		self.codeObjects = []

	def addCode(self, obj):
		self.codeObjects.append(obj)

	def addCodes(self, obj):
		self.codeObjects += obj

	def addCodeToStart(self, obj):
		self.codeObjects = [obj] + self.codeObjects

	def generate(self):
		result = self.preCode();
		for obj in self.codeObjects:
			if isinstance(obj, MarkupAllocate):
				result += self.allocate(obj)
			elif isinstance(obj, MarkupPutBuffer):
				result += self.putBuffer(obj)
			elif isinstance(obj, MarkupPutPtr):
				result += self.putPtr(obj)
			elif isinstance(obj, MarkupPointVar):
				result += self.pointNewVar(obj)
			elif isinstance(obj, MarkupCopyContent):
				result += self.copyContent(obj)
			elif isinstance(obj, MarkupCallFunc):
				result += self.callFunc(obj)
			else:
				raise Exception("Unknown code type provided to the markup code generator")
		(tmpPre, tmpPost) = self.postCode();
		result = tmpPre + result + tmpPost
		return result

	def preCode(self):
		return ""

	def postCode(self):
		return ("", "")

	def allocate(self, obj):
		raise Exception("Function allocate is not implemented")

	def putBuffer(self, obj):
		raise Exception("Function putBuffer is not implemented")

	def putPtr(self, obj):
		raise Exception("Function putPtr is not implemented")

	def pointNewVar(self, obj):
		raise Exception("Function pointNewVar is not implemented")

	def copyContent(self, obj):
		raise Exception("Function copyContent is not implemented")

	def callFunc(self, obj):
		raise Exception("Function callFunc is not implemented")