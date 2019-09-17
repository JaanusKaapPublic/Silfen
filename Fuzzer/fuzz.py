import os
from ManagerTypes import ManagerTypes
from ManagerFunctions import ManagerFunctions
from ManagerVariables import ManagerVariables
from LogicVarGenerator import LogicVarGenerator
from LogicFuncGenerator import LogicFuncGenerator
from logicHelperGenerator import logicHelperGenerator
from FuzzSetupManager import FuzzSetupManager
from Fuzzer import Fuzzer

setup = FuzzSetupManager()
managerTypes = ManagerTypes(setup).init()
managerFunctions = ManagerFunctions(setup)
managerVariables = ManagerVariables(setup)
logicVarGen = LogicVarGenerator(setup)
logicFuncGen = LogicFuncGenerator(setup)
logicHelperGen = logicHelperGenerator(setup)

fuzzer = Fuzzer(setup)
fuzzer.loadData("Win10Core")
fuzzer.loadData("Win10Win32k")
if not os.path.isfile("code.bin"):
	fuzzer.start()