global _start:

text.section

_start:
	MOV EBP,ESP
	PUSH 20657865
	PUSH 2E646D63
	LEA EAX,DWORD PTR SS:[EBP-8]
	PUSH EAX
	MOV EAX,kernel32.WinExec
	CALL EAX