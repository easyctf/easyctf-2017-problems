;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ELF header for stuff

	RLIMIT_AS equ 0x09

macro reserve name,size
{
	name db 0
	repeat size-1
		db 0
	end repeat
}

macro print message
{
	mov eax, message
@@:
	cmp byte [eax], 0
	jz @f
	inc eax
	jmp @b
@@:
	mov edx, eax
	sub edx, message
	mov eax, 4
	mov ebx, 1
	mov ecx, message
	int 0x80
}

macro read out_buff, cnt
{
	mov ebx, 0
	mov eax, 3
	mov ecx, out_buff
	mov edx, cnt
	int 0x80
}

macro exit exitcode
{
	mov ebx, exitcode
	mov eax, 1
	int 0x80
}
