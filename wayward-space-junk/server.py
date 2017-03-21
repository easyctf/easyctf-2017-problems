import SocketServer
import os
import re
import time
from math import sin, cos, pi, sqrt, atan

equations = [
	lambda constant, offset, amp, theta: amp * sin(constant * theta) + offset,
	lambda constant, offset, amp, theta: amp * cos(constant * theta) + offset,
	lambda constant, offset, amp, theta: amp * atan(constant * theta) + offset
]

pattern = re.compile("\((\d+(?:.\d+)?),(?:\s+)?(\d+(?:.\d+)?)\)")

def dist(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return sqrt(dx * dx + dy * dy)

def p2r(r, theta):
	return (r * cos(theta), r * sin(theta))

class RequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.request.sendall("Please enter your pilot key: ")
		key = self.request.recv(1024).strip()

		import random
		random.seed(key)

		amplitude = random.uniform(5000, 10000)
		offset = random.uniform(5000, 10000)
		constant = random.uniform(0, 2 * pi)
		equation = random.choice(equations)
		period = random.uniform(400, 800)

		current_time = time.time()
		self.request.sendall("The current time is: %s\n" % current_time)
		self.request.sendall("Please enter the coordinates (x, y) you would like to hit:\n")

		theta = current_time
		while theta > period:
			theta -= period
		theta *= 2 * pi / period

		coordinates = self.request.recv(1024).strip()
		match = pattern.match(coordinates)
		if not match:
			self.request.sendall("Sorry, you didn't enter valid coordinates.\n")
			return

		x1, y1 = float(match.group(1)), float(match.group(2))
		x2, y2 = p2r(equation(constant, offset, amplitude, theta), theta)
		distance = dist(x1, y1, x2, y2)

		if distance < 10:
			random.seed("super%secretkeylalalala" % key)
			flag = "".join([random.choice("012456789abcdef") for i in range(32)])
			self.request.sendall("Perfect!\n")
			self.request.sendall("Your flag is: easyctf{%s}\n" % flag)
		else:
			self.request.sendall("You missed. You were (%.3f, %.3f) off.\n" % (x2 - x1, y2 - y1))
			# self.request.sendall("[DEBUG] Actual coordinates: (%.3f, %.3f)\n" % (x2, y2))


if __name__ == "__main__":
	HOST = os.getenv("HOST", "0.0.0.0")
	PORT = int(os.getenv("PORT", "8580"))
	server = SocketServer.TCPServer((HOST, PORT), RequestHandler)
	print "Listening on %s:%s" % (HOST, PORT)
	server.serve_forever()