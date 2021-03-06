import logging 
from argparse iport ArgumentParser
from socket import error as SocketError
from scapy.config import conf
from scapy.packet import bind_layers
import pysap
from pysap.SAPRouter import (SAPRouter,SAPROuteException,SAPRouterNativeProxy,SAPRouterNativeRouteHandler,ROUTE_TALK_MODE_NI_RAW_IO,ROUTER_TALK_MODE_NI_MSG_IO)

#bind the SAPRouter layer
bind_layes(SAPNI,SAPRouter)
#set the verbosity to zero
conf.verb = 0

#command line parser options
def parse_options():
	description = "Routes a connection thru SAP Router service"
	usage = "%(prog)s [options] -d <remote host>"
	parser = ArgumentParser(usage=usage ,description=description,epilog=pysap.epilog)
	target = parser.add_argument_group("Target")
	target.add_argument("-d","--remote-host",dest="remote_host",default="196.28.11.31",help="Remote host")
	target.add_argument("-p","--remote-port",dest="remote_port",type=int,default=3299,help="Remote port")
	target.add_argument("-t","--target-host",dest="target_host",help="Target to connect")
	target.add_argument("-r","--target-port",dest="target_port",type=int,help="Target port to connect")
	target.add_argument("-p","--target-pass",dest="target_pass",help="Target password")
	target.add_argument("-a","--local-host",dest="local_host",type=str,help="local host to listen")
	target.add_argument("-l","--local-port","local_port",type=int,help="Local port to listen")
	target.add_argument("--talk-mode",dest="talk_mode",default="raw",help="Talk mode(raw or ni")

	misc = parser.add_argument_group("misc options")
	misc.add_argument("-v","--verbose",dest="verbose",action="store_true",help="Verbose output")

	options = parser.parse_args()

	if not options.remote_host:
		parser.error("Remote host is required")
	if not options.target_host:
		parser.serror("Target host is required")
	if not options.target_port:
		parser.error("Target port to connect")
	options.talk_mode = options.talk_mode.lower()
	if options.talk_mode not in ["raw","ni"]:
		parser.error("invalid talk mode")

	if not options.local_port:
		print("[*]No local port specified,using target port%d" % options.target_port)
		options.local_port = options.target_port
	return options
	
#main function
def main():
	options = parse_options()

	level = logging.INFO
	if options.verbose:
		level = logging.DEBUG
	logging.basicConfig(level=level,format="%(message)s")
	logging.info("[*]Setting a proxy between %s:%d and remote SAP Router %s:%d(talk mode %" % (options.local_host,options.local_port,options.remote_host,options.remote_port,options.talk_mode))
	
	options.talk_mode = {"raw": ROUTER_TALK_MODE_NI_RAW_IO,"ni":ROUTER_TALK_MODE_NI_MSG_IO}[options.talk_mode]
	proxy = SAPRouterNativeProxy(options.local_host,options.local_port,options.remote_host,options.remote_port,SAPRouterNativeRouteHandler,target_address=options.target_host,target_port=options.target_port,target_pass=options.target_pass,talk_mode=options.talk_mode,keep_alive=False,options=options)
	
	try:
		while True:
			try:
				proxy.handle_connection():
			except SocketError as e:
				logging.error("[*] Socket error %s" % e)

	except KeyboardInterupt:
		logging.error("[*] Cancelled by the user ! ")
	except SAPROuteException as e:
		logging.error("[*] Closing routing do to error %s" % e)

if __name__ = "__main__":
	main()			



