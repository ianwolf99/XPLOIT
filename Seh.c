#include <stdio.h>
#include <windows.h>
int main(int argc, char *argv[])
{
char temp[20];
__try
{
strcpy(temp, argv[1]);
printf("\nPress any key to continue . . .\n");
getch();
}
__except(EXCEPTION_EXECUTE_HANDLER)
{
printf("\nException code: %.8x\n", GetExceptionCode());
}
printf("\nArgument entered is: %s\n\n", argv[1]);
return 0;
}

offset
EB069090...jump 6 bytes ahead
pop pop ret
shellcode
extra junk