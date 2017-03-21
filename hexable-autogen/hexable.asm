format ELF executable 3
entry start

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Buffer macros
	BUFF_SIZE equ 32
;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Includes of macros
include 'elf.inc'
include 'char.inc'
;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Code
segment executable writeable readable
put:
	print ecx
	ret

start:
	mov ecx, msg
	call put
	exit 0
reserve no_code,20
;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Data
segment readable writeable
msg db 'Can you find the flag?',ENDL,0
flag db 'easyctf{abcdef__123456}'
reserve temp,1
;;;;;;;;;;;;;;;;;;;;;;;;;;;
