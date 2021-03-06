import logging
import argparse import ArgumentParser
from scapy.config import config
from scapy.packet import bind_layers
import pysap
from pysap.SAPNI import SAPNIStreamSocket,SAPNI
from pysap.SAPRouter import (SAPRouterRouteHop,get_router_version,SAPRoutedStreamSocket,SAPRouteException,SAPRouter,ROUTER_TALK_MODE_NI_RAW_IO)

try:
	import netaddr
except ImportError:
	print("[-] netaddr library not found,running without network range parsing support")
	netaddr = None

#Bind the SAPRouter layer
bind_layers(SAPNI,SAPRouter)
#commandline parser
def parse_options():
	description = "perform scan via saprouter"
	usage = "%(prog)s [options] -d <remote host>"
	parser = ArgumentParser(usage=usage,description=description,epilog=pysap.epilog)
	target = parser.add_argument_group("target")
	target.add_argument("-d","--remote-host",dest="remote_host",default="196.168.50.46",help="Remote host [%(default)d]")
	target.add_argument("-p","--remote-port",dest="remote_port",type=int,default=3299,help="Remote port[%(default)d]")
	target.add_argument("-t","--target-hosts",dest="target_hosts",help="Targets host to scan")
	target.add_argument("-r","--target-ports",dest="target_ports",help="Target_ports to scan")
	target.add_argument("--router-version",dest="router_version",type=int,help="Router_version")
	target.add_argument("--talk-mode",dest="talk_mode",default=raw,help="Talk mode to use when requesting route(raw or ni [%(default)d]")
	
	misc = parser.add_argument_group("misc options")
	misc.add_argument("-v","--verbose",dest="verbose",action="store_true",help="verbose output")

	options = parser.parser_args()

	if not options.remote_host:
		parser.error("Remote host required")
	if not options.target_hosts:
		parser.error("target hosts required")
	if not options.target_ports:
		parser.error("target ports required")
	options.talk_mode = options.talk_mode.lower()
	if options.talk_mode not in ["raw","ni"]:
		parser.error("Invalid talk mode")

	return options
	
def parse_target_ports(target_hosts,target_ports):
	for port in parse_target_ports(target_ports):
		for host in target_hosts.split(','):
			if netaddr:
				if netaddr.valid_nmap_range(host):
					for ip in netaddr.iter_nmap_range(host):
						yield (ip,port)

				else:
					for ip in netaddr.iter_unique_ips(host):
						yield (ip,port)
			else:
				yield (host,port)

def route_test(rhost,rport,thost,tport,talkmode,router_version):

	logging.info("[*] Routing connections to %s:%s" % (thost,tport))
	#Build the route to the target host passing via the saprouter
	route = [SAPRouterRouteHop(hostname=rhost,port=rport),SAPRouterRouteHop(hostname=thost,port=tport)]
	#try to connect to target host using the routed stream socket
	try:
		conn = SAPRoutedStreamSocket.get_nisocket(route=route,talk_mode=talk_mode,router_version)
		conn.close()
		status = 'open'

	#If an SAPRouterException is raised ,the route was denied or an error
	#Occurred with SAP router
	except SAPRouteException:
		status = 'denied'


	#Another error occurred on the server(eg timeout),mark the atrget as error
	except Exception:
		status = 'error'

	return status
#main function
def main():
	options = parse_options()

	level = logging.INFO 
	if options.verbose:
		level = logging.DEBUG
	logging.basicConfig(level=level,format = '%(messages)s')
	logging.info("[*]Connecting to SAP Router %s:%d (talk mode %s)"(options.remote_host,options.remote_port,options.talk_mode))

	#Retrieve the router version used by the server if not specified
	if options.router_version is None:
		conn = SAPNIStreamSocket.get_nisocket(options.remote_host,options.remote_port,keep_alive=False)
		options.router_version = get_router_version(conn)
		conn.close()
	logging.info("[*] Using SAP Router Version %d" % options.router_version)
	options.talk_mode = {"raw":ROUTER_TALK_MODE_NI_RAW_IO , "ni":ROUTER_TALK_MODE_NI_MSG_IO}[options.talk_mode]

	results = []
	for (host,port) in parse_target_hosts(options.target_hosts,options.target_ports):
		status = route_test(options.remote_host,options_port,host,port,options.talk_node,options.router_version)
		if options.verbose:
			logging.info("[*] status of %s:%s:%s" % (host,port,status))
		if status == "open":
			results.append((host,port))

	logging.info("[*] Host?ports found open:")
	for (host,port)	in results:
		logging.info("\thost: %s\tport:%s" %(host,port))
		
if __name__ == "__main__":
	main()
