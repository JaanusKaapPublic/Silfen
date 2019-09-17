import os
import subprocess
import time
from importlib import import_module
from MarkupGeneratorBinary import MarkupGeneratorBinary

class Fuzzer:
	setup = None
	syscallsPerIteration = 64
	maxIterationDuration = 12
	iterationsToDetectHanggFuncs = 1024
	showInfo = True


	def __init__(self, setup):
		self.setup = setup

	def loadData(self, subDir):
		self.setup.types.loadSimpleTypes(import_module(subDir + '.Types').Data)
		self.setup.types.loadEnums(import_module(subDir + '.Enums').Data)
		self.setup.types.loadStructures(import_module(subDir + '.Structs').Data)
		self.setup.functions.load(import_module(subDir + '.Syscalls').Data)

	def start(self, iterations = None):
		iterationTime = self.maxIterationDuration * 4;
		count = 0

		while iterations is None or count < iterations:
			self.setup.variables.clear()
			codeblocks = []
			for x in xrange(self.syscallsPerIteration):
				func = self.setup.functions.get()
				codeblocks += self.setup.logicFuncGenerator.callFunc(func)
			c = MarkupGeneratorBinary()
			c.addCodes(codeblocks)
			f = open("code.bin", "wb")
			f.write(c.generate())
			f.flush()
			os.fsync(f)
			f.close()
			p = None
			if count < self.iterationsToDetectHanggFuncs:
				p = subprocess.Popen(["CodeExecutor.exe", "code.bin", "funcs.txt"])
			else:
				p = subprocess.Popen(["CodeExecutor.exe", "code.bin"])


			for x in xrange(iterationTime):
				time.sleep(0.25)
				poll = p.poll()
				if p.poll() is not None:
					break
				else:
					if x == iterationTime - 1:
						p.kill()
						if count < self.iterationsToDetectHanggFuncs:
							f = open("funcs.txt", "r")
							failedFunc = f.readlines()
							f.close()
							failedFunc = failedFunc[len(failedFunc) - 1].strip()
							self.setup.functions.remove(failedFunc)
							if self.showInfo:
								print "Function \"%s\" stopped execution and was removed from fuzzing list!" % failedFunc
			count += 1
			if self.showInfo:
				if count % 10 == 0:
					print "Done %d iterations" % count


