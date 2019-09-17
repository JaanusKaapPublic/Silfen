from MarkupGeneratorBase import *

class MarkupGeneratorC(MarkupGeneratorBase):
	importedMethods = None

	def __init__(self):
		MarkupGeneratorBase.__init__(self)
		self.importedMethods = {}

	def allocate(self, obj):
		return "char var%d[%d];\n" % (obj.dstId, obj.size)

	def putBuffer(self, obj):
		buf = ""
		for c in obj.buffer:
			buf += "\\x%02X" % ord(c)
		return "memcpy(var%d + %d, \"%s\", %d);\n" % (obj.dstId, obj.offset, buf, len(obj.buffer))

	def putPtr(self, obj):
		return "((char**)(var%d + %d))[0] = var%d;\n" % (obj.dstId, obj.offset, obj.ptrId)

	def pointNewVar(self, obj):
		return "char* var%d = var%d + %d;\n" % (obj.dstId, obj.srcId, obj.offset)

	def copyContent(self, obj):
		return "memcpy(var%d + %d, var%d, %d);\n" % (obj.dstId, obj.offset, obj.srcId, obj.size)

	def callFunc(self, obj):
		if obj.library not in self.importedMethods:
			self.importedMethods[obj.library] = {}
		if obj.function not in self.importedMethods[obj.library]:
			self.importedMethods[obj.library][obj.function] = len(obj.parameters)

		params = []
		for param in obj.parameters:
			if isinstance(param, MarkupCallFuncParamNum):
				params.append(str(param.value))
			elif isinstance(param, MarkupCallFuncParamVar):
				#params.append("(%s)((char**)var%d)[0]" % (param.origType, param.value))
				params.append("((char**)var%d)[0]" % (param.value))
			else:
				raise Exception("Unknworn parameter type")
		#return "*var%d = %s.%s(%s);\n" % (obj.retVarId, obj.library, obj.function, ", ".join(params))
		return "*var%d = %s_ref(%s);\n" % (obj.retVarId, obj.function, ", ".join(params))

	def postCode(self):
		importCodes = ""
		defCodes = ""
		for dll in self.importedMethods:
			dllVar = dll.lower().replace(".dll", "")
			importCodes += "HINSTANCE %s = LoadLibrary(\"%s\");\n" % (dllVar, dll)
			for method in self.importedMethods[dll]:
				importCodes += "%s_def %s_ref = (%s_def)GetProcAddress(%s, \"%s\");\n" % (method, method, method, dllVar, method)
				defCodes += "typedef void* (__stdcall *%s_def)(%s);\n" % (method, ", ".join(["void*"] * self.importedMethods[dll][method]))
		return ("#include <windows.h>\n\n" + defCodes + "\n\n\nint main()\n{\n" + importCodes + "\n\n", "}")
