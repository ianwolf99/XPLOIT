#include "stdio.h"

unsigned long find_start(void)
{
	__asm__("mov, %esp,  %eax");

}

int int main()
{
	/* code */
	printf("%s\n", find_start());
	return 0;
}