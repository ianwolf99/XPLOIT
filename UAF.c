int main(int argc, char**argv){
	char *buf1;
	char *buf2;
	char *buf3;

	buf1 = (char *)malloc(BUFSIZE1);
	free(buf1);

	buf2 = (char *)malloc(BUFSIZE2);
	buf3 = (char *)malloc(BUFSIZE2);
	strncpy(buf1,argv[1],BUFSIZE1-1); /*Vulnerability lie here and other uf1 and buf2 will be overwritten including metadata*/
	....
}