#Author ianwolf99
import logging
from argparse import ArgumentParser
from socket import error as socketerror
from scapy.config import config
import pysap
import pysap.SAPRFC import SAPRFC
from pysap.utils.console import BaseConsole
from pysap SAPRouter import SAPRouterStreamSocket

conf.verb = 0

class SAPGWMonitorConsole(BaseConsole):

	intro = "SAP Gateway/RFC Monitor Console"
	connection = None
	connected = False
	clients = []

	def __init__(self, options):
		super(SAPGWMonitorConsole, self).__init__(options)
		self.runtimeoptions["clients"] = self.options.clients
		self.runtimeoptions["version"] = self.options.version

	#initialization
	def preloop(self):
		super(SAPGWMonitorConsole , self).preloop()
		self.do_connect(None)
		self.do_client_list(None)

	#SAP Gateway/RFC Monitor commands
	def do_connect(self, args):
	#intantiate a connection to the gateway service
	try:
		self.connection = SAPRouterStreamSocket.get_nisocket(self.options.remote_host,self.options.remote_port,self.options.route_string,base_cls=SAPRFC)

	except socketError as e:
		self.error("Error connecting with the Gateway service")
		self._error(str(e))
		return

	self._print("Attached to %s / %d" % (self.options.remote_host,self.options.remote_port))
	
	p = SAPRFC(version=int(self.runtimeoptions["version"]), req_type=1)

	self._debug("Sending check gateway packet")
	try:
		response = self.connection.send(p) 
	except socketError:
		self._error("Error connecting to the gateway monitor service")
	else:
		self.connected = True

	def do_disconnect(self, args):
	#Disconnects from the Gateway service 
		if not self.connected:
		self._error("You need to connect to the server first")
		return 			

		self.connection.close()
		self._print("Dettached fro %s %d.." % (self.options.remote_host,self.options.remote_port))
		self.connected = False

	def do_exit(self, args):
		if self.connected:
			self.do_disconnect(None)
		return super(SAPGWMonitorConsole, self).do_exit(args)
		
	def do_noop(self,args):
	#send a noop command to the gateway service 
		if not self.connected:
			self._error("You need to connect first")
			return
		p = SAPRFC(version=int(self.runtimeoptions["version"]),req_type=9,cmd=1)
		self.debug("Sending noop packet")
		response = self.connection.send(p)
	def do_client_list(self, args):
		#retrieve the list of connected clients
		if not self.connected:
			self._error("You need to connect first")
			return

	#command line options parser
def parse_options():

	description = "Implements SAP Gateway Monitor Program(gwmon)"

	usage = "%(prog)s [options ] -d <remote host>"

	parser = ArgumentParser(usage=usage ,description=description, epilog=pysap.epilog)

	target = parser.add_argument_group("Target")
	target.add_argument("-d","--remote-host",dest="remote_host",type=str help="Remote host")
	target.add_argument("-p","--remote-port",dest="remote_host",type=int,default=3300,help="Remote port[%(default)d]")
	target.add_argument("--route_string",dest="route_string",help="Route string for connecting through saprouter")
	target.add_argument("--version",dest="version",type=int ,default=3,help="version of the protocol to use [%(default)d]")

	misc = parser.add_argument_group("misc options")
	misc.add_argument("-v","--verbose",dest="verbose",action="store_true",help="Verbose output")
	misc.add_argument("-c","--client",dest="client",default="CE3",help="Client name[%(default)d]")
	misc.add_argument("--log-file",dest="logfile",metavar="FILE",help="Log file")
	misc.add_argument("--console-log",dest="cosolelog",metavar="FILE",help="Console log file")
	misc.add_argument("--script",dest="script",metavar="FILE",help="script to run")

	options = parser.parse_args()


		if not (options.remote_host or options.route_string):
			parser.error("Remote host or string is required")
			return options

def main():
	options = parse_options()

	if options.verbose:
		logging.basicConfig(level=logging.DEBUG)
	rfc_console = SAPGWMonitorConsole(options)
	
	try:
		if options.script:
			rfc_console.do_script(options.script)

		else:
			rfc_console.cmdloop()
	except KeyboardInterupt:
		print("Cancelled by user !")
		rfc_console.do_exit(None)

if __name__ == "__main__":
	main()

#Hacked by ianwolf	