int main(int argc, char**argv)
{
	.....
	buf1 = (char *)malloc(BUFSIZE1);
	free(buf1);
	buf2 = (char *)malloc(BUFSIZE2);
	strncpy(buf2,argv[1],BUFSIZE2-1);
	free(buf1);
	free(buf2);
}