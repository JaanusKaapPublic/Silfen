import random
from VarTypes.DefVarTypeInt import DefVarTypeInt
from VarTypes.DefVarTypePtr import DefVarTypePtr
from VarTypes.DefVarTypeHandle import DefVarTypeHandle
from VarTypes.DefVarTypeBuffer import DefVarTypeBuffer
from VarTypes.DefVarTypeStruct import DefVarTypeStruct, DefVarTypeStructElement

class ManagerTypes:
	setup = None
	types = None

	lastError = None

	def __init__(self, setup):
		self.types = {}
		self.setup = setup
		setup.types = self

	def add(self, type):
		self.types[type.name] = type

	def addRef(self, name, type):
		self.types[name] = type

	def get(self, name):
		if name not in self.types:
			return None
		return self.types[name]

	def getRandom(self):
		return self.types[random.choice(self.types.keys())]

	def init(self):
		self.add(DefVarTypeInt("int8", 1))
		self.add(DefVarTypeInt("int16", 2))
		self.add(DefVarTypeInt("int32", 4))
		self.add(DefVarTypeInt("int64", 8))
		self.add(DefVarTypePtr("pint8", self.get("int8")))
		self.add(DefVarTypePtr("pint16", self.get("int16")))
		self.add(DefVarTypePtr("pint32", self.get("int32")))
		self.add(DefVarTypePtr("pint64", self.get("int64")))

		self.add(DefVarTypeBuffer("buf"))
		self.add(DefVarTypeBuffer("code"))
		self.add(DefVarTypeBuffer("str", isStr = True))
		self.add(DefVarTypeBuffer("wstr", isWStr= True))
		self.add(DefVarTypePtr("pbuf", self.get("buf")))
		self.add(DefVarTypePtr("pcode", self.get("code")))
		self.add(DefVarTypePtr("pstr", self.get("str")))
		self.add(DefVarTypePtr("pwstr", self.get("wstr")))
		self.add(DefVarTypePtr("ppbuf", self.get("pbuf")))

		self.add(DefVarTypeHandle("HANDLE"))
		self.add(DefVarTypeHandle("HDC"))
		self.add(DefVarTypeHandle("HWND"))
		self.add(DefVarTypeHandle("HMENU"))
		self.add(DefVarTypeHandle("HBITMAP"))
		self.add(DefVarTypeHandle("HBRUSH"))
		self.add(DefVarTypeHandle("HSURF"))
		self.add(DefVarTypeHandle("HDEV"))
		self.add(DefVarTypeHandle("HINSTANCE"))
		self.add(DefVarTypeHandle("HICON"))
		self.add(DefVarTypeHandle("HCURSOR"))
		self.add(DefVarTypeHandle("HWINSTA"))
		self.add(DefVarTypeHandle("HRGN"))
		self.add(DefVarTypeHandle("HFONT"))
		self.add(DefVarTypeHandle("HACCEL"))
		self.add(DefVarTypeHandle("HLSURF"))
		self.add(DefVarTypeHandle("HWINEVENTHOOK"))
		self.add(DefVarTypeHandle("HDESK"))
		self.add(DefVarTypeHandle("HDWP"))
		self.add(DefVarTypeHandle("HPALETTE"))
		self.add(DefVarTypeHandle("HCOLORSPACE"))
		self.add(DefVarTypeHandle("HGDIOBJ"))
		self.add(DefVarTypeHandle("HHOOK"))
		self.add(DefVarTypeHandle("HMONITOR"))
		self.add(DefVarTypeHandle("HUMPD"))
		self.add(DefVarTypeHandle("HMODULE"))
		self.add(DefVarTypeHandle("HPEN"))
		self.add(DefVarTypeHandle("HRAWINPUT"))
		self.add(DefVarTypePtr("PHANDLE", self.get("HANDLE")))
		self.add(DefVarTypePtr("PHDC", self.get("HDC")))
		self.add(DefVarTypePtr("PHWND", self.get("HWND")))
		self.add(DefVarTypePtr("PHMENU", self.get("HMENU")))
		self.add(DefVarTypePtr("PHBITMAP", self.get("HBITMAP")))
		self.add(DefVarTypePtr("PHBRUSH", self.get("HBRUSH")))
		self.add(DefVarTypePtr("PHSURF", self.get("HSURF")))
		self.add(DefVarTypePtr("PHDEV", self.get("HDEV")))
		self.add(DefVarTypePtr("PHINSTANCE", self.get("HINSTANCE")))
		self.add(DefVarTypePtr("PHCURSOR", self.get("HCURSOR")))
		self.add(DefVarTypePtr("PHWINSTA", self.get("HWINSTA")))
		self.add(DefVarTypePtr("PHRGN", self.get("HRGN")))
		self.add(DefVarTypePtr("PHFONT", self.get("HFONT")))
		self.add(DefVarTypePtr("PHACCEL", self.get("HACCEL")))
		self.add(DefVarTypePtr("PHLSURF", self.get("HLSURF")))
		self.add(DefVarTypePtr("PHWINEVENTHOOK", self.get("HWINEVENTHOOK")))
		self.add(DefVarTypePtr("PHDESK", self.get("HDESK")))
		self.add(DefVarTypePtr("PHDWP", self.get("HDWP")))
		self.add(DefVarTypePtr("PHPALETTE", self.get("HPALETTE")))
		self.add(DefVarTypePtr("PHGDIOBJ", self.get("HGDIOBJ")))
		self.add(DefVarTypePtr("PHHOOK", self.get("HHOOK")))
		self.add(DefVarTypePtr("PHMONITOR", self.get("HMONITOR")))
		self.add(DefVarTypePtr("PHUMPD", self.get("HUMPD")))
		self.add(DefVarTypePtr("PHMODULE", self.get("HMODULE")))
		self.add(DefVarTypePtr("PHPEN", self.get("HPEN")))
		self.add(DefVarTypePtr("PHRAWINPUT", self.get("HRAWINPUT")))

		return self

	def loadSimpleTypes(self, data):
		while True:
			lastFail = None
			oneFailed = False
			oneSucceeded = False

			for type in data:
				res = self.loadSingleType(type, data[type])
				if res is not None:
					if res:
						oneSucceeded = True
					else:
						oneFailed = True
						lastFail = type
			if not oneFailed:
				break
			if not oneSucceeded:
				raise Exception("Could not read datatypes - last failed type was '%s'!" % lastFail)

	def loadSingleType(self, name, value):
		if self.get(name) != None:
			return None
		if self.get(value) == None:
			return False
		self.addRef(name, self.get(value))
		return True

	def loadEnums(self, data):
		for type in data:
			if isinstance(data[type], list):
				self.addRef(type, self.get("int32"))
			else:
				self.addRef(type, self.get("pint32"))

	def loadStructures(self, data):
		while True:
			lastFail = None
			oneFailed = False
			oneSucceeded = False
			for type in data:
				if isinstance( data[type], list):
					res = self.loadSingleStruct(type, data[type], data)
				else:
					res = self.loadSingleStructPointer(type, data[type])
				if res is not None:
					if res:
						oneSucceeded = True
					else:
						oneFailed = True
						lastFail = type
			if not oneFailed:
				break
			if not oneSucceeded:
				raise Exception("Could not read structures - last failed structure was '%s'!\n%s" % (lastFail, self.lastError))

	def loadSingleStruct(self, name, value, dataAll = {}):
		if self.get(name) != None:
			return None
		structObj = DefVarTypeStruct(name)
		for element in value:
			type = self.get(element['type'])
			if type is None:
				if element['type'] not in dataAll:
					self.lastError = "Type '%s' inside structure '%s' is unknown!" % (element['type'], name)
				return False
			elementObj = DefVarTypeStructElement(element['name'], type)
			structObj.addElement(elementObj)
		self.add(structObj)
		return True

	def loadSingleStructPointer(self, name, value):
		if self.get(name) != None:
			return None
		if not value.endswith("*"):
			raise Exception("Structure type '%s' should be a pointer to something" % name)
		value = value[:-1]
		type = self.get(value)
		if type is None:
			return False
		self.add(DefVarTypePtr(name, type))
		return True





