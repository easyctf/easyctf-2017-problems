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

output_text db 'Assuming you got every challenge right here is the flag: %s', ENDL, 0

start:
	shl edx, 2
	sub edi, edx
	push edi
	mov eax, dword [ebx]
	lea ecx, [esi + output_text]
	push ecx
	call dword [eax]
	add esp, 8

	ret

resv_stuff 512-$
