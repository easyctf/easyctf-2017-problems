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

start:
	push edx
	push edi
	push esi

	mov eax, dword [ebx]
	lea ecx, [esi + base_txt]
	push ecx
	call dword [eax]
	add esp, 4

	xor eax, eax
	push eax
	mov eax, esp
	push eax

	lea eax, [ebx + 8]
	mov eax, dword [eax]
	lea ecx, [esi+scanf_txt]
	push ecx
	call dword [eax]
	add esp, 8

	; inputt'd float is now on top of the stack
	pop eax
	mov dword [esi+temp_val], eax

	sub esp, 8
	cvtss2sd xmm0, dword [esi+temp_val]
	movsd qword [esp], xmm0

	; call cos
	lea eax, [ebx + 0x10]
	mov eax, dword [eax]
	call dword [eax]

	fstp qword [esp]
	movsd xmm0, qword [esp]
	add esp, 8
	cvtss2sd xmm1, dword [esi+c_val]
	mulsd xmm0, xmm1
	push ebp
	push ebp
	movsd qword [esp], xmm0

	; call atan
	lea eax, [ebx + 0x20]
	mov eax, dword [eax]
	call dword [eax]

	fstp qword [esp]
	movsd xmm0, qword [esp]
	pop eax
	cvtss2sd xmm1, dword [esi+b_val]
	pop ecx
	mulsd xmm0, xmm1
	push esp
	push ebp
	movsd qword [esp], xmm0

	; call sin
	lea eax, [ebx + 0xc]
	mov eax, dword [eax]
	call dword [eax]

	fstp qword [esp]
	cvtss2sd xmm1, dword [esi+a_val]
	movsd xmm0, qword [esp]
	mulsd xmm0, xmm1

	movsd qword [esp], xmm0
	cvtsd2ss xmm0, qword [esp]
	pop eax
	movss dword [esp], xmm0
	pop eax

	pop esi
	push esi

	cmp eax, dword [esi+final_val]
	jnz trash
	lea ecx, [esi+right_txt]
	jmp past_trash
trash:
	lea ecx, [esi+wrong_txt]
	; Make this so it crashes badly
	inc esp
past_trash:
	push ecx
	lea eax, [ebx + 0x4]
	mov eax, dword [eax]
	call dword [eax]
	pop ebp

	pop esi
	pop edi
	pop edx

	mov eax, dword [esi+temp_val]
	; 0x336a687b = little endian of '{hj3'
	; 0x336a687b ^ 0x3fab396d which is the value of the correct input 1.33769
	; is equal to 0x5e9c6316
	xor eax, 0xcc15116
	mov dword [edi], eax
	xor eax, eax
	mov dword [esi+temp_val], eax

	retn

b_val dd 0x4039999a
base_txt db 'Please enter the best number, round to 6 significant figures.', ENDL, 0
a_val dd 0x40d00000
scanf_txt db '%f', 0
final_val dd 0xc092e6a0
right_txt db 'You got it!', 0
c_val dd 0xbf99999a
wrong_txt db 'You dumb.', 0
temp_val dd 0

resv_stuff 512-$
