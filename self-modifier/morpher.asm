format PE console
entry start
include 'C:\\Projects/asm/INCLUDE/win32a.inc'
include 'C:\\Projects/asm/std.inc'

section '.mrph' code readable executable writeable
mrph:

file 'base_block.bin'


section '.stat' code readable executable

data import
    library msvcrt, 'msvcrt.dll'
    import msvcrt, \
        printf , 'printf', \
        puts ,  'puts', \
        scanf , 'scanf', \
        sin , 'sin', \
        cos , 'cos', \
        tan , 'tan', \
        asin , 'asin', \
        acos , 'acos', \
        atan , 'atan', \
        malloc , 'malloc', \
        free , 'free', \
        getchar , 'getchar'
end data

do_morph:
	push ebp
	mov eax, 1
	mov edx, dword [num_block]
	lea ecx, [block_ptrs + 4*edx]
	mov ecx, dword [ecx]
	
	cmp ecx, 0 ; If the block ptr is null return
	jz .finish

	inc edx
	mov dword [num_block], edx
	lea edx, [ecx+512]
	mov edi, mrph

.mod:
	cmp ecx, edx
	jz .finish
	movzx eax, byte [ecx]
	movzx ebp, byte [edi]
	xor eax, ebp
	mov byte [edi], al 
	inc edi
	inc ecx
	xor eax, eax
	jmp .mod

.finish:
	pop ebp
	ret

; No args, flushes input.
flush_inp:
	call [getchar]
	cmp eax, -1
	jz .finish
	cmp eax, ENDL
	jnz flush_inp
.finish:
	ret

; On entrance to each shellcode segment the ebx register will be a vtable of std funcs
; esi contains the base address of the shellcode segment
; edi contains the address of the part of the flag that this segment fills
; edx contains the number of the block
run_morphed:
	mov esi, mrph
	mov edx, dword [num_block]
	dec edx
	lea edi, [flag + 4*edx]
	mov ebx, func_vtable
	call mrph
	ret

start:
	call do_morph
	cmp eax, 0
	jnz .finish
	call run_morphed
	call flush_inp
	jmp start

.finish:
	ret

section '.dat' data readable writeable

num_block dd 0

func_vtable dd printf, puts, scanf, sin, cos, tan, asin, acos, atan, malloc, free, 0

flag db 64 dup (0)

b0.bin: file 'b0.bin'
b1.bin: file 'b1.bin'
b2.bin: file 'b2.bin'
b3.bin: file 'b3.bin'
b4.bin: file 'b4.bin'
block_ptrs dd b0.bin, b1.bin, b2.bin, b3.bin, b4.bin, 0
