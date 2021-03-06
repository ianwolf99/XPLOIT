#Ms_dump python file
import logging
from argparse import ArgumentParser
from scapy.config import conf
import pysap
from pysap.SAPRouter import SAPRoutedStreamSocket
from pysap.SAPMS import SAPMS,ms_dump_command_values,ms_opcode_error_values,msdomain_values_inv

conf.verb = 0
#command line options
def parse_options():
	description = 'Gather intel from SAP Netweaver Application server with dump command'
	usage = "%(prog)s [options] -d <remote host>"
	parser = ArgumentParser(usage=usage,description=description,epilog=pysap.epilog)
	
	target = parser.add_argument_group("Target")
	target.add_argument("-d","--remote-host",dest="remote_host",help="Remote host")
	target.add_argument("-p","--remote-port",dest="remote_port",default=3900,help="Remote Host")
	target.add_argument("--route-string",dest="route_string",help="Route string for connecting ")
	target.add_argument("--domain",dest="domain",default="ABAP",help="Domain to connect to (ABAP,J2EE or JSTARTUP
		
	misc = parser.add_argument_group("misc options")
	misc.add_argument("-v","--verbose",dest="verbose",action="store true",help="Verbose output")
	misc.add_argument("-c","--client",dest="client",default="pysaps dumper")
	
	options = parser.parse_args()
	
	if not (options.remote_host or options.route_string):
		parser.error("Remote host or route string is required")
	if options.domain not in ms_domain_values_inv():
		parser.error("Invalid domain specified")
		
	return options
	
# main function
def main():
	options = parse_options()
	
	if options.verbose:
		logging.basicConfig(level=logging.DEBUG)
	
	domain = ms_domain_values_inv[options.domain]
	
	#initiate the connection
	conn = SAPRoutedSteamSocket.get_nisocket(options.remote_host,options.remote_port,options.route_string,base_cls=SAPMS)
	
	print("[*] connected  to message server %s:%d" % (options.remote_host,options.remote_port))
	
	client_string = options.client
	
	#send MS_LOGIN_2 packet
	p = SAPMS(flag=0x00,iflag=0x08,domain=domain,toname=client_string,fromname=client_string)
	
	print("[*] Sending dump info",ms_dump_command_values[i])
	response = conn.sr(p)[SAPMS]
	
	if response.opcode_error !=0:
		print("Error:",ms_opcode_error_values[response.opcode_error]
	
	print("[*] Sending login packet:")
	response = conn.sr(p)[SAPMS]
	
	print("[*] Login OK,Server string:%s" % response.fromname)
	server_string = response.fromname
	
	#Send a dump info packet for each posible dump
	for i in ms_dump_command_values.keys():

		
		#Skip MS_DUMP_MSADM and MS_DUMP _COUNTER commands as the info
		#is included in other dump commands
		
		if i in [1,12]:
			continue
			
		p = SAPMS(flag=0x02,iflag=0X01,domain=domain,toname=server_string,fromname=client_string,opcode=0xie,dump_dest=0x02,dump_command=i)						
		
		print("[*] Sending dump info,ms_dump_command_values[i])
		response = conn.sr(p)[SAPMS]
		
		if response.opcode_error != 0:
			print("Error:",ms_opcode_error_values[response.opcode_error])
		print(response.opcode_value)
			
if __name__ == "__main__":
	main()
