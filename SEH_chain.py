import immlib
#used with Immunity Debugger
imm= immlib.Debugger

def main(args):
	if (args[0]=="sehchain"):
		sehchain=imm.getSehChain()
		sehtable=imm.createTable('SEH chain',['Address','Value'])
		for chainentry in sehchain:
			sehtable.add(0,("0x%08x"%(chainentry[0],("%08x"%(chainentry[1]))))
			

