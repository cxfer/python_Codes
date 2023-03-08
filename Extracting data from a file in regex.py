import re
den=open('equity.txt')
nulist=list()
for line in den:
	line=line.rstrip()
	ste=re.findall('dan',line)
	nulist.append(ste)
	
print(nulist)
