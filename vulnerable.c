#include "stdio.h"

int int main(int argc, char const *argv[])
{
	/* code */
	char little_array[512];

	if (argc > 1)
	{
		/* code */
		strcpy(little_array,argv[1]); 
	}
	return 0;
}