format binary 
use32
include 'std.inc'

; On entrance to each shellcode segment the ebx register will be a vtable of std funcs
; printf
; puts
; scanf
; sin
; cos
; tan
; asin
; acos
; atan
; malloc
; free
; esi contains the base address of the shellcode segment
; edi contains the address of the part of the flag that this segment fills
; edx contains the number of the block

jmp start

startup_text db 'What did you say?',0

start:
	push edi

	lea ecx, [esi+startup_text]
	push ecx
	lea eax, [ebx + 0x4]
	mov eax, dword [eax]
	call dword [eax]
	pop ebp

	xor eax, eax
	push eax
	push eax
	mov eax, esp
	push eax

	lea eax, [ebx + 8]
	mov eax, dword [eax]
	lea ecx, [esi+scanf_text]
	push ecx
	call dword [eax]
	add esp, 8

	pop ecx
	pop eax
	pop edi

	mov dword [edi], ecx

	lea edx, [esi+to_match]

.check:
	movzx ecx, byte [edi]
	call check_char
	cmp eax, 0
	jz idiot

	inc edi
	inc edx
	cmp byte [edx], 0
	jnz .check

	ret

scanf_text db '%4[^',ENDL,']'

; ecx = input'd char
; edx = ptr to char to match
check_char:
	cmp ecx, CHAR_a ; 97
	jl fail
	cmp ecx, 126
	jge fail
	
	sub ecx, CHAR_a ; 97
	add ecx, esi
	lea ecx, [ecx + alphabet]
	movzx eax, byte [ecx]
	cmp byte [edx], al
	jnz fail

	mov eax, 1
	ret

idiot_text db 'Wrong...', 0

fail:
	mov eax, 0
	ret

to_match db 'xtnq', 0

idiot:
	lea ecx, [esi+idiot_text]
	push ecx
	lea eax, [ebx + 0x4]
	mov eax, dword [eax]
	call dword [eax]
	pop ebp
	dec esp
	ret

alphabet db 'hqxfbntvirwml{cap|z}sjeodygku', 0
;            abcdefghijklmnopqrstuvwxyz{|}
; flag is "cgfb"
resv_stuff 512-$
