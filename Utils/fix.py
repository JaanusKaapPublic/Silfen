import Syscalls
import CoreKernel

result = [""] * 0x2000

for name in CoreKernel.Data:
	oname = name
	if oname not in Syscalls.Data:
		oname = "Zw" + oname[2:]
	if oname not in Syscalls.Data:
		#print "%s was not found" % name
		CoreKernel.Data[name]['done'] = False
	else:
		CoreKernel.Data[name]['params'] = Syscalls.Data[oname]['params']
		CoreKernel.Data[name]['done'] = True
		
for name in CoreKernel.Data:
	code = CoreKernel.Data[name]['code']
	if not CoreKernel.Data[name]['done']:
		result[code] += "\t#TODO: Unknown function until now\n"
	if len(CoreKernel.Data[name]['params']) > 0 and CoreKernel.Data[name]['params'][0]['type'] == "?":
		result[code] += "\t#TODO: Unknown parameter types\n"
	result[code] += "\t'%s': {'code': 0x%X, 'retVal':'%s', 'lib': '%s', 'params':\n" % (name, CoreKernel.Data[name]['code'], CoreKernel.Data[name]['retVal'], CoreKernel.Data[name]['lib'])
	result[code] += "\t\t[\n"
	for param in CoreKernel.Data[name]['params']:
		result[code] += "\t\t\t{'name': '%s', 'type':'%s', 'in': %s, 'out': %s, 'optional': %s},\n" % (param['name'], param['type'], param['in'], param['out'], param['optional'])
	result[code] += "\t\t]},\n"
	
	
print "Data = {"
for code in result:
	if code != "":
		print code
print "}"
