int authenicate = 0;
char *packet = (char *)malloc(1000);

while (!authenicated){
	packetRead(packet);
	if(Authenicate(packet))
		authenicated = 1;
}
if(authenicated)
processPacket(packet);