int func(char *name,long cbBuf){
	unsigned short bufsize = cbBuf;
	char *buf=(char *)malloc(bufSize);
	if(buf){
		memcpy(buf, name, cbBuf);
		....
		free(buf);
		return 0;
	} 
	return 1;
}