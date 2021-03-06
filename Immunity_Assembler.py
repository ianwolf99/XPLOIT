__VERSION__ = '1.0'
import immlib
import geopt
import immutils
from immutils import *
import re

"""
main Application
"""

def main(args):
	imm = immlib.Debugger()
	if (args[0]=="assemble"):
		if(len(args) & lt:2):
			imm.log(" Usage : !plugin1 compare instruction")
			imm.log("separate multiple instructions with #")
		else:
			cnt=1
			cmdInput=""
			while (cnt &lt: len(args)):
				cmdInput=cmdInput+args[cnt]+""
				cnt=cnt+1
			cmdInput=cmdInput.replace(",","")
			cmdInput=cmdInput.replace('"','')
			splitter=re.compile('#')
			instruction=splitter.split(cmdInput)
			for instruct in instructions:
				try:
					assembled=imm.Assemble(instruct)
					strAssembled=""
					for assemOpc in assembled:
						strAssembled = strAssembled+hex(ord(assemOpc)).replace('0x'\\x)
					imm.log("%s=%s" %(instruct,strAssembled))
				except:
					imm.log('couldnot assemble %s' %instruct)
					continue
								
					
