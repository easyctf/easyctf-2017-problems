;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Standard Includes of my
; code
include 'char.inc'

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; File descriptor macros
	STDIN	equ 0
	STDOUT 	equ 1
	STDERR	equ 2
;;;;;;;;;;;;;;;;;;;;;;;;;;;


; Standard prologue of a function
macro prologue
{
	push ebp
	mov ebp, esp
}

; Standard epilogue of a function
macro epilogue
{
	mov esp, ebp
	pop ebp
}

; Allocates space on the stack for something
macro local_alloc size
{
	sub esp,size
}