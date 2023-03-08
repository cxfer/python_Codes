import re

hand =open('equity.txt')
for line in hand:
	line=line.rstrip()
	if re.search('dan', line):
		print(line)

