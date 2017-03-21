from cStringIO import StringIO
from PIL import Image, ImageDraw
from math import ceil, sqrt

ALTCONST = sqrt(3) / 2.0
ISIZE = 784.0
IMARGIN = 22.0

def empty_hex(size):
	c = 0
	points = []
	for i in range(2, size * 2 + 2, 2):
		points.append([0] * i)
	middle = []
	for i in range(size * 2 - 1):
		row = [0] * (size * 2)
		middle.append(row)
	epoints = list(row[:] for row in points[::-1])
	return points + middle + epoints

def intify(points):
	return map(lambda c: (int(c[0]), int(c[1])), points)

def draw_triangle(im, points, cell, size):
	draw = ImageDraw.Draw(im)
	# draw.polygon(points, outline=(0, 0, 0))
	if cell:
		draw.polygon(intify(points), fill=(0, 0, 0))
	return im

def getsection(i, size):
	return 0 if i <= size - 1 else (1 if i < 3 * size - 1 else 2)

def getspace(size):
	return max(0, sum(len(filter(lambda a: a == 0, b)) for b in empty_hex(size)) - 2)

def generate_image(string, debug=False):
	size = 0
	binstring = bin(int(string.encode("hex"), 16)).strip("0b")
	while size < 2 or getspace(size + 1) - 80 < len(binstring):
		size += 1
	n = getspace(size)
	# print size, len(binstring)
	if debug: print "SIZE", size, " n =", n
	im = Image.new("RGB", (int(ISIZE), int(ISIZE)), "white")
	pattern = empty_hex(size)
	# print len(binstring)
	# print sum(len(i) for i in pattern)
	pattern[0][len(string) % 2] = 1
	curr = (1, 1 + len(string) % 2, 3 - len(string) % 2)
	# 0 1
	# 3 2
	for c in range(n): # range(len(binstring)):
		i, j, d = curr
		row = pattern[i]
		if c < len(binstring):
			b = int(binstring[c])
			pattern[i][j] = b
		if c % 2 == 0:
			pattern[i][j] ^= 1

		section = getsection(i, size)
		leftfacing = [j % 2 == 0, j % 2 != (i - size) % 2, j % 2 == 0][section]
		if debug: print "c =", c, ", i =", i, ", j =", j, ", d =", d, ", s =", section, ", l =", leftfacing
		if section == 0:
			if getsection(i + 1, size) == 0:
				if leftfacing:
					if d == 0:
						if j == 0:
							curr = i + 1, j, (d + 2) % 4
						else:
							curr = i - 1, j - 1, d
					elif d == 1 or d == 2:
						curr = i, j + 1, d
					elif d == 3:
						curr = i + 1, j + 1, d
				else:
					if d == 0:
						curr = i, j - 1, d
					elif d == 1:
						if j == len(row) - 1:
							curr = i + 1, j + 2, (d + 2) % 4
						else:
							curr = i - 1, j - 1, d
					elif d == 2:
						curr = i + 1, j + 1, d
					elif d == 3:
						curr = i, j - 1, d
			elif getsection(i + 1, size) == 1:
				if leftfacing:
					if d == 0:
						if j == 0:
							curr = i + 1, j, (d + 2) % 4
						else:
							curr = i - 1, j - 1, d
					elif d == 1 or d == 2:
						curr = i, j + 1, d
					elif d == 3:
						curr = i + 1, j, d
				else:
					if d == 0:
						curr = i, j - 1, d
					elif d == 1:
						if j == len(row) - 1:
							curr = i + 1, j, (d + 2) % 4
						else:
							curr = i - 1, j - 1, d
					elif d == 2:
						curr = i + 1, j, d
					elif d == 3:
						curr = i, j - 1, d
		elif section == 1:
			if getsection(i - 1, size) == 0:
				if leftfacing:
					if j == len(row) - 1:
						if d == 1:
							curr = i + 2, j, (d + 2) % 4
						elif d == 2:
							curr = i + 2, j, (d + 2) % 4
						elif d == 3:
							curr = i + 1, j, d
					else:
						if d == 0:
							curr = i - 1, j, d
						elif d == 1 or d == 2:
							curr = i, j + 1, d
						elif d == 3:
							curr = i + 1, j, d
				else:
					if j == 0:
						if d == 0:
							curr = i + 2, j, (d + 2) % 4
						elif d == 2:
							curr = i + 1, j, d
						elif d == 3:
							curr = i + 2, j, (d + 2) % 4
					else:
						if d == 0 or d == 3:
							curr = i, j - 1, d
						elif d == 1:
							curr = i - 1, j, d
						elif d == 2:
							curr = i + 1, j, d
			elif getsection(i - 1, size) == 1:
				if getsection(i + 1, size) == 1:
					if leftfacing:
						if j == len(row) - 1:
							if d == 0:
								curr = i - 1, j, d
							elif d == 1:
								curr = i + 2, j, (d + 2) % 4
							elif d == 2:
								curr = i + 2, j, (d + 2) % 4
							elif d == 3:
								curr = i + 1, j, d
						else:
							if d == 0:
								curr = i - 1, j, d
							elif d == 1 or d == 2:
								curr = i, j + 1, d
							elif d == 3:
								curr = i + 1, j, d
					else:
						if j == 0:
							if d == 0:
								curr = i + 2, j, (d + 2) % 4
							elif d == 1:
								curr = i - 1, j, d
							elif d == 2:
								curr = i + 1, j, d
							elif d == 3:
								curr = i + 2, j, (d + 2) % 4
						else:
							if d == 0 or d == 3:
								curr = i, j - 1, d
							elif d == 1:
								curr = i - 1, j, d
							elif d == 2:
								curr = i + 1, j, d
				elif getsection(i + 1, size) == 2:
					if leftfacing:
						if j == len(row) - 1:
							if d == 0:
								curr = i - 1, j, d
							elif d == 2:
								curr = i + 1, j, (d + 2) % 4
						else:
							if d == 0:
								curr = i - 1, j, d
							elif d == 1:
								curr = i, j + 1, d
							elif d == 2:
								curr = i, j + 1, d
							elif d == 3:
								curr = i + 1, j, d
					else:
						if d == 0:
							curr = i, j - 1, d
						elif d == 1:
							curr = i - 1, j, d
						elif d == 2:
							curr = i + 1, j, d
						elif d == 3:
							if j == 0:
								curr = i + 1, j, (d + 2) % 4
							else:
								curr = i, j - 1, d
		elif section == 2:
			if getsection(i - 1, size) == 1:
				if leftfacing:
					if d == 0:
						curr = i - 1, j, d
					elif d == 1:
						curr = i, j + 1, d
					elif d == 2:
						curr = i, j + 1, d
					elif d == 3:
						if j == 0:
							curr = i + 1, j, (d + 2) % 4
						else:
							curr = i + 1, j - 1, d
				else:
					if d == 0 or d == 3:
						curr = i, j - 1, d
					elif d == 1:
						curr = i - 1, j, d
					elif d == 2:
						if j == len(row) - 1:
							curr = i + 1, j - 2, (d + 2) % 4
						else:
							curr = i + 1, j - 1, d
			elif getsection(i - 1, size) == 2:
				if leftfacing:
					if d == 0:
						curr = i - 1, j + 1, d
					elif d == 1 or d == 2:
						curr = i, j + 1, d
					elif d == 3:
						if j == 0:
							curr = i + 1, j, (d + 2) % 4
						else:
							curr = i + 1, j - 1, d
				else:
					if j == len(row) - 1:
						if d == 0:
							curr = i, j - 1, d
						elif d == 1:
							curr = i - 1, j + 1, d
						elif d == 2:
							curr = i + 1, j - 2, (d + 2) % 4
					else:
						if d == 0 or d == 3:
							curr = i, j - 1, d
						elif d == 1:
							curr = i - 1, j + 1, d
						elif d == 2:
							curr = i + 1, j - 1, d
	# for i in range(len(pattern)):
	# 	for j in range(len(pattern[i])):
	# 		section = 0 if i <= size - 1 else (1 if i < 3 * size - 1 else 2)
	# 		leftfacing = [j % 2 == 0, j % 2 != (i - size) % 2, j % 2 == 0][section]
	# 		if not leftfacing:
	# 			print j,
	# 	print
	sidelen = (ISIZE - IMARGIN * 2) / (2.0 * size)
	altitude = sidelen * ALTCONST
	# print sidelen, altitude
	for i in range(len(pattern)):
		section = getsection(i, size)
		row = pattern[i]
		rowleft = (ISIZE / 2) - (altitude * len(row) / 2)
		if section % 2 == 0:
			evenrow = i % 2 == 0
			for j in range(len(row)):
				cell = row[j]
				top = ceil(i / 2.0) * sidelen - (0.5 * sidelen if not evenrow else 0) + IMARGIN
				bottom = top + sidelen
				if j % 2 == 0:
					points = [
						(rowleft + altitude * j, top + sidelen / 2),
						(rowleft + altitude * (j + 1), top), (rowleft + altitude * (j + 1), bottom)
					]
				else:
					points = [
						(rowleft + altitude * (j + 1), top + sidelen / 2),
						(rowleft + altitude * j, top), (rowleft + altitude * j, bottom)
					]
				draw_triangle(im, points, cell, size)
		else:
			evenrow = (i - size) % 2 == 1
			for j in range(len(row)):
				cell = row[j]
				top = ceil(i / 2.0) * sidelen - (0.5 * sidelen if i % 2 == 1 else 0) + IMARGIN
				bottom = top + sidelen
				if j % 2 == (i - size) % 2:
					points = [
						(rowleft + altitude * (j + 1), top + sidelen / 2),
						(rowleft + altitude * j, top), (rowleft + altitude * j, bottom)
					]
				else:
					points = [
						(rowleft + altitude * j, top + sidelen / 2),
						(rowleft + altitude * (j + 1), top), (rowleft + altitude * (j + 1), bottom)
					]
				draw_triangle(im, points, cell, size)
	return im

FLAG = "are_triangles_more_secure_than_squares?_%s"

def get_salt(random):
	salt = "".join([random.choice("0123456789abcdef") for i in range(8)])
	return salt

def generate_flag(random):
	salt = get_salt(random)
	im = generate_image("easyctf{%s}" % (FLAG % salt))
	flag = StringIO()
	im.save(flag, format="PNG")
	return flag

def generate(random):
	return dict(files={
		"flag.png": generate_flag
	})

def grade(random, key):
	salt = get_salt(random)
	if key.find(FLAG % salt) >= 0:
		return True, "Correct!"
	return False, "Nope."
