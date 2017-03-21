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

	push edi

	lea ecx, [esi+pattern_text]
	push ecx
	lea eax, [ebx + 0x4]
	mov eax, dword [eax]
	call dword [eax]
	pop ebp

	mov ecx, 0
printLoop:
	push ecx
	call adv_fib
	push eax
	lea ecx, [esi + format_text]
	mov eax, dword [ebx]
	push ecx
	call dword [eax]
	pop ecx
	pop ebp
	pop ecx
	inc ecx
	cmp ecx, 6
	jnz printLoop

	lea ecx, [esi+empty_text]
	lea eax, [ebx + 0x4]
	mov eax, dword [eax]
	push ecx
	call dword [eax]
	pop ebp


	lea ecx, [esi+inputVal]
	push ecx
	lea eax, [ebx + 8]
	mov eax, dword [eax]
	lea ecx, [esi+unsignFmt]
	push ecx
	call dword [eax]
	add esp, 8

	mov ecx, dword [esi+inputVal]
	pop edi
	; 797691075 is the answer
	; (struct.unpack('<I', b'-0p9')[0] ^ 0x2f8bccc3)
	; This part of the flag is -0p9 ^ the 36th value in the pattern.
	xor ecx, 0x16fbfcee
	mov dword [edi], ecx

	push edi
	lea ecx, [esi+pray_text]
	mov eax, dword [ebx]
	push ecx
	call dword [eax]
	pop ecx
	pop edi

	mov dword [esi+inputVal], 0

	ret

pattern_text db 'What is the 36th number (index 35) in the following sequence?', 0
format_text db '%d ', 0

; ecx = arg
adv_fib:
	cmp ecx, 2
	jg do_more
	mov eax, 1
	ret

unsignFmt db '%u', 0
inputVal dd 0

do_more:
	push edx
	dec ecx
	push ecx
	call adv_fib
	pop ecx
	push eax
	dec ecx
	push ecx
	call adv_fib
	pop ecx
	push eax
	dec ecx
	call adv_fib
	pop edx
	add eax, edx
	pop edx
	add eax, edx
	pop edx
	ret

empty_text db 0
pray_text db 'Hope you got it right! Result: [%s]', ENDL, 0

resv_stuff 512-$
