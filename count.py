#!/usr/bin/env python

import os
import yaml
import traceback
from collections import Counter

problem_names = os.listdir(os.path.dirname(os.path.abspath(__file__)))
problems = []

failed = []
total = 0

for problem_name in problem_names:
	folder = os.path.dirname(os.path.abspath(__file__)) + os.sep + problem_name
	if not (os.path.exists(folder) and os.path.isdir(folder)): continue
	try:
		metadata_file = folder + os.sep + "problem.yml"
		with open(metadata_file, "r") as f:
			metadata_raw = f.read()
			metadata = yaml.load(metadata_raw)
			if "category" in metadata:
				problems.append(metadata)
	except:
		failed.append(problem_name)

problems.sort(key=lambda p: p.get("value"), reverse=True)
print("Grand Total: %d" % len(problems))
print("Category Breakdown:")

maxtitle = max(map(lambda p: len(p.get("title")), problems)) + 3
maxauthor = max(map(lambda p: len(p.get("author")), problems)) + 3

c = Counter(map(lambda p: p.get("category", ""), problems))
categories = sorted(c.items(), key=lambda c: c[1], reverse=True)
for category, count in categories:
	print("  %s: %s" % (category, count))
	for problem in problems:
		if problem.get("category") != category: continue
		total += int(problem.get("value"))
		print("    %s %s %sp" % (problem.get("title") + " " * (maxtitle - len(problem.get("title"))), problem.get("author") + " " * (maxauthor - len(problem.get("author"))), problem.get("value")))

print ("\nTOTAL VALUE: %d" % total)

print("\nThe following problems failed to parse.")
for title in failed:
	if title in [".git"]: continue
	print("    %s" % title)