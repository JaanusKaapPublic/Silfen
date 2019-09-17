from MarkupGeneratorBase import *
from struct import *

class MarkupGeneratorBinary(MarkupGeneratorBase):
	def allocate(self, obj):
		return "\x01" + pack('<II', obj.dstId, obj.size)

	def putBuffer(self, obj):
		return "\x02" + pack('<III', obj.dstId, obj.offset, len(obj.buffer)) + obj.buffer

	def putPtr(self, obj):
		return "\x03" + pack('<III', obj.dstId, obj.offset, obj.ptrId)

	def pointNewVar(self, obj):
		return "\x04" + pack('<III', obj.dstId, obj.srcId, obj.offset)

	def copyContent(self, obj):
		return "\x05" + pack('<IIII', obj.dstId, obj.offset, obj.srcId, obj.size)

	def callFunc(self, obj):
		result = "\x06"
		result += pack('<H', len(obj.library)) + obj.library
		result += pack('<H', len(obj.function)) + obj.function
		result += pack('<III', obj.retVarId, obj.retVarSize, len(obj.parameters))
		for param in obj.parameters:
			if isinstance(param, MarkupCallFuncParamNum):
				result += "\x00" + pack('<Q', param.value)
			elif isinstance(param, MarkupCallFuncParamVar):
				result += "\x01" + pack('<I', param.value)
			else:
				raise Exception("Unknworn parameter type")
		return result

	def parse(self, data):
		codeblocks = []
		while len(data) > 0:
			op = ord(data[0])
			data = data[1:]
			if op == 0x1:
				(dstId, size) = unpack('<II', data[0:8])
				codeblocks.append(MarkupAllocate(dstId, size))
				data = data[8:]
			elif op == 0x2:
				(dstId, offset, size) = unpack('<III', data[0:12])
				buffer = data[12:12+size]
				data = data[12+size:]
				codeblocks.append(MarkupPutBuffer(dstId, offset, buffer))
			elif op == 0x3:
				(dstId, offset, ptrId) = unpack('<III', data[0:12])
				data = data[12:]
				codeblocks.append(MarkupPutPtr(dstId, ptrId, offset))
			elif op == 0x4:
				(dstId, srcId, offset) = unpack('<III', data[0:12])
				data = data[12:]
				codeblocks.append(MarkupPointVar(dstId, srcId, offset))
			elif op == 0x5:
				(dstId, offset, srcId, size) = unpack('<IIII', data[0:16])
				data = data[16:]
				codeblocks.append(MarkupCopyContent(dstId, srcId, offset, size))
			elif op == 0x6:
				libLen = unpack('<H', data[0:2])[0]
				lib = data[2:2+libLen]
				data = data[2+libLen:]
				funcLen = unpack('<H', data[0:2])[0]
				func = data[2:2+funcLen]
				data = data[2+funcLen:]

				(retVarId, retVarSize, paramCount) = unpack('<III', data[0:12])
				data = data[12:]

				params = []
				for x in xrange(paramCount):
					if ord(data[0]) == 0:
						value = unpack('<Q', data[1:9])[0]
						data = data[9:]
						params.append(MarkupCallFuncParamNum(value))
					elif ord(data[0]) == 1:
						value = unpack('<I', data[1:5])[0]
						data = data[5:]
						params.append(MarkupCallFuncParamVar(value))

				codeblocks.append(MarkupCallFunc(lib, func, retVarId, retVarSize, params))
			else:
				raise Exception("Unknown command 0x%X" % op)
		return codeblocks


