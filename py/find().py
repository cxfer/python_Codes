hand =open('equity.txt')
for line in hand:
	line=line.rstrip()
	if line.find('hacking') >=0:
		print(line)
