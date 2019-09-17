class DefVarTypePtr:
	name = None
	size = 8
	pointedType = None

	def __init__(self, name, pointedType):
		self.name = name
		self.pointedType = pointedType