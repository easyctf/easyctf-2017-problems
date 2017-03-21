import subprocess
# Build a self-modifying thinga-ma-jig

def run_command(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
      stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdoutput = proc.stdout.read() + proc.stderr.read()
    return stdoutput

def build_bin(name):
	print(run_command('fasm %s.asm' % name))

def create_xor_block(last_shellcode_block, next_shellcode_block):
	block = bytearray(b'')
	for x in range(0, len(last_shellcode_block)): # each shellcode block should be 512 bytes
		block.append((last_shellcode_block[x]) ^ (next_shellcode_block[x]))
	return bytes(block)

def get_shellcode_block(name):
	build_bin(name)
	f = open('%s.bin' % name, 'rb')
	out = f.read()
	f.close()
	return out

shellcode_files = ['first', 'second', 'third', 'fourth', 'last']
shellcode_blocks = [get_shellcode_block('base_block')]
morpher_file = 'morpher'
morpher_template = 'morpher.template.asm'

xor_blocks = []
xor_block_files = []

def build_shellcode_files():
	for x in shellcode_files:
		shellcode_blocks.append(get_shellcode_block(x))

def gen_xor_blocks():
	for x in range(0, len(shellcode_files)):
		xor_block = create_xor_block(shellcode_blocks[x], shellcode_blocks[x+1])
		xor_blocks.append(xor_block)
		f = open('b%d.bin' % x, 'wb')
		f.write(xor_block)
		f.close()
		xor_block_files.append('b%d.bin' % x)


def create_morpher_file():
	_mrph = 'file \'base_block.bin\'\n'
	_data = ''
	_block_list = ''

	for x in xor_block_files:
		_data += '%s: file \'%s\'\n' % (x, x)
		_block_list += '%s, ' % x

	_data += 'block_ptrs dd %s0' % _block_list

	f = open(morpher_template, 'rb')
	template = f.read().decode('utf-8')
	f.close()
	result = template % (_mrph, _data)
	f = open('%s.asm' % morpher_file, 'wb')
	f.write(result.encode('utf-8'))
	f.close()


# The morpher has 3 sections, modifiable code, static code (morphing), data
# Modifiable code will be where each shellcode segment is done
# Static code has the morpher that sets up each shellcode segment
# Data has the XOR block pointers and indicies for the ones to use in order
# Begins by the morpher creating the first shellcode block, setting it up, then running it
# continues until the final block that will print the flag
# Kinda like a binary bomb but in one binary

# On entrance to each shellcode segment the ebx register will be a vtable of std funcs
# printf
# puts
# scanf
# esi contains the base address of the shellcode segment
# edi contains the address of the part of the flag that this segment fills
# edx contains the number of the block

build_shellcode_files()
gen_xor_blocks()
create_morpher_file()
build_bin(morpher_file)

#print(create_xor_block(b'123', b'321'))
#print(get_shellcode_block('shellcode'))
