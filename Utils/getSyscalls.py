from idautils import *
from idaapi import *
from idc import *

def createFunc(name, retType, code, params):
	print "\t'%s': {'code': 0x%X, 'retVal':'%s', 'lib': '%s', 'params':" % (name, code, retType, GetInputFile())
	print "\t\t["
	for param in params:
		if len(param.strip())>0:
			print "\t\t\t{'type':'%s', 'in': True, 'out': False, 'optional': False}," % param
	print "\t\t]},\n\n"

codeToName = {}

for funcea in Functions():
	functionName = GetFunctionName(funcea)
	if ((functionName.startswith("Nt") or functionName.startswith("Zw"))) and GetMnem(funcea) == "mov" and GetOpnd(funcea, 0) == "r10" and GetOpnd(funcea, 1) == "rcx"  and GetMnem(funcea+3) == "mov" and GetOpnd(funcea+3, 0) == "eax":
		code = GetOpnd(funcea + 3, 1)
		if len(code) > 1 and code[0] == '0':
			code = code[1:]
		if len(code) > 1 and code[-1] == 'h':
			code = code[0:-1]
		code = int(code, 16)
		outType = "NTSTATUS"
		
		funcLine = GuessType(funcea)
		funcLine = funcLine[funcLine.find('(')+1:funcLine.find(')')]
		parametersTmp = funcLine.split(", ")
		params = []
		for param in parametersTmp:
			param = param.split(" ")[0]
			if param == "int":
				param = "?"
			params.append(param)
			
		if code not in codeToName or (functionName.startswith("Nt") and not codeToName[code][0].startswith("Nt")):
			codeToName[code] = [functionName, outType, code, params]
			
exportNames = {}
for data in list(Entries()):
	exportNames[data[3]] =  True
			
for code in codeToName:
	if codeToName[code][0].startswith("Zw") and ("Nt" + codeToName[code][0][2:]) in exportNames:
		codeToName[code][0] = "Nt" + codeToName[code][0][2:]	

for code in codeToName:
	createFunc(codeToName[code][0], codeToName[code][1], codeToName[code][2], codeToName[code][3])
		
#print list(Entries())