void getComment(unsigned int len, char *src)
{
	unsigned int size;
	size = len-2;
	char *comment = (char *)malloc(size+1);
	memcpy(comment,src,size);
	return;
}