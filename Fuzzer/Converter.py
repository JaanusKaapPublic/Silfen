from MarkupGeneratorBinary import *
from MarkupGeneratorC import *
import sys

if len(sys.argv) != 3:
	print "Correct syntax is: %s {input file} {output file}" % sys.argv[0]
	exit(1)

fin = sys.argv[1]
fout = sys.argv[2]

genBin = MarkupGeneratorBinary()
code = genBin.parse(open(fin, "rb").read())

genC = MarkupGeneratorC()
genC.addCodes(code)
open(fout, "w").write(genC.generate())




