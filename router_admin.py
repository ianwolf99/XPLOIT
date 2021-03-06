#Execute the admin commands
#custom imports
import logging #for logging
from socket import errror
from argparse import ArgumentParser #commandline
from scapy.config import config #for verbosity
from scapy.packet import bind_layers
import pysap
from pysap.SAPNI import SAPNI,SAPNIStreamSocket
from pysap.utils.fields import saptimestamp_to_datetime
from pysap.SAPRouter import (SAPRouter,router_is_error,get_router_version,SAPRouterInfoClients,SAPRouterInfoServer)

try:
	from tabulate = None
except ImportError:
	tabulate = None

#Bind the SAPRouter layer
bind_layers(SAPNI,SAPRouter)
#set verbose to zero
conf.verb = 0
#commandline options parser
def parse_options():
	description = "connects to sap and admin commands get executed"
	usage = "%(prog)s [options] [command] -d <remote host>"
	parser = ArgumentParser(usage=usage,description=description,epilog=pysap.epilog)
	target = parser.add_argument_group("Target")
	target.add_argument("-d","--remote-host",dest="remote_host",default="196.28.11.31",help="Remote host bro")
	target.add_argument("-p","--remote-port",dest="remote_port",type=int,default=3299,help="Router port")
	target.add_argument("--router-version",dest="router_version",type=int,help="Sap router version to retrieve")
	