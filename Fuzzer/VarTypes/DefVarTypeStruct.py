class DefVarTypeStructElement:
	name = None
	type = None

	def __init__(self, name, type):
		self.name = name
		self.type = type

class DefVarTypeStruct:
	name = None
	size = None
	elements = None

	def __init__(self, name, elements = []):
		self.name = name
		self.size = 0
		self.elements = []
		for element in elements:
			self.addElement(element)

	def addElement(self, element):
		self.elements.append(element)
		self.size += element.type.size