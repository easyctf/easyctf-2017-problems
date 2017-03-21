# Generates random flag thing
import random

flag_temp = '{%s}'

def gen_flag(len):
	val = ''
	for x in range(len):
		val += random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
	return flag_temp % val

print(gen_flag((4*3)-2))