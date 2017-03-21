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

; 2 - 3,5 - '-'
; 3 - 5,7 - '_'
; 5 - 7,11 - 'e'
; 7 - 11,13 - 'x'
; 11 - 13,17 - 'z'
; 13 - 17,19 - '}'
; 17 - 19,23 - '}'
; 19 - 23,29 - '}'

; 2 * 7 * 11 * 17 = 0x74e
; answer "0 4 8 13"
; flag -ez}

start:
	push edi

	lea eax, [ebx + 0x4]
	lea ecx, [esi+startup_txt]
	mov eax, dword [eax]
	push ecx
	call dword [eax]
	pop ebp

	pop edi

	lea ebp, [esi+one]
.lp:
	call process
	cmp byte [ebp+8], 125
	jnz .lp

	mov eax, dword [esi+super_val]
	cmp eax, 0x74e
	jnz .bad
	jmp .finish

.bad:
	lea eax, [ebx + 0x4]
	lea ecx, [esi+wrong_txt]
	mov eax, dword [eax]
	push ecx
	call dword [eax]
	pop ebp
	inc esp

.finish:
	ret

two:
	dd three,five
	db '-',2

startup_txt db 'Numberz?', 0

three:
	dd five,seven
	db '_',3

fmt_txt db '%u',0

five:
	dd seven,eleven
	db 'e',5

; ebp = current node
process:
	push ebp
	push ebp
	mov eax, esp
	push eax

	lea eax, [ebx + 8]
	lea ecx, [esi+fmt_txt]
	mov eax, dword [eax]
	push ecx
	call dword [eax]
	pop ebp
	pop eax
	pop ecx
	pop ebp

	movzx eax, byte [ebp+9]

	cmp eax, ecx
	jle above_handler
	jmp below_handler

seven:
	dd eleven,thirteen
	db 'x',7

above_handler:
	mov ecx, dword [ebp+4]
	lea ebp, [esi+ecx]
	jmp add_next_char

eleven:
	dd thirteen,seventeen
	db 'z',11

mul_handler:
	movzx eax, byte [ebp+9]
	mov edx, dword [esi+super_val]
	mul edx
	mov dword [esi+super_val], eax
	ret

thirteen:
	dd seventeen, nineteen
	db '}',13

below_handler:
	mov ecx, dword [ebp]
	lea ebp, [esi+ecx]
	jmp add_next_char

seventeen:
	dd nineteen, twentythree
	db '}',17

add_next_char:
	movzx eax, byte [ebp+8]
	mov byte [edi], al
	inc edi
	jmp mul_handler

nineteen:
	dd twentythree, twentynine
	db '}',19

super_val dd 1

twentythree:
	dd 0, 0
	db ':',23

twentynine:
	dd 0, 0
	db ')',29

wrong_txt db 'Nope!',0

one:
	dd two, three
	db 0,1

resv_stuff 512-$
